#!/usr/bin/env python3
"""
Script to convert Supporting Contributor Application CSV responses into supporting.json format.

This script:
1. Reads the CSV file from Google Forms responses
2. Filters for approved entries only
3. Converts data to supporting.json format
4. Sets is_active based on end date (false if ended >3 years ago)
5. Completely replaces the content of supporting.json

Usage:
    python scripts/update_supporting_contributors.py <path_to_csv>

Example:
    python scripts/update_supporting_contributors.py ~/Downloads/form_responses.csv
"""

import csv
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path


def parse_date(date_str):
    """Parse date string in M/D/YY format and return ISO format string."""
    if not date_str or date_str.strip() == "":
        return None
    try:
        # Handle M/D/YY format
        dt = datetime.strptime(date_str.strip(), "%m/%d/%y")
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        try:
            # Try M/D/YYYY format
            dt = datetime.strptime(date_str.strip(), "%m/%d/%Y")
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            print(f"Warning: Could not parse date: {date_str}")
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


def csv_to_supporting_json(csv_path, output_path):
    """
    Convert CSV file to supporting.json format.
    
    Args:
        csv_path: Path to the CSV file
        output_path: Path to the output JSON file
    """
    contributors = []
    
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        # Use semicolon as delimiter based on the CSV format
        reader = csv.DictReader(csvfile, delimiter=';')
        
        for row in reader:
            # Only process approved entries
            approved = row.get('Approved (yes/no)', '').strip().lower()
            if approved != 'yes':
                continue
            
            # Determine if organization or individual
            entry_type = row.get('Individual or Organisation', '').strip()
            is_organization = entry_type.lower() == 'organisation'
            
            # Get the name (use Organization Name if org, otherwise Name)
            if is_organization:
                name = row.get('Organization Name', '').strip()
                if not name:
                    name = row.get('Name', '').strip()
            else:
                name = row.get('Name', '').strip()
            
            if not name:
                print(f"Warning: Skipping entry with no name: {row}")
                continue
            
            # Parse roles
            roles = parse_roles(row.get('Type of activities', ''))
            
            # Get description
            description = row.get('Description of contribution', '').strip()
            
            # Get link
            link = row.get('Website/Profile link', '').strip()
            
            # Get start and end dates
            start_date = parse_date(row.get('Please enter the start date of your activities with the QGIS community', ''))
            end_date = parse_date(row.get('Please enter the end date of your activities with the QGIS community', ''))
            
            # Determine if active
            is_active = is_active_contributor(end_date)
            
            # Generate avatar filename
            avatar_img = generate_avatar_filename(name, is_organization)
            
            # Create contributor entry
            contributor = {
                "name": name,
                "is_organization": is_organization,
                "is_active": is_active,
                "avatar_img": avatar_img,
                "link": link if link else None,
                "roles": roles,
                "contribution_description": description,
                "start_date": start_date,
                "end_date": end_date
            }
            
            contributors.append(contributor)
    
    # Sort by start date (oldest first), using a very old date for missing start dates
    contributors.sort(key=lambda x: x.get('start_date') or '9999-12-31')
    
    # Write to JSON file
    with open(output_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(contributors, jsonfile, indent=2, ensure_ascii=False)
    
    print(f"✅ Successfully converted {len(contributors)} approved contributors to {output_path}")
    print(f"   - Organizations: {sum(1 for c in contributors if c['is_organization'])}")
    print(f"   - Individuals: {sum(1 for c in contributors if not c['is_organization'])}")
    print(f"   - Active: {sum(1 for c in contributors if c['is_active'])}")
    print(f"   - Inactive: {sum(1 for c in contributors if not c['is_active'])}")
    
    # Print avatar filenames for reference
    print("\n📸 Avatar images needed (add these to static/img/contributors/):")
    for contributor in contributors:
        print(f"   - {contributor['avatar_img']}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/update_supporting_contributors.py <path_to_csv>")
        print("\nExample:")
        print("  python scripts/update_supporting_contributors.py ~/Downloads/form_responses.csv")
        sys.exit(1)
    
    csv_path = Path(sys.argv[1])
    if not csv_path.exists():
        print(f"❌ Error: CSV file not found: {csv_path}")
        sys.exit(1)
    
    # Output path relative to script location
    script_dir = Path(__file__).parent
    output_path = script_dir.parent / "data" / "contributors" / "supporting.json"
    
    print(f"📄 Reading CSV from: {csv_path}")
    print(f"💾 Writing JSON to: {output_path}")
    print()
    
    csv_to_supporting_json(csv_path, output_path)


if __name__ == "__main__":
    main()
