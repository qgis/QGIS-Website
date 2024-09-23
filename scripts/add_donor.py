#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script should be run from the root repo directory (../)

$ python scripts/add_donor.py "John Doe"

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


def log(msg):
    with open('/tmp/stripehook.log', 'a', encoding="utf-8") as f:
        f.write('{}\n'.format(msg))

# Function to clean and format names
def format_name(name):
    # Remove trailing dots or commas
    name = re.sub(r'[.,]+$', '', name.strip())

    # Ensure that the first letter of each word is capitalized
    # Convert to title case (first letter uppercase, others lowercase)
    name = name.title()
    return name


# Function to update donors list with the new name
def update_donors(new_donor_name, donors_json_file):
    # Read the existing donors from the JSON file
    try:
        with open(donors_json_file, 'r') as f:
            data = json.load(f)
            donors = data.get("donors", [])
    except FileNotFoundError:
        donors = []
        data = {"donors": donors}

    # Clean and format the new donor's name
    new_donor = format_name(new_donor_name)

    # Add the new donor to the list if not already present
    if new_donor not in donors:
        donors.append(new_donor)

    # Sort donors alphabetically by first name
    donors.sort()

    # Write the updated donors list back to the JSON file
    with open(donors_json_file, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python add_donor.py \"John Doe\"")
        sys.exit(1)

    new_donor_name = sys.argv[1]  # Name passed as argument
    log(f"Adding new donor: {new_donor_name}")
    donors_json_file = 'data/donors.json'  # Path to the donors.json file

    # Update the donors list with the new name
    update_donors(new_donor_name, donors_json_file)
    print(f"Donor '{new_donor_name}' has been added and the list updated.")