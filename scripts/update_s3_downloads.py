#!/usr/bin/env python3
"""
Script to fetch S3 bucket contents and generate a JSON file with file metadata.

This script:
1. Connects to an S3 bucket (AWS or compatible)
2. Recursively fetches all files and folders
3. Extracts metadata (size, modified date, type, etc.)
4. Generates a structured JSON file for the file explorer

Usage:
    python scripts/update_s3_downloads.py

Environment Variables:
    S3_ENDPOINT_URL: S3 endpoint URL (optional, for S3-compatible services)
    S3_BUCKET_NAME: Name of the S3 bucket
    S3_ACCESS_KEY_ID: AWS access key ID
    S3_SECRET_ACCESS_KEY: AWS secret access key
    S3_REGION: AWS region (default: us-east-1)
    S3_PREFIX: Prefix/folder to filter objects (optional)
"""

import os
import sys
import json
import mimetypes
import datetime
from pathlib import Path
from typing import List, Dict, Optional

try:
    import boto3
    from botocore.exceptions import ClientError, NoCredentialsError
except ImportError:
    print("❌ Error: boto3 is not installed. Install it with:")
    print("   pip install boto3")
    sys.exit(1)


class S3FileExplorer:
    """Fetch and organize S3 bucket contents."""

    def __init__(
        self,
        bucket_name: str,
        access_key: str,
        secret_key: str,
        endpoint_url: Optional[str] = None,
        region: str = "us-east-1",
        prefix: str = "",
    ):
        """Initialize S3 client."""
        self.bucket_name = bucket_name
        self.prefix = prefix.rstrip("/")
        
        # Initialize S3 client
        session = boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region,
        )
        
        client_kwargs = {"region_name": region}
        if endpoint_url:
            client_kwargs["endpoint_url"] = endpoint_url
        
        self.s3_client = session.client("s3", **client_kwargs)
        
        # Initialize MIME types
        mimetypes.init()

    def get_file_category(self, key: str) -> str:
        """Determine file category based on extension."""
        ext = Path(key).suffix.lower()
        
        categories = {
            "installer": [".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm", ".appimage"],
            "archive": [".zip", ".tar", ".gz", ".bz2", ".7z", ".rar", ".xz"],
            "document": [".pdf", ".doc", ".docx", ".txt", ".md", ".rst"],
            "image": [".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico"],
            "video": [".mp4", ".avi", ".mov", ".mkv", ".webm"],
            "data": [".json", ".xml", ".csv", ".yaml", ".yml"],
            "source": [".py", ".js", ".cpp", ".h", ".c", ".java"],
        }
        
        for category, extensions in categories.items():
            if ext in extensions:
                return category
        
        return "other"

    def format_size(self, size_bytes: int) -> str:
        """Convert bytes to human-readable format."""
        for unit in ["B", "KB", "MB", "GB", "TB"]:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} PB"

    def fetch_bucket_contents(self) -> List[Dict]:
        """Fetch all objects from S3 bucket."""
        print(f"📦 Fetching contents from bucket: {self.bucket_name}")
        if self.prefix:
            print(f"   With prefix: {self.prefix}")
        
        files = []
        continuation_token = None
        total_objects = 0
        
        try:
            while True:
                list_kwargs = {
                    "Bucket": self.bucket_name,
                    "MaxKeys": 1000,
                }
                
                if self.prefix:
                    list_kwargs["Prefix"] = self.prefix + "/"
                
                if continuation_token:
                    list_kwargs["ContinuationToken"] = continuation_token
                
                response = self.s3_client.list_objects_v2(**list_kwargs)
                
                if "Contents" not in response:
                    print("   No objects found in bucket")
                    break
                
                for obj in response["Contents"]:
                    key = obj["Key"]
                    
                    # Skip folders (keys ending with /)
                    if key.endswith("/"):
                        continue
                    
                    # Skip paths with double slashes (malformed paths)
                    if "//" in key:
                        continue
                    
                    # Get file metadata (only essential fields for lightweight output)
                    file_info = {
                        "key": key,
                        "name": Path(key).name,
                        "path": str(Path(key).parent) if Path(key).parent != Path(".") else "",
                        "size": obj["Size"],
                        "size_formatted": self.format_size(obj["Size"]),
                        "last_modified": obj["LastModified"].isoformat(),
                        "last_modified_timestamp": int(obj["LastModified"].timestamp()),
                        "extension": Path(key).suffix.lower(),
                        "category": self.get_file_category(key),
                    }
                    
                    files.append(file_info)
                    total_objects += 1
                
                # Check if there are more objects to fetch
                if response.get("IsTruncated"):
                    continuation_token = response.get("NextContinuationToken")
                else:
                    break
            
            print(f"   ✅ Found {total_objects} files")
            return files
        
        except NoCredentialsError:
            print("❌ Error: AWS credentials not found")
            sys.exit(1)
        except ClientError as e:
            print(f"❌ Error accessing S3: {e}")
            sys.exit(1)

    def build_file_tree(self, files: List[Dict]) -> Dict:
        """Build hierarchical file tree from flat file list."""
        tree = {
            "name": self.bucket_name,
            "type": "folder",
            "path": "",
            "children": [],
            "files": [],
        }
        
        # Folders to exclude from the tree (prevent memory overload from large repos)
        excluded_folder_prefixes = ('ubuntu', 'debian')
        
        for file in files:
            path_parts = file["path"].split("/") if file["path"] else []
            
            # Skip files in excluded folders
            if path_parts and any(path_parts[0].lower().startswith(prefix) for prefix in excluded_folder_prefixes):
                continue
            
            # Navigate/create directory structure
            current_level = tree
            current_path = ""
            
            for part in path_parts:
                if not part:
                    continue
                
                current_path = f"{current_path}/{part}" if current_path else part
                
                # Check if directory exists at this level
                dir_exists = False
                for child in current_level["children"]:
                    if child["name"] == part and child["type"] == "folder":
                        current_level = child
                        dir_exists = True
                        break
                
                # Create directory if it doesn't exist
                if not dir_exists:
                    new_dir = {
                        "name": part,
                        "type": "folder",
                        "path": current_path,
                        "children": [],
                        "files": [],
                    }
                    current_level["children"].append(new_dir)
                    current_level = new_dir
            
            # Add file to current directory level
            current_level["files"].append(file)
        
        # Sort directories and files
        def sort_tree(node):
            if "children" in node:
                node["children"].sort(key=lambda x: x["name"].lower())
                for child in node["children"]:
                    sort_tree(child)
            if "files" in node:
                node["files"].sort(key=lambda x: x["name"].lower())
        
        sort_tree(tree)
        return tree

    def generate_statistics(self, files: List[Dict]) -> Dict:
        """Generate statistics about the bucket contents."""
        stats = {
            "total_files": len(files),
            "total_size": sum(f["size"] for f in files),
            "total_size_formatted": self.format_size(sum(f["size"] for f in files)),
            "by_category": {},
            "by_extension": {},
            "last_updated": datetime.datetime.now(datetime.UTC).isoformat(),
        }
        
        # Count by category
        for file in files:
            category = file["category"]
            if category not in stats["by_category"]:
                stats["by_category"][category] = {
                    "count": 0,
                    "size": 0,
                }
            stats["by_category"][category]["count"] += 1
            stats["by_category"][category]["size"] += file["size"]
        
        # Format sizes for categories
        for category in stats["by_category"]:
            stats["by_category"][category]["size_formatted"] = self.format_size(
                stats["by_category"][category]["size"]
            )
        
        # Count by extension (top 10)
        ext_counts = {}
        for file in files:
            ext = file["extension"] or "no extension"
            ext_counts[ext] = ext_counts.get(ext, 0) + 1
        
        sorted_exts = sorted(ext_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        stats["by_extension"] = dict(sorted_exts)
        
        return stats

    def save_to_json(self, files: List[Dict], output_path: str):
        """Save files data to JSON."""
        tree = self.build_file_tree(files)
        stats = self.generate_statistics(files)
        
        data = {
            "bucket_name": self.bucket_name,
            "prefix": self.prefix,
            "generated_at": datetime.datetime.now(datetime.UTC).isoformat(),
            "statistics": stats,
            "tree": tree,
            "files": files,
        }
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Saved file data to: {output_path}")
        print(f"   Total files: {stats['total_files']}")
        print(f"   Total size: {stats['total_size_formatted']}")


def main():
    """Main entry point."""
    # Get configuration from environment variables
    bucket_name = os.getenv("S3_BUCKET_NAME", "qgis-download")
    access_key = os.getenv("S3_ACCESS_KEY_ID")
    secret_key = os.getenv("S3_SECRET_ACCESS_KEY")
    endpoint_url = os.getenv("S3_ENDPOINT_URL", "https://nbg1.your-objectstorage.com")
    region = os.getenv("S3_REGION", "us-east-1")
    prefix = os.getenv("S3_PREFIX", "")
    
    # Validate required variables
    if not bucket_name:
        print("❌ Error: S3_BUCKET_NAME environment variable is required")
        sys.exit(1)
    
    if not access_key or not secret_key:
        print("❌ Error: S3_ACCESS_KEY_ID and S3_SECRET_ACCESS_KEY are required")
        sys.exit(1)
    
    # Output path
    script_dir = Path(__file__).parent
    output_path = script_dir.parent / "data" / "s3_downloads.json"
    
    print("🚀 Starting S3 Downloads Update")
    print(f"   Bucket: {bucket_name}")
    print(f"   Region: {region}")
    if endpoint_url:
        print(f"   Endpoint: {endpoint_url}")
    
    # Fetch and save
    explorer = S3FileExplorer(
        bucket_name=bucket_name,
        access_key=access_key,
        secret_key=secret_key,
        endpoint_url=endpoint_url,
        region=region,
        prefix=prefix,
    )
    
    files = explorer.fetch_bucket_contents()
    explorer.save_to_json(files, str(output_path))
    
    print("\n✨ S3 downloads data updated successfully!")


if __name__ == "__main__":
    main()
