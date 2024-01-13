import re
import os

def parse_and_write_data(input_file_path, output_folder):
    # Open the input file for reading
    with open(input_file_path, 'r') as input_file:
        # Extract file name (excluding extension) for creating output files
        file_name = os.path.splitext(os.path.basename(input_file_path))[0]

        # Define output file paths for each type of data
        output_email_path = os.path.join(output_folder, f'{file_name}_email_addresses.txt')
        output_phone_path = os.path.join(output_folder, f'{file_name}_phone_numbers.txt')
        output_url_path = os.path.join(output_folder, f'{file_name}_urls.txt')
        output_ip_path = os.path.join(output_folder, f'{file_name}_ips.txt')
        output_credit_card_path = os.path.join(output_folder, f'{file_name}_credit_cards.txt')

        # Iterate over each line in the input file
        for line in input_file:
            # Extract email addresses using a regular expression
            email_addresses = re.findall(r'[\w\.-]+@[\w\.-]+', line)
            if email_addresses:
                with open(output_email_path, 'w') as output_email:
                    output_email.write('\n'.join(email_addresses) + '\n')

            # Extract phone numbers using a regular expression
            phone_numbers = re.findall(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', line)
            if phone_numbers:
                with open(output_phone_path, 'w') as output_phone:
                    output_phone.write('\n'.join(phone_numbers) + '\n')

            # Extract URLs using a regular expression
            url_pattern = r'https?://[\w.-]+/\S+'
            urls = re.findall(url_pattern, line)
            if urls:
                with open(output_url_path, 'w') as output_url:
                    output_url.write('\n'.join(urls) + '\n')

            # Extract IP addresses using a regular expression
            ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
            ips = re.findall(ip_pattern, line)
            if ips:
                with open(output_url_path, 'w') as output_ip:
                    output_ip.write('\n'.join(ips) + '\n')

            # Extract credit card numbers using a regular expression
            credit_card_pattern = r'\b(?:\d{4}-?){3}\d{4}\b'
            credit_cards = re.findall(credit_card_pattern, line)
            if credit_cards:
                with open(output_url_path, 'w') as output_credit_card:
                    output_credit_card.write('\n'.join(credit_cards) + '\n')


if __name__ == "__main__":

    # Specify the folder containing input files
    input_folder = '/home/champ'

    # Specify the folder for output files
    output_folder = 'output_files'

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            input_file_path = os.path.join(input_folder, filename)
            parse_and_write_data(input_file_path, output_folder)
