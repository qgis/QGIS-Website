#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Payrexx Donor Management Script.

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

The script fetches new donors from Payrexx Transaction API (v1.11)
and updates the donors list accordingly.

Required environment variables:
- PAYREXX_INSTANCE: Your Payrexx instance name
- PAYREXX_API_SECRET: Your Payrexx API secret (for signature generation)
"""

import base64
import hashlib
import hmac
import json
import os
import re
import sys
from datetime import datetime, timedelta
from urllib.parse import urlencode

import requests

TIMESTAMP_FILE = "scripts/latest_payrexx_transaction.txt"
POSITIVE_VALUES = [
  'yes', 'ja', 'si', 'oui', 'sí', 'sim', 'да', 'tak', 'ano', 'igen',
  'はい', '是', 'evet', 'kyllä', 'ie', 'oo', 'taip', 'jah', 'bai',
  'áno', 'da', 'iya', 'نعم', 'כן', 'हाँ', 'ναι', 'ita', 'jo'
]


def log(msg):
  """Write message to log file."""
  with open('/tmp/payrexxhook.log', 'a', encoding="utf-8") as f:
    f.write(f'{msg}\n')


def format_name(name):
  """Clean and format donor names.
  
  Args:
    name (str): Raw name from API
    
  Returns:
    str: Formatted name with proper capitalization
  """
  # Remove trailing dots or commas
  name = re.sub(r'[.,]+$', '', name.strip())
  
  # Convert to title case (first letter uppercase, others lowercase)
  return name.title()


def update_donors(new_donor_name, donors_json_file):
  """Add or update donor in the donors list.
  
  Args:
    new_donor_name (str): Name of the donor to add
    donors_json_file (str): Path to the donors JSON file
  """
  # Read the existing donors from the JSON file
  try:
    with open(donors_json_file, 'r', encoding='utf-8') as f:
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
    print(f"Donor '{new_donor}' has been added to the list.")
  
  # Sort donors alphabetically by first name
  donors.sort()
  
  # Write the updated donors list back to the JSON file
  with open(donors_json_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


def remove_donor(donor_name, donors_json_file):
  """Remove donor from the donors list.
  
  Args:
    donor_name (str): Name of the donor to remove
    donors_json_file (str): Path to the donors JSON file
  """
  # Read the existing donors from the JSON file
  try:
    with open(donors_json_file, 'r', encoding='utf-8') as f:
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
    print(f"Donor '{donor}' has been removed from the list.")
  
  # Write the updated donors list back to the JSON file
  with open(donors_json_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)


def save_latest_timestamp(timestamp):
  """Save the latest timestamp to a file.
  
  Args:
    timestamp (str): Timestamp in YYYY-MM-DD HH:MM:SS format
  """
  with open(TIMESTAMP_FILE, "w", encoding='utf-8') as file:
    file.write(timestamp)


def get_latest_timestamp():
  """Retrieve the latest timestamp from a file.
  
  Returns:
    str: Latest timestamp or 30 days ago if not found
  """
  if os.path.exists(TIMESTAMP_FILE):
    with open(TIMESTAMP_FILE, "r", encoding='utf-8') as file:
      content = file.read().strip()
      if content:
        return content
  
  # Return timestamp from 30 days ago if no previous timestamp exists
  thirty_days_ago = datetime.now() - timedelta(days=30)
  return thirty_days_ago.strftime("%Y-%m-%d %H:%M:%S")


def generate_api_signature(query_string, api_secret):
  """Generate API signature for Payrexx authentication.
  
  Args:
    query_string (str): URL encoded query parameters
    api_secret (str): Payrexx API secret
    
  Returns:
    str: Base64 encoded HMAC signature
  """
  signature = hmac.new(
    api_secret.encode('utf-8'),
    query_string.encode('utf-8'),
    hashlib.sha256
  ).digest()
  return base64.b64encode(signature).decode('utf-8')


def get_donors(donors_json_file, custom_field_label):
  """Retrieve and process donations from Payrexx Transaction API.
  
  Fetches transactions created after the latest timestamp and updates
  the donors list based on customer preferences in custom fields.
  
  Args:
    donors_json_file (str): Path to the donors JSON file
    custom_field_label (str): Name of the custom field to check for consent
  """
  latest_timestamp = get_latest_timestamp()

  payrexx_instance = os.getenv("PAYREXX_INSTANCE")
  payrexx_api_secret = os.getenv("PAYREXX_API_SECRET")

  if not payrexx_instance or not payrexx_api_secret:
    print("Error: Payrexx instance name and API secret are required.")
    sys.exit(1)
  
  base_url = "https://api.payrexx.com/v1.11/Transaction/"
  current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  
  # Prepare initial query parameters
  params = {
    "filterDatetimeUtcGreaterThan": latest_timestamp,
    "filterDatetimeUtcLessThan": current_time,
    "limit": 100,
    "offset": 0,
  }
  
  all_transactions = []
  new_latest_timestamp = latest_timestamp
  
  print(f"Fetching transactions since: {latest_timestamp}")
  
  # Paginated API requests
  while True:
    query_string = urlencode(params)
    api_signature = generate_api_signature(query_string, payrexx_api_secret)
    
    request_params = params.copy()
    request_params["ApiSignature"] = api_signature
    
    try:
      response = requests.get(
        f"{base_url}?instance={payrexx_instance}",
        params=request_params,
        headers={"accept": "application/json"},
        timeout=30
      )
      response.raise_for_status()
      result = response.json()
      
      if result.get("status") != "success":
        print(f"API returned error: {result}")
        break
      
      transactions = result.get('data', [])
      
      if not transactions:
        break
      
      all_transactions.extend(transactions)
      params["offset"] += len(transactions)
      
      # If we got less than the limit, we've reached the end
      if len(transactions) < params["limit"]:
        break
    
    except requests.exceptions.RequestException as e:
      print(f"Error fetching transactions from Payrexx: {e}")
      return
  
  print(f"Found {len(all_transactions)} transactions to process")
  
  # Process each transaction
  for transaction in all_transactions:
    transaction_time = transaction.get('time')
    if not transaction_time:
      continue
    
    # Update the latest timestamp
    if transaction_time > new_latest_timestamp:
      new_latest_timestamp = transaction_time
    
    # Skip transactions that are not confirmed/authorized
    status = transaction.get('status', '').lower()
    if status not in ['confirmed', 'authorized']:
      continue
    
    contact = transaction.get('contact')
    if not contact:
      continue
    
    # Get name from contact
    firstname = contact.get('firstname', '').strip()
    lastname = contact.get('lastname', '').strip()
    
    if not (firstname or lastname):
      continue
    
    name = f"{firstname} {lastname}".strip()
    
    # Check if the donor wants to be listed (default to False)
    list_me_as_donor = False
    
    # Check custom fields in the invoice
    invoice = transaction.get('invoice', {})
    custom_fields = invoice.get('customFields', [])
    
    if custom_fields:
      for field_data in custom_fields:
        field_name = field_data.get('name', '').lower()
        field_value = field_data.get('value', '').strip().lower()
        
        if custom_field_label.lower() in field_name:
          list_me_as_donor = field_value in POSITIVE_VALUES
          break
    
    # Update donor list based on preference
    if list_me_as_donor:
      update_donors(name, donors_json_file)
    else:
      remove_donor(name, donors_json_file)
  
  # Save the latest timestamp if new transactions were processed
  if new_latest_timestamp > latest_timestamp:
    save_latest_timestamp(new_latest_timestamp)
    print(f"Updated latest timestamp to: {new_latest_timestamp}")
  else:
    print("No new transactions found.")


def main():
  """Main function to run the donor update process."""
  custom_field_label = "Add me as donor"
  donors_json_file = 'data/donors.json'
  
  print("Starting Payrexx donor update...")
  print(f"Custom field to check: '{custom_field_label}'")
  print(f"Output file: {donors_json_file}")
  
  get_donors(donors_json_file, custom_field_label)
  
  print("Payrexx donor update completed.")


if __name__ == "__main__":
  main()