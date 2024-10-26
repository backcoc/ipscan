# Domain Resolver Script

This project contains a Python script that resolves a list of domains to their corresponding IP addresses and saves the results in either an Excel or CSV file.

## Features

- Resolves domain names to IP addresses using `dig`.
- Outputs results to an Excel file with two sheets or a CSV file with multiple sections.
- Handles domains with or without HTTP/HTTPS prefixes.
- Generates separate sheets/sections for just IP addresses and for domains with their resolved IPs.

## Requirements

- Python 3.x
- `xlsxwriter` library (for Excel output) or standard `csv` module (for CSV output)
- `dig` command-line tool (should be installed by default on Kali Linux)

## Installation

1. **Install Python**: Make sure you have Python 3 installed. You can check by running:

   ```bash
   python3 --version
