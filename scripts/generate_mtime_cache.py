#!/usr/bin/env python3
"""
One-off script to build a mtime cache from S3 object metadata.

Background
----------
S3's LastModified field reflects when an object was uploaded to S3, not the
original file's modification time. Tools like rclone store the original mtime
as a Unix timestamp in the object's custom metadata field ("mtime"). S3 does
not allow setting LastModified to an arbitrary past date, even via copy_object.

This script reads the mtime metadata from every object in the bucket via
parallel HEAD requests and writes a cache file:

    data/downloads/mtime_cache.json  ->  { "<s3-key>": "<iso-datetime>", ... }

The hourly update_s3_downloads.py then loads this cache (fast, no HEAD
requests) and uses it as the last_modified source, falling back to
LastModified for any key not in the cache.

Run this script once (or whenever the bucket contents change significantly):

    python scripts/generate_mtime_cache.py

Environment Variables (same as update_s3_downloads.py):
    S3_ENDPOINT_URL, S3_BUCKET_NAME, S3_ACCESS_KEY_ID, S3_SECRET_ACCESS_KEY,
    S3_REGION, S3_PREFIX
"""

import os
import sys
import json
import datetime
import concurrent.futures
from pathlib import Path
from typing import Dict, Optional, Tuple

try:
    from tqdm import tqdm
except ImportError:
    print("❌ Error: tqdm is not installed.  pip install tqdm")
    sys.exit(1)

try:
    import boto3
    from botocore.exceptions import ClientError, NoCredentialsError
except ImportError:
    print("❌ Error: boto3 is not installed.  pip install boto3")
    sys.exit(1)


def list_all_keys(s3_client, bucket: str, prefix: str) -> list:
    """Return all non-folder object keys in the bucket."""
    keys = []
    continuation_token = None

    with tqdm(desc="Listing objects", unit="file") as pbar:
        while True:
            kwargs = {"Bucket": bucket, "MaxKeys": 1000}
            if prefix:
                kwargs["Prefix"] = prefix + "/"
            if continuation_token:
                kwargs["ContinuationToken"] = continuation_token

            response = s3_client.list_objects_v2(**kwargs)

            for obj in response.get("Contents", []):
                key = obj["Key"]
                if key.endswith("/") or "//" in key:
                    continue
                keys.append(key)
                pbar.update(1)

            if response.get("IsTruncated"):
                continuation_token = response.get("NextContinuationToken")
            else:
                break

    return keys


def fetch_mtime(s3_client, bucket: str, key: str) -> Tuple[str, Optional[str]]:
    """Return (key, iso_timestamp) using mtime metadata, or None if absent."""
    try:
        response = s3_client.head_object(Bucket=bucket, Key=key)
        mtime_str = response.get("Metadata", {}).get("mtime")
        if mtime_str:
            dt = datetime.datetime.fromtimestamp(float(mtime_str), tz=datetime.timezone.utc)
            return key, dt.isoformat()
    except ClientError:
        pass
    return key, None


def main():
    bucket = os.getenv("S3_BUCKET_NAME", "qgis-download")
    access_key = os.getenv("S3_ACCESS_KEY_ID")
    secret_key = os.getenv("S3_SECRET_ACCESS_KEY")
    endpoint_url = os.getenv("S3_ENDPOINT_URL", "https://nbg1.your-objectstorage.com")
    region = os.getenv("S3_REGION", "us-east-1")
    prefix = os.getenv("S3_PREFIX", "").rstrip("/")

    if not access_key or not secret_key:
        print("❌ S3_ACCESS_KEY_ID and S3_SECRET_ACCESS_KEY are required")
        sys.exit(1)

    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region,
    )
    client_kwargs = {"region_name": region}
    if endpoint_url:
        client_kwargs["endpoint_url"] = endpoint_url
    s3 = session.client("s3", **client_kwargs)

    output_path = Path(__file__).parent.parent / "data" / "downloads" / "mtime_cache.json"

    print(f"🚀 Generating mtime cache for bucket: {bucket}")
    if endpoint_url:
        print(f"   Endpoint: {endpoint_url}")

    # Phase 1: list all keys
    try:
        keys = list_all_keys(s3, bucket, prefix)
    except NoCredentialsError:
        print("❌ AWS credentials not found")
        sys.exit(1)
    except ClientError as e:
        print(f"❌ Error accessing S3: {e}")
        sys.exit(1)

    print(f"   Found {len(keys)} files. Fetching mtime metadata in parallel...")

    # Phase 2: parallel HEAD requests
    cache: Dict[str, str] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(fetch_mtime, s3, bucket, key): key for key in keys}
        with tqdm(total=len(keys), desc="Fetching mtime", unit="file") as pbar:
            for future in concurrent.futures.as_completed(futures):
                key, iso_ts = future.result()
                if iso_ts is not None:
                    cache[key] = iso_ts
                pbar.update(1)

    print(f"   ✅ mtime resolved for {len(cache)}/{len(keys)} files")

    # Save cache
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)

    print(f"✅ Cache saved to: {output_path}")
    print("   Run update_s3_downloads.py to regenerate the download JSON files.")


if __name__ == "__main__":
    main()
