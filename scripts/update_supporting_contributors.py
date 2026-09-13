#!/usr/bin/env python3
"""
Script to convert Supporting Contributor Application XLSX responses into supporting.json format.

This script:
1. Reads the XLSX file from Google Forms responses
2. Checks that avatar images exist in static/img/contributors/supporting/
3. Resizes images to max 300px height
4. Filters for approved entries only
5. Converts data to supporting.json format
6. Sets is_active based on end date (false if ended >3 years ago)
7. Outputs email lists (BCC) for approved and rejected contributors
8. Generates a GeoJSON file with contributor locations

Usage:
    python scripts/update_supporting_contributors.py <path_to_xlsx>

Example:
    python scripts/update_supporting_contributors.py assets/csv/supporting_contributors.xlsx
"""

import json
import sys
import os
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd

# Import the resize_image function
sys.path.insert(0, str(Path(__file__).parent))
from resize_image import resize_image


def parse_date(date_input):
    """Parse date from pandas datetime or string and return ISO format string."""
    if pd.isna(date_input) or date_input is None:
        return None
    
    # If it's already a pandas datetime, convert directly
    if isinstance(date_input, pd.Timestamp):
        return date_input.strftime("%Y-%m-%d")
    
    # If it's a string, try parsing it
    if isinstance(date_input, str):
        date_str = date_input.strip()
        if not date_str:
            return None
        try:
            # Handle M/D/YY format
            dt = datetime.strptime(date_str, "%m/%d/%y")
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            try:
                # Try M/D/YYYY format
                dt = datetime.strptime(date_str, "%m/%d/%Y")
                return dt.strftime("%Y-%m-%d")
            except ValueError:
                print(f"Warning: Could not parse date: {date_str}")
                return None
    
    return None


def is_active_contributor(end_date_str):
    """
    Determine if contributor is active.
    Returns False if end date is more than 3 years ago, True otherwise.
    """
    if not end_date_str or end_date_str.strip() == "":
        # No end date means still active
        return True
    
    try:
        # Parse the date string back to datetime for comparison
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        three_years_ago = datetime.now() - timedelta(days=3*365)
        return end_date > three_years_ago
    except (ValueError, TypeError):
        # If we can't parse the date, assume active
        return True


def parse_roles(activities_str):
    """Parse the 'Type of activities' field into a list of roles."""
    if not activities_str or activities_str.strip() == "":
        return []
    
    # Split by comma and clean up
    roles = [role.strip() for role in activities_str.split(",")]
    return [role for role in roles if role]  # Remove empty strings


def generate_avatar_filename(name, is_org):
    """Generate a filename for the avatar image."""
    # Convert name to lowercase, replace spaces with underscores
    safe_name = name.lower().replace(" ", "_").replace(".", "")
    # Remove any special characters
    safe_name = "".join(c for c in safe_name if c.isalnum() or c == "_")
    return f"/img/contributors/supporting/{safe_name}.png"


