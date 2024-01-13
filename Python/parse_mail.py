import re

# File path
file_path = 'mail.txt'

# Open the file for reading
with open(file_path, 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Extract email addresses using a regular expression
        email_addresses = re.findall(r'[\w\.-]+@[\w\.-]+', line)

        # Iterate over the extracted email addresses and print them
        for address in email_addresses:
            print(address)
