#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script should be run from the root repo directory (../)

$ python scripts/update_donors.py

It will update the json file (data/donors.json)
ordered alphabetically by the first name.

All names should start with a capital letter,
names where all characters are capitalized
should be converted to lower case letters
(except for the first character of each word).

Trailing dots or commas should be removed.
If a name is already in the list, it should
not be added again.

The script fetches new donors from Stripe API
and updates the donors list accordingly.
"""

import json
import re
import sys
import stripe
import os

TIMESTAMP_FILE = "scripts/latest_donation.txt"

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
        print(f"Donor '{new_donor_name}' has been added to the list.")

    # Sort donors alphabetically by first name
    donors.sort()

    # Write the updated donors list back to the JSON file
    with open(donors_json_file, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def save_latest_timestamp(timestamp):
    """Save the latest timestamp to a file."""
    with open(TIMESTAMP_FILE, "w") as file:
        file.write(str(timestamp))

def get_latest_timestamp():
    """Retrieve the latest timestamp from a file."""
    if os.path.exists(TIMESTAMP_FILE):
        with open(TIMESTAMP_FILE, "r") as file:
            return int(file.read().strip())
    return 0  # Return 0 if the file does not exist (fetch all donations initially)

def get_donors(donors_json_file):
    """Retrieve donations created after the latest timestamp."""
    latest_timestamp = get_latest_timestamp()
    donors = []

    charges = stripe.Charge.list(limit=100, created={'gt': latest_timestamp})
    new_latest_timestamp = latest_timestamp
    while True:
        for charge in charges['data']:
            if charge['paid'] and not charge['refunded']:
                donor = {
                    "name": charge.get('billing_details', {}).get('name'),
                    "date": charge['created'],
                }
                new_donor_name = donor['name']
                # Update the donors list with the new name
                update_donors(new_donor_name, donors_json_file)
                new_latest_timestamp = max(new_latest_timestamp, donor['date'])
        if not charges['has_more']:
            break
        last_charge = charges['data'][-1]
        charges = stripe.Charge.list(
            limit=100,
            starting_after=last_charge['id'],
            created={'gt': latest_timestamp}
        )

    # Save the latest timestamp if new donations are found
    if new_latest_timestamp > latest_timestamp:
        save_latest_timestamp(new_latest_timestamp)
    return donors

if __name__ == "__main__":
    api_key = os.getenv("STRIPE_API_KEY")
    if not api_key:
        print("Please set the STRIPE_API_KEY environment variable.")
        sys.exit(1)
    stripe.api_key = api_key
    donors_json_file = 'data/donors.json'  # Path to the donors.json file
    new_donors = get_donors(donors_json_file)
    for donor in new_donors:
        new_donor_name = donor['name']
        # Update the donors list with the new name
        update_donors(new_donor_name, donors_json_file)