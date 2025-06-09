#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script should be run from the root repo directory (../)

$ python scripts/update_payrexx_donors.py

It will update the json file (data/donors.json)
ordered alphabetically by the first name.

All names should start with a capital letter,
names where all characters are capitalized
should be converted to lower case letters
(except for the first character of each word).

Trailing dots or commas should be removed.
If a name is already in the list, it should
not be added again.

The script fetches new donors from Payrexx API
and updates the donors list accordingly.
"""

import json
import re
import sys
import os
import requests
from datetime import datetime

TIMESTAMP_FILE = "scripts/latest_payrexx_donation.txt"

def log(msg):
    with open('/tmp/payrexxhook.log', 'a', encoding="utf-8") as f:
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

# Function to remove a donor from the list
def remove_donor(donor_name, donors_json_file):
    # Read the existing donors from the JSON file
    try:
        with open(donors_json_file, 'r') as f:
            data = json.load(f)
            donors = data.get("donors", [])
    except FileNotFoundError:
        print("Donors list not found.")
        return

    # Clean and format the donor's name
    donor = format_name(donor_name)

    # Remove the donor from the list if present
    if donor in donors:
        donors.remove(donor)

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
            content = file.read().strip()
            if content:
                return int(content)
    return 0  # Return 0 if the file does not exist or is empty

def get_donors(donors_json_file, custom_field_label):
    """
        Retrieve donations created after the latest timestamp.

        list_me_as_donor determines whether 
        a customer should be listed as a donor 
        based on form fields.
        It defaults to True if no specific preference is found.
        It is updated based on the customer's form fields if available.
        This ensures that only customers who have opted to be listed as donors are 
        included in the donors list.

        Steps:
            1. Retrieve the latest timestamp from a file.
            2. Fetch invoices from Payrexx created after the latest timestamp.
            3. Iterate through each invoice:
                - Get the contact information and donation preference
                - Determine if the customer should be listed as a donor
            4. Update the donors list by adding or removing the customer based on their preference.
            5. Update and save the latest timestamp if new donations are found.
    """
    latest_timestamp = get_latest_timestamp()
    payrexx_instance = os.getenv("PAYREXX_INSTANCE")
    payrexx_api_key = os.getenv("PAYREXX_API_KEY")
    
    if not payrexx_instance or not payrexx_api_key:
        print("Please set the PAYREXX_INSTANCE and PAYREXX_API_KEY environment variables.")
        sys.exit(1)

    base_url = f"https://api.payrexx.com/v1.0/Invoice/"
    headers = {
        "accept": "application/json",
    }
    params = {
        "instance": payrexx_instance,
        "apiKey": payrexx_api_key,
    }

    try:
        response = requests.get(base_url, headers=headers, params=params)
        response.raise_for_status()
        invoices = response.json()['data']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching invoices from Payrexx: {e}")
        return

    new_latest_timestamp = latest_timestamp
    
    for invoice in invoices:
        invoice_time = int(invoice['time'])
        if invoice_time <= latest_timestamp:
            continue
            
        contact = invoice.get('contact')
        if not contact:
            continue
            
        name = contact.get('company') or f"{contact.get('forename')} {contact.get('surname')}"
        if not name:
            continue
            
        # Check if the donor wants to be listed
        list_me_as_donor = True  # Default to True if not specified
        form_fields = invoice.get('fields', [])
        for field in form_fields:
            if field.get('name', '').lower() == custom_field_label.lower():
                list_me_as_donor = field.get('value', '').strip().lower() == 'yes'
                break

        if list_me_as_donor:
            update_donors(name, donors_json_file)
        else:
            remove_donor(name, donors_json_file)
            
        new_latest_timestamp = max(new_latest_timestamp, invoice_time)

    # Save the latest timestamp if new donations are found
    if new_latest_timestamp > latest_timestamp:
        save_latest_timestamp(new_latest_timestamp)

if __name__ == "__main__":
    custom_field_label = os.getenv("LIST_AS_DONOR_LABEL", "List me as a donor")
    donors_json_file = 'data/donors.json'  # Path to the donors.json file
    get_donors(donors_json_file, custom_field_label)