#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script should be run from the root repo directory (../)

$ python scripts/update_donors_from_file.py <path_to_donors.txt> [<path_to_donors2.txt> ...]

For the upcoming donors list, there will be
a text file that contains one name per line

It will update the json file (donors.json)
ordered alphabetically by the first name.

All names should start with a capital letter,
names where all characters are capitalized
should be converted to lower case letters
(except for the first character of the name).

Trailing dots or commas should be removed.
If a name is already in the list, it should
not be added again.

"""
import json
import re
import sys
import os


# Function to clean and format names
def format_name(name):
    # Remove trailing dots or commas
    name = re.sub(r'[.,]+$', '', name.strip())

    # Ensure that the first letter of each word is capitalized
    # Convert to title case (first letter uppercase, others lowercase)
    name = name.title()
    return name


# Function to update donors list with new names
def update_donors(new_donors_files, donors_json_file):
    # Read the existing donors from the JSON file
    try:
        with open(donors_json_file, 'r') as f:
            data = json.load(f)
            donors = data.get("donors", [])
    except FileNotFoundError:
        donors = []
        data = {"donors": donors}

    # Process each input donor file
    for new_donors_file in new_donors_files:
        # Check if the new donors file exists
        if not os.path.isfile(new_donors_file):
            print(f"Error: The file '{new_donors_file}' does not exist.")
            continue

        # Read new donors from the text file
        with open(new_donors_file, 'r') as f:
            new_donors = f.readlines()

        # Clean and format new donors, add to the list if not already present
        for donor in new_donors:
            donor = format_name(donor)
            if donor not in donors:
                donors.append(donor)

    # Sort donors alphabetically by first name
    donors.sort()

    # Write the updated donors list back to the JSON file
    with open(donors_json_file, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Usage: python update_donors.py <path_to_donors1.txt> [<path_to_donors2.txt> ...]"
        )
        sys.exit(1)
    new_donors_files = sys.argv[1:]  # List of input files
    donors_json_file = 'data/donors.json' # Output JSON file
    update_donors(new_donors_files, donors_json_file)
    print("Donors list has been updated.")
