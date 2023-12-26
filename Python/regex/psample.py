import re

# File path
file_path = 'psample.txt'

# Open the file for reading
with open(file_path, 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Extract email addresses using a regular expression
        email_addresses = re.findall(r'[\w\.-]+@[\w\.-]+', line)

        # Extract phone numbers using a regular expression
        phone_numbers = re.findall(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', line)

        # Extract URLs using a regular expression
        url_pattern = r'https?://[\w.-]+/\S+'
        urls = re.findall(url_pattern, line)

        # Extract IP addresses using a regular expression
        ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        ips = re.findall(ip_pattern, line)

        # Extract credit card numbers using a regular expression
        credit_card_pattern = r'\b(?:\d{4}-?){3}\d{4}\b'
        credit_cards = re.findall(credit_card_pattern, line)

        # Print extracted data
        if email_addresses:
            print("Email Addresses:", email_addresses)
        if phone_numbers:
            print("Phone Numbers:", phone_numbers)
        if ips:
            print("IP Addresses:", ips)
        if credit_cards:
            print("Credit Cards:", credit_cards)
        if urls:
            print("URLs:", urls)
        print()
