#!/usr/bin/env python3
"""
Script to remove expired funders from content/funders directory.
Checks the endDate in each markdown file and removes both the .md file
and its associated logo if the membership has expired.
"""

import os
import re
from datetime import datetime
from pathlib import Path

# Directory containing funder files
FUNDERS_DIR = Path("content/funders")

# Current date for comparison
CURRENT_DATE = datetime.now().date()


def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    # Match YAML frontmatter between --- delimiters
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}
    
    frontmatter = {}
    for line in match.group(1).split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            frontmatter[key] = value
    
    return frontmatter


def parse_date(date_string):
    """Parse date string in various formats."""
    if not date_string:
        return None
    
    # Try different date formats
    formats = [
        "%Y-%m-%d",
        "%Y/%m/%d",
        "%d-%m-%Y",
        "%d/%m/%Y",
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_string, fmt).date()
        except ValueError:
            continue
    
    return None


def find_logo_file(md_file):
    """Find the logo file associated with a markdown file."""
    base_name = md_file.stem
    
    # Look for logo files with common extensions
    extensions = ['.png', '.jpg', '.jpeg', '.svg']
    for ext in extensions:
        logo_file = md_file.parent / f"{base_name}{ext}"
        if logo_file.exists():
            return logo_file
    
    return None


def is_expired(md_file):
    """Check if a funder membership has expired based on endDate."""
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        frontmatter = parse_frontmatter(content)
        
        # Skip index.md or files without endDate
        if md_file.name == 'index.md' or 'endDate' not in frontmatter:
            return False
        
        end_date_str = frontmatter.get('endDate', '')
        end_date = parse_date(end_date_str)
        
        if end_date and end_date < CURRENT_DATE:
            return True, end_date, frontmatter.get('title', 'Unknown')
        
        return False
    
    except Exception as e:
        print(f"Error processing {md_file}: {e}")
        return False


def remove_expired_funders(dry_run=True):
    """Remove expired funders and their logos."""
    if not FUNDERS_DIR.exists():
        print(f"Error: Directory {FUNDERS_DIR} does not exist")
        return
    
    removed_count = 0
    skipped_count = 0
    
    print(f"Scanning {FUNDERS_DIR} for expired funders...")
    print(f"Current date: {CURRENT_DATE}")
    print(f"Mode: {'DRY RUN' if dry_run else 'ACTUAL DELETION'}")
    print("-" * 80)
    
    # Get all markdown files
    md_files = sorted(FUNDERS_DIR.glob("*.md"))
    
    for md_file in md_files:
        result = is_expired(md_file)
        
        if result:
            expired, end_date, title = result
            
            # Find associated logo
            logo_file = find_logo_file(md_file)
            
            print(f"\n✗ EXPIRED: {title}")
            print(f"  File: {md_file.name}")
            print(f"  End Date: {end_date}")
            
            if logo_file:
                print(f"  Logo: {logo_file.name}")
            else:
                print(f"  Logo: Not found")
            
            if not dry_run:
                # Actually remove the files
                try:
                    md_file.unlink()
                    print(f"  → Deleted: {md_file.name}")
                    
                    if logo_file and logo_file.exists():
                        logo_file.unlink()
                        print(f"  → Deleted: {logo_file.name}")
                    
                    removed_count += 1
                except Exception as e:
                    print(f"  → Error deleting: {e}")
            else:
                print(f"  → Would delete (dry run)")
                removed_count += 1
        else:
            skipped_count += 1
    
    print("\n" + "=" * 80)
    print(f"Summary:")
    print(f"  Total files scanned: {len(md_files)}")
    print(f"  Expired funders found: {removed_count}")
    print(f"  Active/skipped: {skipped_count}")
    
    if dry_run:
        print("\n⚠ This was a DRY RUN. No files were actually deleted.")
        print("Run with --execute flag to actually delete files.")
    else:
        print(f"\n✓ Removed {removed_count} expired funders and their logos.")


if __name__ == "__main__":
    import sys
    
    # Check for --execute flag
    execute = '--execute' in sys.argv or '-e' in sys.argv
    
    if not execute:
        print("=" * 80)
        print("DRY RUN MODE - No files will be deleted")
        print("=" * 80)
        print()
    
    remove_expired_funders(dry_run=not execute)
    
    if not execute:
        print("\nTo actually delete files, run:")
        print("  python3 remove_expired_funders.py --execute")
