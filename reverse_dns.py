import subprocess
import csv
import argparse

# Function to resolve domain to IP
def resolve_domain(domain):
    try:
        ip = subprocess.check_output(['dig', '+short', domain], universal_newlines=True).strip().split('\n')
        return ip[-1] if ip else None
    except Exception as e:
        return None

# Set up argument parsing
parser = argparse.ArgumentParser(description='Resolve domains to IP addresses and save to a CSV file.')
parser.add_argument('input_file', help='The input text file containing the list of domains')
parser.add_argument('output_file', help='The base name for the output CSV file (without .csv extension)')
args = parser.parse_args()

# Construct output file name
output_file = f"{args.output_file}.csv"

# Open CSV file for writing
with open(output_file, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write headers for two different sections
    csv_writer.writerow(['IP Addresses'])
    
    # Read domains from input file
    with open(args.input_file, 'r') as file:
        domains = file.readlines()

    # Initialize row counters
    row_domains_ips = []

    # Loop through each domain and resolve
    for line in domains:
        domain = line.strip().replace('http://', '').replace('https://', '').replace('www.', '')
        ip = resolve_domain(domain)

        # Write IPs and domains
        if ip:
            row_domains_ips.append([domain, ip])
            csv_writer.writerow([ip])
        else:
            row_domains_ips.append([domain, 'No IP found'])

# Write domain-IP pairs to the CSV
csv_writer.writerow([])
csv_writer.writerow(['Domain', 'IP Address'])
csv_writer.writerows(row_domains_ips)

print(f"Data has been written to {output_file}.")
