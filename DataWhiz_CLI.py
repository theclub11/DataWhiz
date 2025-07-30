import os
import sys
import subprocess
import importlib.util
import signal
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import ANSI
import time
import random
import fake_useragent
import re

init(autoreset=True)

# 🔐 API endpoint removed to prevent abuse or scraping.
# 📬 Reach out on X (formerly Twitter): @AnonKryptiQuz for access or download the precompiled binary to bypass API restrictions.

_cr_u = API_ENDPOINT = "REDACTED_FOR_PUBLIC_RELEASE_CONTACT_X_@AnonKryptiQuz"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_package_installed(package):
    try:
        importlib.import_module(package)
        return True
    except ImportError:
        return False

def install_package(package):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        print(f"{Fore.GREEN}[+] {package} installed successfully.")
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}[!] Failed to install {package}.")

def check_and_install_packages(packages):
    for package in packages:
        if is_package_installed(package):
            print(f"{Fore.GREEN}[+] {package} is already installed.")
        else:
            print(f"{Fore.RED}[!] {package} is missing. Installing...")
            install_package(package)

def get_random_headers():
    user_agent = fake_useragent.UserAgent()
    user_agent_str = user_agent.random
    timezones = [
        'GMT', 'UTC', 'Europe/London', 'Asia/Kolkata', 'America/New_York',
        'Asia/Tokyo', 'America/Los_Angeles', 'Europe/Paris', 'Australia/Sydney'
    ]
    timezone = random.choice(timezones)
    languages = [
        'en-US,en;q=0.9', 'en-GB,en;q=0.8', 'fr-FR,fr;q=0.9', 'de-DE,de;q=0.9', 'es-ES,es;q=0.9'
    ]
    language = random.choice(languages)
    headers = {
        'User-Agent': user_agent_str,
        'Accept-Language': language,
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Timezone': timezone,
    }
    return headers

def create_session():
    session = requests.Session()
    session.headers.update(get_random_headers())
    return session

def fetch_and_parse_page(phone_number, session):
    url = _cr_u
    data = {'cnnum': phone_number}
    print(f"{Fore.MAGENTA}[?] Fetching data for phone number: {Fore.WHITE}{phone_number}{Style.RESET_ALL}\n")
    time.sleep(random.uniform(1, 3))
    try:
        response = session.post(url, data=data)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return extract_records_details(soup, session)
        else:
            print(f"{Fore.RED}[!] Error fetching data. Status Code: {response.status_code}{Style.RESET_ALL}")
    except requests.exceptions.MissingSchema:
        print(f"{Fore.CYAN}[!] API endpoint removed to prevent abuse or scraping.{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[i] Reach out on X (formerly Twitter): @AnonKryptiQuz for access or download the precompiled binary to bypass API restrictions.{Style.RESET_ALL}")
    except requests.exceptions.RequestException as e:
        if "Network is unreachable" in str(e):
            print(f"{Fore.RED}[!] The server cannot be reached. Please check your connection or try again later.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[!] An error occurred while making the request: {e}{Style.RESET_ALL}")

def extract_records_details(soup, session):
    records_found_section = soup.find(string=lambda text: text and "Records Found:" in text)
    if records_found_section:
        number_span = records_found_section.find_next('span', style="color:#FF0000;")
        if number_span:
            records_count = number_span.get_text(strip=True)
            print(f"{Fore.CYAN}[i] Total Records Found:{Style.RESET_ALL} {Fore.WHITE}{records_count}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[!] Number not found in the expected span.{Style.RESET_ALL}")
        time.sleep(2)

    last_values = {'MobileNo': None, 'Name': None, 'CNIC': None, 'Address': None, 'Operator': None}
    rows = soup.find_all('tr')
    found_data = False
    record_count = 1
    result_str = ""
    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 2:
            label = cells[0].get_text(strip=True)
            value = cells[1].get_text(strip=True)
            if label in ['MobileNo', 'Name', 'CNIC', 'Address', 'Operator']:
                if label == 'CNIC' and "(search)" in value:
                    value = value.split('(')[0].strip()
                if not value:
                    value = last_values[label]
                if label == 'MobileNo':
                    if not value.startswith('0'):
                        value = '0' + value
                    label = 'Mobile Number'
                    result_str += f"\n{Fore.YELLOW}[i] Record {record_count}:{Style.RESET_ALL}\n"
                    result_str += f"{Fore.GREEN}{label}:{Style.RESET_ALL} {Fore.WHITE}{value}{Style.RESET_ALL}\n"
                    record_count += 1
                else:
                    result_str += f"{Fore.GREEN}{label}:{Style.RESET_ALL} {Fore.WHITE}{value}{Style.RESET_ALL}\n"
                last_values[label] = value
                found_data = True
    if not found_data:
        print(f"{Fore.RED}[!] No relevant data found for the given phone number/CNIC.{Style.RESET_ALL}")
        sys.exit(0)
    print(result_str)
    save_prompt = prompt(ANSI(f"{Fore.YELLOW}[?] Do you want to save the results to a file? (y/n, press Enter for n): ")).strip().lower()
    if save_prompt in ['y', 'yes']:
        save_results_to_file(result_str)
    else:
        print(f"{Fore.RED}[i] Results will not be saved.{Style.RESET_ALL}")
    return result_str