def xlsx_to_supporting_json(xlsx_path, output_path, geojson_path):
    """
    Convert XLSX file to supporting.json and GeoJSON format.
    
    Args:
        xlsx_path: Path to the XLSX file
        output_path: Path to the output JSON file
        geojson_path: Path to the output GeoJSON file
    """
    # Load existing contributors to check for new entries
    existing_contributors = []
    if os.path.exists(output_path):
        with open(output_path, 'r', encoding='utf-8') as f:
            existing_contributors = json.load(f)
    
    existing_names = {c['name'].lower() for c in existing_contributors}
    
    contributors = []
    coord_map = {}  # name → (longitude, latitude) collected from XLSX
    approved_emails = []
    rejected_emails = []
    skipped_no_image = []
    
    # Get the project root directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Read the XLSX file
    df = pd.read_excel(xlsx_path)
    
    for idx, row in df.iterrows():
        # Get approval status - use "contains yes" instead of exact match
        approved = str(row.get('Approved (yes/no)', '')).strip().lower()
        is_approved = 'yes' in approved
        
        # Determine if organization or individual
        entry_type = str(row.get('Individual or Organisation', '')).strip()
        is_organization = entry_type.lower() == 'organisation'
        
        # Get the name (use Organization Name if org, otherwise Name)
        if is_organization:
            name = str(row.get('Organization Name', '')).strip()
            if not name or name == 'nan':
                name = str(row.get('Name', '')).strip()
        else:
            name = str(row.get('Name', '')).strip()
        
        if not name or name == 'nan':
            print(f"Warning: Skipping entry with no name at row {idx}")
            continue
        
        # Get email
        email = str(row.get('Email Address', '')).strip()
        if email == 'nan':
            email = ''
        
        # Check if this is a new contributor
        is_new_contributor = name.lower() not in existing_names
        
        # Generate avatar filename base (without extension)
        avatar_img = generate_avatar_filename(name, is_organization)
        avatar_base = avatar_img.rsplit('.', 1)[0]  # Remove .png extension
        
        # Check if approved
        if is_approved:
            # Check for image with various extensions
            possible_extensions = ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG']
            avatar_path = None
            final_avatar_img = None
            
            for ext in possible_extensions:
                test_path = project_root / 'static' / (avatar_base + ext).lstrip('/')
                if os.path.exists(test_path):
                    avatar_path = test_path
                    final_avatar_img = avatar_base + ext
                    break
            
            if not avatar_path:
                skipped_no_image.append({
                    'name': name,
                    'email': email,
                    'expected_path': str(project_root / 'static' / avatar_img.lstrip('/'))
                })
                continue
            
            # Resize the image
            try:
                resize_image(str(avatar_path), max_height=300)
            except Exception as e:
                print(f"Warning: Failed to resize image for {name}: {e}")
            
            # Parse roles
            roles = parse_roles(str(row.get('Type of activities', '')))
            
            # Get description - handle newlines correctly
            description = str(row.get('Description of contribution', '')).strip()
            if description == 'nan':
                description = ''
            
            # Get link
            link = str(row.get('Website/Profile link', '')).strip()
            if link == 'nan':
                link = ''
            
            # Get coordinates
            longitude = row.get('Location - Longitude')
            latitude = row.get('Location - Latitude')
            
            # Convert to float if possible
            try:
                longitude = float(longitude) if not pd.isna(longitude) else None
            except (ValueError, TypeError):
                longitude = None
            
            try:
                latitude = float(latitude) if not pd.isna(latitude) else None
            except (ValueError, TypeError):
                latitude = None
            
            # Get start and end dates
            start_date = parse_date(row.get('Please enter the start date of your activities with the QGIS community'))
            end_date = parse_date(row.get('Please enter the end date of your activities with the QGIS community'))
            
            # Determine if active
            is_active = is_active_contributor(end_date)
            
            # Create contributor entry
            contributor = {
                "name": name,
                "is_organization": is_organization,
                "is_active": is_active,
                "avatar_img": final_avatar_img,
                "link": link if link else None,
                "roles": roles,
                "contribution_description": description,
                "start_date": start_date,
                "end_date": end_date
            }
            
            # Only add to contributors list if new
            if is_new_contributor:
                contributors.append(contributor)
                
                if email:
                    approved_emails.append({'name': name, 'email': email})
            
            # Always store coordinates if present (for both new and existing)
            if longitude is not None and latitude is not None:
                coord_map[name] = (longitude, latitude)
            
        elif approved == 'no':
            # Collect rejected email (only for new rejections)
            if is_new_contributor and email:
                rejected_emails.append({'name': name, 'email': email})
    
    # Merge with existing contributors
    all_contributors = existing_contributors + contributors
    
    # Sort by start date (oldest first), using a very old date for missing start dates
    all_contributors.sort(key=lambda x: x.get('start_date') or '9999-12-31')
    
    # Build GeoJSON features using all_contributors as the property source
    # so every field value is identical to what is stored in supporting.json
    geojson_features = []
    for contributor in all_contributors:
        name = contributor['name']
        if name in coord_map:
            longitude, latitude = coord_map[name]
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [longitude, latitude]
                },
                "properties": dict(contributor)
            }
            geojson_features.append(feature)
    
    # Write to JSON file
    with open(output_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(all_contributors, jsonfile, indent=2, ensure_ascii=False)
    
    # Write GeoJSON file
    geojson = {
        "type": "FeatureCollection",
        "features": geojson_features
    }
    
    # Ensure output directory exists
    geojson_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(geojson_path, 'w', encoding='utf-8') as geojsonfile:
        json.dump(geojson, geojsonfile, indent=2, ensure_ascii=False)
    
    # Print summary
    print(f"✅ Successfully processed contributors")
    print(f"   - New approved contributors: {len(contributors)}")
    print(f"   - Total contributors in JSON: {len(all_contributors)}")
    print(f"   - GeoJSON features: {len(geojson_features)}")
    print(f"   - Skipped (no image): {len(skipped_no_image)}")
    print(f"   - Rejected: {len(rejected_emails)}")
    
    # Print skipped entries
    if skipped_no_image:
        print(f"\n⚠️  Skipped entries (image not found):")
        for entry in skipped_no_image:
            print(f"   - {entry['name']}: {entry['expected_path']}")
    
    # Print email information
    print("\n" + "="*80)
    print("📧 EMAIL NOTIFICATIONS")
    print("="*80)
    
    if approved_emails:
        print(f"\n✅ APPROVED CONTRIBUTORS ({len(approved_emails)}):")
        print("\nBCC Recipients:")
        bcc_list = "; ".join([f"{e['email']}" for e in approved_emails])
        print(f"{bcc_list}")
        
        print("\n--- Email Content (Approval) ---")
        print("Subject: ✅ Your QGIS Supporting Contributor Application - Approved")
        print("\nBody:")
        print("""Dear Contributor,

Thank you for your submission to become a QGIS Supporting Contributor!

We are pleased to inform you that your application has been approved. Your profile will be listed on our Supporting Contributors page soon at:
https://qgis.org/community/contributors/supporting/

Your contributions to the QGIS community are greatly valued and appreciated!

Best regards,
The QGIS Community Team""")
        print("\n" + "-"*80)
    
    if rejected_emails:
        print(f"\n❌ REJECTED APPLICATIONS ({len(rejected_emails)}):")
        print("\nBCC Recipients:")
        bcc_list = "; ".join([f"{e['email']}" for e in rejected_emails])
        print(f"{bcc_list}")
        
        print("\n--- Email Content (Rejection) ---")
        print("Subject: Re: Your QGIS Supporting Contributor Application")
        print("\nBody:")
        print("""Dear Contributor,

Thank you for your submission to become a QGIS Supporting Contributor.

After careful review, we are unable to approve your application at this time. This may be due to incomplete information or not meeting the current criteria.

Please review our application guidelines at https://qgis.org/community/contributors/application-guidelines to understand what is needed for acceptance. You are welcome to submit a new application with additional details about your contributions to the QGIS community.

Best regards,
The QGIS Community Team""")
        print("\n" + "-"*80)
    
    if not approved_emails and not rejected_emails:
        print("\n✨ No new notifications to send (all entries already processed)")
    
    print("\n" + "="*80)


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/update_supporting_contributors.py <path_to_xlsx>")
        print("\nExample:")
        print("  python scripts/update_supporting_contributors.py assets/csv/supporting_contributors.xlsx")
        sys.exit(1)
    
    xlsx_path = Path(sys.argv[1])
    if not xlsx_path.exists():
        print(f"❌ Error: XLSX file not found: {xlsx_path}")
        sys.exit(1)
    
    # Output paths relative to script location
    script_dir = Path(__file__).parent
    output_path = script_dir.parent / "data" / "contributors" / "supporting.json"
    geojson_path = script_dir.parent / "static" / "data" / "contributors" / "supporting_map.json"
    
    print(f"📄 Reading XLSX from: {xlsx_path}")
    print(f"💾 Writing JSON to: {output_path}")
    print(f"🗺️  Writing GeoJSON to: {geojson_path}")
    print()
    
    xlsx_to_supporting_json(xlsx_path, output_path, geojson_path)


if __name__ == "__main__":
    main()
