import re
import os

def extract_email_addresses(line):
    return re.findall(r'[\w\.-]+@[\w\.-]+', line)

def extract_phone_numbers(line):
    return re.findall(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', line)

def extract_urls(line):
    url_pattern = r'https?://[\w.-]+/\S+'
    return re.findall(url_pattern, line)

def extract_ips(line):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    return re.findall(ip_pattern, line)

def extract_credit_cards(line):
    credit_card_pattern = r'\b(?:\d{4}-?){3}\d{4}\b'
    return re.findall(credit_card_pattern, line)

def parse_and_write_data(input_file_path, output_folder):
    with open(input_file_path, 'r') as input_file:
        file_name = os.path.splitext(os.path.basename(input_file_path))[0]

        output_email_path = os.path.join(output_folder, f'{file_name}_email_addresses.txt')
        output_phone_path = os.path.join(output_folder, f'{file_name}_phone_numbers.txt')
        output_url_path = os.path.join(output_folder, f'{file_name}_urls.txt')
        output_ip_path = os.path.join(output_folder, f'{file_name}_ips.txt')
        output_credit_card_path = os.path.join(output_folder, f'{file_name}_credit_cards.txt')

        with open(output_email_path, 'w') as output_email, \
             open(output_phone_path, 'w') as output_phone, \
             open(output_url_path, 'w') as output_url, \
             open(output_ip_path, 'w') as output_ip, \
             open(output_credit_card_path, 'w') as output_credit_card:

            for line in input_file:
                email_addresses = extract_email_addresses(line)
                if email_addresses:                
                    output_email.write('\n'.join(email_addresses) + '\n')

                phone_numbers = extract_phone_numbers(line)
                if phone_numbers:
                    output_phone.write('\n'.join(phone_numbers) + '\n')

                urls = extract_urls(line)
                if urls:
                    output_url.write('\n'.join(urls) + '\n')

                ips = extract_ips(line)
                if ips:
                    output_ip.write('\n'.join(ips) + '\n')

                credit_cards = extract_credit_cards(line)
                if credit_cards:
                    output_credit_card.write('\n'.join(credit_cards) + '\n')

def process_all_files(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            input_file_path = os.path.join(input_folder, filename)
            parse_and_write_data(input_file_path, output_folder)

# Specify the folder containing input files
input_folder = 'input_files'

# Specify the folder for output files
output_folder = 'output_files2'

# Process all files in the input folder
process_all_files(input_folder, output_folder)