def remove_ansi_escape_codes(text):
    ansi_escape = re.compile(r'\x1b\[([0-9;]+)m')
    return ansi_escape.sub('', text)

def save_results_to_file(result_str):
    cleaned_result = remove_ansi_escape_codes(result_str)
    filename = "phone_number_results.txt"
    try:
        with open(filename, 'w') as file:
            file.write(cleaned_result)
        print(f"{Fore.GREEN}[+] Results saved to {filename}{Style.RESET_ALL}")
    except IOError as e:
        print(f"{Fore.RED}[!] Error saving results to file: {e}{Style.RESET_ALL}")

def handle_interrupt(signal, frame):
    print(f"\n{Fore.RED}[!] Program interrupted. Exiting...")
    sys.exit(0)

def Banner():
    raw_created_by_text = "AnonKryptiQuz • coffinxp • Hghost010 • 1hehaq • NahoXSS • Nuknov • PaKnonymous"
    max_width = len(raw_created_by_text)

    ascii_lines = [
        rf" {Fore.GREEN} _____        _     {Fore.RED}__          ___     _      ",
        rf" {Fore.GREEN}|  __ \      | |    {Fore.RED}\ \        / / |   (_)     ",
        rf" {Fore.GREEN}| |  | | __ _| |_ __ {Fore.RED}\ \  /\  / /| |__  _ ____ ",
        rf" {Fore.GREEN}| |  | |/ _` | __/ _` {Fore.RED}\ \/  \/ / | '_ \| |_  / ",
        rf" {Fore.GREEN}| |__| | (_| | || (_| |{Fore.RED}\  /\  /  | | | | |/ /  ",
        rf" {Fore.GREEN}|_____/ \__,_|\__\__,_| {Fore.RED}\/  \/   |_| |_|_/___| ",
        rf"                                                "
    ]

    for line in ascii_lines:
        padding = (max_width - len(line)) // 2
        print(" " * padding + f"{Fore.GREEN}{line}{Style.RESET_ALL}")
    
    colored_created_by_text = f"{Fore.MAGENTA}AnonKryptiQuz {Fore.CYAN}• {Fore.MAGENTA}coffinxp {Fore.CYAN}• {Fore.MAGENTA}Hghost010 {Fore.CYAN}• {Fore.MAGENTA}1hehaq {Fore.CYAN}• {Fore.MAGENTA}NahoXSS {Fore.CYAN}• {Fore.MAGENTA}Nuknov {Fore.CYAN}• {Fore.MAGENTA}PaKnonymous"
    print(f"{Fore.RED}{colored_created_by_text}{Style.RESET_ALL}") 
    print("")

def main():
    signal.signal(signal.SIGINT, handle_interrupt)
    clear_screen()
    print(f"{Fore.YELLOW}[i] Checking for required packages...\n")
    required_packages = ["requests", "prompt_toolkit", "colorama", "fake_useragent"]
    check_and_install_packages(required_packages)
    time.sleep(2)
    clear_screen()
    Banner()
    while True:
        phone_number = prompt(ANSI(f"{Fore.WHITE}[?] Please enter a valid phone number or CNIC (numbers only, or +92…): "))
        phone_number = re.sub(r"[\s-]+", "", phone_number)
        if phone_number.isdigit() or phone_number.startswith("+92"):
            break
        else:
            print(f"{Fore.RED}[!] Invalid input. Please enter only digits for the phone number.{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}[?] Press Enter to try again...{Style.RESET_ALL}")
            input()
            clear_screen()
            Banner()
    if phone_number.startswith("+92"):
        phone_number = "0" + phone_number[3:]
    print(f"{Fore.YELLOW}\nLoading, please wait...{Style.RESET_ALL}")
    time.sleep(3)
    clear_screen()
    session = create_session()
    fetch_and_parse_page(phone_number, session)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{Fore.RED}\n[!] Operation interrupted. Exiting...")
