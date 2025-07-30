import os
import sys
import subprocess
import importlib.util
import signal
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
import time
import random
import fake_useragent
import re
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
from PIL import Image
import webbrowser
from io import BytesIO

init(autoreset=True)

# 🔐 API endpoint removed to prevent abuse or scraping.
# 📬 Reach out on X (formerly Twitter): @AnonKryptiQuz for access or download the precompiled binary to bypass API restrictions.

_cr_u = API_ENDPOINT = "REDACTED_FOR_PUBLIC_RELEASE_CONTACT_X_@AnonKryptiQuz"

def handle_interrupt(signum, frame):
    print(f"\n{Fore.RED}[!] Operation interrupted. Exiting...{Style.RESET_ALL}")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

PACKAGE_IMPORT_NAMES = {
    "beautifulsoup4": "bs4",
    "Pillow": "PIL",
    "requests": "requests",
    "fake_useragent": "fake_useragent",
    "customtkinter": "customtkinter"
}

REQUIRED_PACKAGES = ["requests", "beautifulsoup4", "fake_useragent", "customtkinter", "Pillow"]


def is_package_installed(package_name):
    import_name = PACKAGE_IMPORT_NAMES.get(package_name, package_name)
    try:
        importlib.import_module(import_name)
        return True
    except ImportError:
        return False

def install_package(package):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        return True
    except subprocess.CalledProcessError:
        return False

def check_and_install_packages(packages):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.YELLOW}[i] Checking for required packages...\n{Style.RESET_ALL}")
    time.sleep(1)

    for package in packages:
        if is_package_installed(package):
            print(f"{Fore.GREEN}[+] {package} is already installed.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[!] {package} is missing. Attempting to install...{Style.RESET_ALL}")
            if install_package(package):
                if is_package_installed(package):
                    print(f"{Fore.GREEN}[+] {package} installed successfully.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}[!] {package} was installed but could not be imported. Please check your Python environment.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[!] Failed to install {package}. Please install manually using 'pip install {package}' and restart the application.{Style.RESET_ALL}")
        time.sleep(0.5)
    
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

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

def _get_gui_banner_string():
    banner_str = ""
    banner_str += rf" ██████   █████  ████████  █████  ██     ██ ██   ██ ██ ███████ " + "\n"
    banner_str += rf" ██   ██ ██   ██    ██    ██   ██ ██     ██ ██   ██ ██    ███  " + "\n"
    banner_str += rf" ██   ██ ███████    ██    ███████ ██  █  ██ ███████ ██   ███   " + "\n"
    banner_str += rf" ██   ██ ██   ██    ██    ██   ██ ██ ███ ██ ██   ██ ██  ███    " + "\n"
    banner_str += rf" ██████  ██   ██    ██    ██   ██  ███ ███  ██   ██ ██ ███████ " + "\n"  
    return banner_str

def show_launch_animation(duration=2.5, message="Launching Application..."):
    animation_states = ["   ", ".  ", ".. ", "...", " ..", "  ."]
    start_time = time.time()
    
    sys.stdout.write(f"{Fore.CYAN}[i] {message} {Style.RESET_ALL}")
    sys.stdout.flush()

    idx = 0
    while time.time() - start_time < duration:
        sys.stdout.write(f"\b\b\b{animation_states[idx % len(animation_states)]}")
        sys.stdout.flush()
        time.sleep(0.15)
        idx += 1
        if time.time() - start_time >= duration:
            break
    
    sys.stdout.write("\b\b\b   \b\b\b")
    sys.stdout.write("\n")
    sys.stdout.flush()
    
    os.system('cls' if os.name == 'nt' else 'clear')

def run_continuous_terminal_animation(stop_event):
    Banner()
    animation_chars = ['|', '/', '-', '\\']
    message = f"{Fore.CYAN}[+] Application is running {Fore.MAGENTA}"
    idx = 0
    while not stop_event.is_set():
        sys.stdout.write(f"\r{message}{animation_chars[idx % len(animation_chars)]}")
        sys.stdout.flush()
        time.sleep(0.2)
        idx += 1
    
    sys.stdout.write(f"\r{' ' * (len(message) + 2)}\r")
    sys.stdout.flush()

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

def remove_ansi_escape_codes(text):
    ansi_escape = re.compile(r'\x1b\[([0-9;]+)m')
    return ansi_escape.sub('', text)

def extract_records_details(soup, session, update_callback, current_mode):
    result_str_with_ansi = ""

    query_type_term = current_mode.replace('mobile', 'phone number').replace('cnic', 'CNIC')

    records_found_section = soup.find(string=lambda text: text and "Records Found:" in text)
    if records_found_section:
        number_span = records_found_section.find_next('span', style="color:#FF0000;")
        if number_span:
            records_count = number_span.get_text(strip=True)
            update_callback(f"[i] Total Records Found: {records_count}\n", append=True, color="cyan")
            result_str_with_ansi += f"{Fore.CYAN}[i] Total Records Found:{Style.RESET_ALL} {Fore.WHITE}{records_count}{Style.RESET_ALL}\n"
        else:
            update_callback("[!] Number not found in the expected span.\n", append=True, color="red")
            result_str_with_ansi += f"{Fore.RED}[!] Number not found in the expected span.{Style.RESET_ALL}\n"
        time.sleep(0.5)

    last_values = {'MobileNo': None, 'Name': None, 'CNIC': None, 'Address': None, 'Operator': None}
    rows = soup.find_all('tr')
    found_data = False
    record_count = 1

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
                    display_label = 'Mobile Number'
                    ansi_label = 'Mobile Number'
                    
                    update_callback(f"\n[i] Record {record_count}:\n", append=True, color="yellow")
                    result_str_with_ansi += f"{Fore.YELLOW}[i] Record {record_count}:{Style.RESET_ALL}\n"

                    
                    update_callback(f"{display_label}: ", append=True, color="black_label")
                    update_callback(f"{value}\n", append=True, color="green")
                    result_str_with_ansi += f"{Fore.BLACK}{ansi_label}:{Style.RESET_ALL} {Fore.GREEN}{value}{Style.RESET_ALL}\n"
                    record_count += 1
                else:
                    
                    update_callback(f"{label}: ", append=True, color="black_label")
                    update_callback(f"{value}\n", append=True, color="green")
                    result_str_with_ansi += f"{Fore.BLACK}{label}:{Style.RESET_ALL} {Fore.GREEN}{value}{Style.RESET_ALL}\n"
                
                last_values[label] = value
                found_data = True

    if not found_data:
        update_callback(f"[!] No relevant data found for the given {query_type_term}.\n", append=True, color="red")
        result_str_with_ansi += f"{Fore.RED}[!] No relevant data found for the given {query_type_term}.{Style.RESET_ALL}\n"
    
    return result_str_with_ansi

def fetch_and_parse_page(query_value, session, update_callback, current_mode):
    url = _cr_u
    data = {'cnnum': query_value}

    
    update_callback(f"[?] Fetching data for: {query_value}\n\n", append=True, color="magenta")
    
    raw_output_buffer = f"{Fore.MAGENTA}[?] Fetching data for: {Fore.WHITE}{query_value}{Style.RESET_ALL}\n\n"

    time.sleep(random.uniform(0.5, 1.5))

    try:
        response = session.post(url, data=data)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            extracted_details_ansi = extract_records_details(soup, session, update_callback, current_mode)
            raw_output_buffer += extracted_details_ansi
            return raw_output_buffer
        else:
            update_callback(f"[!] Error fetching data. Status Code: {response.status_code}\n", append=True, color="red")
            raw_output_buffer += f"{Fore.RED}[!] Error fetching data. Status Code: {response.status_code}{Style.RESET_ALL}\n"
            return raw_output_buffer
    except requests.exceptions.MissingSchema:
        update_callback(f"[!] API endpoint removed to prevent abuse or scraping.\n", append=True, color="cyan")
        update_callback(f"[i] Reach out on X (formerly Twitter): @AnonKryptiQuz for access.\n", append=True, color="cyan")
        raw_output_buffer += f"{Fore.CYAN}[!] API endpoint removed to prevent abuse or scraping.{Style.RESET_ALL}\n"
        raw_output_buffer += f"{Fore.CYAN}[i] Reach out on X (formerly Twitter): @AnonKryptiQuz for access or download the precompiled binary to bypass API restrictions.{Style.RESET_ALL}\n"

        return raw_output_buffer
    except requests.exceptions.RequestException as e:
        error_message = str(e)
        if "Network is unreachable" in error_message:
            update_callback(f"[!] The server cannot be reached. Please check your connection or try again later.\n", append=True, color="red")
            raw_output_buffer += f"{Fore.RED}[!] The server cannot be reached. Please check your connection or try again later.{Style.RESET_ALL}\n"
            return raw_output_buffer
        elif "Connection reset by peer" in error_message:
            update_callback(f"[!] Connection was reset by the server. Try again later or consider using a VPN.\n", append=True, color="red")
            raw_output_buffer += f"{Fore.RED}[!] Connection was reset by the server. Try again later or consider using a VPN.{Style.RESET_ALL}\n"
            return raw_output_buffer
        else:
            update_callback(f"[!] An error occurred while making the request: {e}\n", append=True, color="red")
            raw_output_buffer += f"{Fore.RED}[!] An error occurred while making the request: {e}{Style.RESET_ALL}\n"
            return raw_output_buffer

class PhoneNumberLookupApp(ctk.CTk):
    def __init__(self, stop_animation_event):
        super().__init__()
        self.stop_animation_event = stop_animation_event

        self.title("DataWhiz Lookup Tool")
        self.geometry("800x700")
        self.minsize(600, 600)
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.configure(fg_color="#D0D0C8") 

        self.current_results_text = ""
        self.current_mode = None
        self.last_mode_selected = None
        self.status_label = None

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.create_mode_selection_screen()

    def on_closing(self):
        self.stop_animation_event.set()
        self.destroy()

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

    def _open_creator_link(self, event=None):
        webbrowser.open_new("https://AnonKryptiQuz.github.io")

    def _open_pta_link(self, event=None):
        webbrowser.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    def _create_common_header_widgets(self):
        top_banner_frame = ctk.CTkFrame(self, fg_color="#C0C0B8", corner_radius=8)
        top_banner_frame.grid_columnconfigure(0, weight=1) 
        top_banner_frame.grid_rowconfigure(0, weight=1) 
        top_banner_frame.grid_rowconfigure(1, weight=0) 
        top_banner_frame.grid_rowconfigure(2, weight=1) 

        con_color="#B0B0A8"
        banner_and_credits_frame = ctk.CTkFrame(top_banner_frame, fg_color=con_color, corner_radius=8,
                                                border_width=1, border_color="#555555") 
        banner_and_credits_frame.grid(row=1, column=0, pady=15, padx=15, sticky="nsew") 

        banner_and_credits_frame.grid_columnconfigure(0, weight=1)
        banner_and_credits_frame.grid_rowconfigure(0, weight=0)
        banner_and_credits_frame.grid_rowconfigure(1, weight=0)

        self.banner_label = ctk.CTkLabel(banner_and_credits_frame, text=_get_gui_banner_string(),
                                         font=ctk.CTkFont(family="Consolas", size=14, weight="bold"),
                                         text_color="#005F7F",
                                         fg_color=con_color) 
        self.banner_label.grid(row=0, column=0, pady=(15, 0), padx=15, sticky="n")

        credits_inner_frame = ctk.CTkFrame(banner_and_credits_frame, fg_color=con_color)
        credits_inner_frame.grid(row=1, column=0, pady=(0, 15), padx=15, sticky="n")
        
        parts = [
            ("AnonKryptiQuz", "#A00000"),
            (" • ", "#005F7F"),
            ("coffinxp", "#A00000"),
            (" • ", "#005F7F"),
            ("Hghost010", "#A00000"),
            (" • ", "#005F7F"),
            ("1hehaq", "#A00000"),
            (" • ", "#005F7F"),
            ("NahoXSS", "#A00000"),
            (" • ", "#005F7F"),
            ("Nuknov", "#A00000"),
            (" • ", "#005F7F"),
            ("PaKnonymous", "#A00000")
        ]
        
        current_column = 0
        for text, color in parts:
            label_part = ctk.CTkLabel(credits_inner_frame, text=text,
                                      font=ctk.CTkFont(size=12, weight="bold"),
                                      text_color=color,
                                      fg_color=con_color)
            label_part.grid(row=0, column=current_column, sticky="w")
            credits_inner_frame.grid_columnconfigure(current_column, weight=0)
            current_column += 1
        
        credits_inner_frame.grid_columnconfigure(current_column -1, weight=1)
        
        return top_banner_frame

    def _handle_main_menu_keypress(self, event):
        is_control_pressed = (event.state & 0x0004)
        is_alt_pressed = (event.state & 0x0008)

        if event.keysym == "Escape":
            self.on_closing()
            return "break"

        if event.keysym == "Left" and is_control_pressed:
            self.show_dashboard("mobile")
            return "break"

        if event.keysym == "Right" and is_control_pressed:
            self.show_dashboard("cnic")
            return "break"

        if event.keysym == "Right" and is_alt_pressed:
            if self.last_mode_selected:
                self.show_dashboard(self.last_mode_selected)
            return "break"

        return None
        
    def create_mode_selection_screen(self):
        self.clear_widgets()

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=0)
        self.grid_columnconfigure(0, weight=1)

        nav_frame = ctk.CTkFrame(self, fg_color="#C0C0B8", corner_radius=8, border_width=0)
        nav_frame.grid(row=0, column=0, pady=(10, 0), padx=20, sticky="ew") 
        nav_frame.grid_columnconfigure(0, weight=0) 
        nav_frame.grid_columnconfigure(1, weight=1) 
        nav_frame.grid_columnconfigure(2, weight=0)

        about_button = ctk.CTkButton(nav_frame, text="About", command=self._open_creator_link, 
                                     width=150, height=30,
                                     font=ctk.CTkFont(size=13, weight="bold"),
                                     fg_color="#B0B0A8", hover_color="#909088", 
                                     text_color="#2B2B2B",
                                     corner_radius=8, border_width=1, border_color="#808078") 
        about_button.grid(row=0, column=0, padx=10, pady=10, sticky="w") 

        exit_button = ctk.CTkButton(nav_frame, text="Exit", command=self.on_closing,
                                    width=150, height=30,
                                    font=ctk.CTkFont(size=13, weight="bold"),
                                    fg_color="#B0B0A8", hover_color="#909088", 
                                    text_color="#2B2B2B",
                                    corner_radius=8, border_width=1, border_color="#808078") 
        exit_button.grid(row=0, column=2, padx=10, pady=10, sticky="e") 

        header_frame = self._create_common_header_widgets()
        header_frame.grid(row=1, column=0, pady=(10, 0), padx=20, sticky="nsew")

        mode_buttons_container = ctk.CTkFrame(self, fg_color="#C0C0B8", corner_radius=8, border_width=0)
        mode_buttons_container.grid(row=2, column=0, sticky="nsew", padx=20, pady=(10, 10)) 
        
        mode_buttons_container.grid_rowconfigure(0, weight=0)
        mode_buttons_container.grid_rowconfigure(1, weight=0)
        mode_buttons_container.grid_rowconfigure(2, weight=1)
        
        mode_buttons_container.grid_columnconfigure(0, weight=1)
        mode_buttons_container.grid_columnconfigure(1, weight=0)
        mode_buttons_container.grid_columnconfigure(2, weight=0)
        mode_buttons_container.grid_columnconfigure(3, weight=1)

        welcome_label = ctk.CTkLabel(mode_buttons_container, text="Welcome! Select Your Lookup Service:",
                                     font=ctk.CTkFont(size=24, weight="bold"),
                                     text_color="#005F7F")
        
        welcome_label.grid(row=0, column=1, columnspan=2, pady=(30, 10), sticky="s") 

        mobile_mode_box = ctk.CTkFrame(mode_buttons_container, fg_color="#B0B0A8", corner_radius=15, border_width=2, border_color="#007BFF")
        
        mobile_mode_box.grid(row=1, column=1, padx=20, pady=(20, 20), sticky="nsew")
        mobile_mode_box.grid_rowconfigure(0, weight=0)
        mobile_mode_box.grid_rowconfigure(1, weight=0)
        mobile_mode_box.grid_rowconfigure(2, weight=0)
        mobile_mode_box.grid_rowconfigure(3, weight=1)
        mobile_mode_box.grid_rowconfigure(4, weight=0)
        mobile_mode_box.grid_columnconfigure(0, weight=1)

        mobile_title = ctk.CTkLabel(mobile_mode_box, text="Mobile Number Lookup",
                                    font=ctk.CTkFont(size=18, weight="bold"), text_color="#2B2B2B")
        mobile_title.grid(row=0, column=0, pady=(20, 5), padx=20, sticky="n")

        mobile_main_description = ctk.CTkLabel(mobile_mode_box,
                                               text="Search for details using a mobile phone number.",
                                               font=ctk.CTkFont(size=14),
                                               text_color="#444444",
                                               wraplength=250, justify="center")
        mobile_main_description.grid(row=1, column=0, pady=(5, 5), padx=20, sticky="nsew")

        mobile_formats_description = ctk.CTkLabel(mobile_mode_box,
                                                  text="Accepted formats:\n"
                                                       "  • 03xxxxxxxxx\n"
                                                       "  • +92xxxxxxxxx",
                                                  font=ctk.CTkFont(size=11),
                                                  text_color="#666666",
                                                  wraplength=250, justify="center")
        mobile_formats_description.grid(row=2, column=0, pady=(5, 10), padx=20, sticky="nsew")

        mobile_button = ctk.CTkButton(mobile_mode_box, text="Look up Mobile Number",
                                      command=lambda: self.show_dashboard("mobile"),
                                      width=250, height=50,
                                      font=ctk.CTkFont(size=16, weight="bold"),
                                      fg_color="#007BFF", hover_color="#0069D9",
                                      corner_radius=10)
        mobile_button.grid(row=4, column=0, pady=(10, 10), padx=20) 

        cnic_mode_box = ctk.CTkFrame(mode_buttons_container, fg_color="#B0B0A8", corner_radius=15, border_width=2, border_color="#4CAF50")
        cnic_mode_box.grid(row=1, column=2, padx=20, pady=(20, 20), sticky="nsew")
        cnic_mode_box.grid_rowconfigure(0, weight=0)
        cnic_mode_box.grid_rowconfigure(1, weight=0)
        cnic_mode_box.grid_rowconfigure(2, weight=0)
        cnic_mode_box.grid_rowconfigure(3, weight=1)
        cnic_mode_box.grid_rowconfigure(4, weight=0)
        cnic_mode_box.grid_columnconfigure(0, weight=1)

        cnic_title = ctk.CTkLabel(cnic_mode_box, text="CNIC Lookup",
                                  font=ctk.CTkFont(size=18, weight="bold"), text_color="#2B2B2B")
        cnic_title.grid(row=0, column=0, pady=(20, 5), padx=20, sticky="n")

        cnic_main_description = ctk.CTkLabel(cnic_mode_box,
                                             text="Search for details using a CNIC (National Identity Card) number.",
                                             font=ctk.CTkFont(size=14),
                                             text_color="#444444",
                                             wraplength=250, justify="center")
        cnic_main_description.grid(row=1, column=0, pady=(5, 5), padx=20, sticky="nsew")

        cnic_formats_description = ctk.CTkLabel(cnic_mode_box,
                                                text="Accepted formats:\n"
                                                     "  • XXXXXXXXXXXXX\n"
                                                     "  • XXXXX-XXXXXXX-X",
                                                  font=ctk.CTkFont(size=11),
                                                  text_color="#666666",
                                                  wraplength=250, justify="center")
        cnic_formats_description.grid(row=2, column=0, pady=(5, 10), padx=20, sticky="nsew")

        cnic_button = ctk.CTkButton(cnic_mode_box, text="Look up CNIC",
                                    command=lambda: self.show_dashboard("cnic"),
                                    width=250, height=50,
                                    font=ctk.CTkFont(size=16, weight="bold"),
                                    fg_color="#4CAF50", hover_color="#45A049",
                                    corner_radius=10)
        cnic_button.grid(row=4, column=0, pady=(10, 10), padx=20) 

        powered_by_footer_frame = ctk.CTkFrame(self, fg_color="#C0C0B8")
        
        powered_by_footer_frame.grid(row=3, column=0, pady=(0, 10), padx=20, sticky="ew") 
        powered_by_footer_frame.grid_columnconfigure(0, weight=1)

        powered_by_footer_label = ctk.CTkLabel(powered_by_footer_frame,
                                               text="Powered by the Digital Unseen.",
                                               font=ctk.CTkFont(size=12, slant="italic"),
                                               text_color="#005F7F")
        powered_by_footer_label.grid(row=0, column=0, pady=5, padx=10, sticky="ew")
        powered_by_footer_label.bind("<Button-1>", self._open_pta_link) 

        self.bind("<KeyPress>", self._handle_main_menu_keypress)
        self.bind("<Control-i>", lambda event: (self._open_creator_link(), "break")) 

        
        self.unbind("<Control-s>")
        self.unbind("<Control-l>")
        self.unbind("<Alt-Left>")
        self.unbind("<Control-Shift-C>") 
        
        self.focus_force()

    def show_dashboard(self, mode):
        self.current_mode = mode
        self.clear_widgets()

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=1) 
        self.grid_rowconfigure(4, weight=0)
        self.grid_rowconfigure(5, weight=0)
        self.grid_columnconfigure(0, weight=1)

        self_title_text = ""
        placeholder_text = ""

        if mode == "mobile":
            self_title_text = "DataWhiz - Mobile Number Lookup"
            placeholder_text = "Enter phone number (e.g., 03xxxxxxxxx or +92xxxxxxxxx)"
        elif mode == "cnic":
            self_title_text = "DataWhiz - CNIC Lookup"
            placeholder_text = "Enter CNIC (e.g., XXXXXXXXXXXXX or XXXXX-XXXXXXX-X)"
        
        self.title(self_title_text)

        self.create_dashboard_widgets(placeholder_text)

        
        self.unbind("<KeyPress>")
        self.unbind("<Control-i>")

        self.bind("<Escape>", lambda event: (self.on_closing(), "break"))
        self.bind("<Control-s>", lambda event: (self.save_results_to_file(), "break"))
        self.bind("<Control-l>", lambda event: (self.clear_all_fields(), "break"))
        self.bind("<Alt-Left>", lambda event: (self.go_back_to_mode_selection(), "break"))
        
        self.bind("<Control-Shift-C>", lambda event: (self.copy_all_results(), "break"))
        
        self.focus_force()


    def _copy_selected_text(self, event):
        try:
            selected_text = event.widget.selection_get()
            self.clipboard_clear()
            self.clipboard_append(selected_text)
        except tk.TclError:
            pass
        return "break"

    def _cut_selected_text(self, event):
        try:
            selected_text = event.widget.selection_get()
            self.clipboard_clear()
            self.clipboard_append(selected_text)
            event.widget.delete(tk.SEL_FIRST, tk.SEL_LAST)
        except tk.TclError:
            pass
        return "break"

    def _paste_text(self, event):
        try:
            clipboard_content = self.clipboard_get()
            if event.widget.selection_present():
                event.widget.delete(tk.SEL_FIRST, tk.SEL_LAST)
            event.widget.insert(tk.INSERT, clipboard_content)
        except tk.TclError:
            pass
        return "break"
    def _select_all_text(self, event):
        event.widget.select_range(0, 'end')
        event.widget.icursor('end')
        return "break"

    def copy_all_results(self):
        if not self.current_results_text:
            messagebox.showinfo("Copy Results", "No results to copy.")
            return

        try:
            self.clipboard_clear()
            self.clipboard_append(self.current_results_text)
            messagebox.showinfo("Copy Results", "All results copied to clipboard!")
            self.update_status("Results copied to clipboard.", "green")
        except tk.TclError as e:
            messagebox.showerror("Copy Error", f"Failed to copy results to clipboard: {e}")
            self.update_status("Error copying results.", "red")

    def create_dashboard_widgets(self, placeholder_text):
        nav_frame = ctk.CTkFrame(self, fg_color="#C0C0B8", corner_radius=8, border_width=0)
        nav_frame.grid(row=0, column=0, pady=(10, 0), padx=20, sticky="ew") 
        nav_frame.grid_columnconfigure(0, weight=0)
        nav_frame.grid_columnconfigure(1, weight=1) 
        nav_frame.grid_columnconfigure(2, weight=0)

        back_button = ctk.CTkButton(nav_frame, text="< Back to Menu", command=self.go_back_to_mode_selection,
                                    width=150, height=30,
                                    font=ctk.CTkFont(size=13, weight="bold"),
                                    fg_color="#B0B0A8", hover_color="#909088", 
                                    text_color="#2B2B2B",
                                    corner_radius=8, border_width=1, border_color="#808078") 
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        exit_button = ctk.CTkButton(nav_frame, text="Exit", command=self.on_closing,
                                    width=150, height=30,
                                    font=ctk.CTkFont(size=13, weight="bold"),
                                    fg_color="#B0B0A8", hover_color="#909088", 
                                    text_color="#2B2B2B",
                                    corner_radius=8, border_width=1, border_color="#808078") 
        exit_button.grid(row=0, column=2, padx=10, pady=10, sticky="e") 

        header_frame = self._create_common_header_widgets()
        header_frame.grid(row=1, column=0, pady=(10, 0), padx=20, sticky="nsew")

        input_frame = ctk.CTkFrame(self, fg_color="#C0C0B8")
        input_frame.grid(row=2, column=0, pady=(10, 0), padx=20, sticky="ew")
        input_frame.grid_columnconfigure(0, weight=1)
        input_frame.grid_columnconfigure(1, weight=0)

        self.phone_number_entry = ctk.CTkEntry(input_frame, placeholder_text=placeholder_text,
                                               width=400, height=40,
                                               font=ctk.CTkFont(size=14),
                                               fg_color="#C0C0B8",
                                               text_color="#2B2B2B",
                                               placeholder_text_color="#666666",
                                               border_color="#808078", border_width=1)
        self.phone_number_entry.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="ew")
        self.phone_number_entry.bind("<Return>", self.start_lookup_thread)

        self.phone_number_entry._entry.config(
            selectbackground="#000080",
            selectforeground="white"
        )

        self.phone_number_entry.bind("<Control-c>", self._copy_selected_text)
        self.phone_number_entry.bind("<Control-x>", self._cut_selected_text)
        self.phone_number_entry.bind("<Control-v>", self._paste_text)
        self.phone_number_entry.bind("<Control-a>", self._select_all_text)

        self.search_button = ctk.CTkButton(input_frame, text="Search", command=self.start_lookup_thread,
                                           width=120, height=40,
                                           font=ctk.CTkFont(size=14, weight="bold"),
                                           fg_color="#4CAF50", hover_color="#45A049",
                                           corner_radius=8)
        self.search_button.grid(row=0, column=1, padx=(5, 10), pady=10, sticky="e")

        output_container_frame = ctk.CTkFrame(self, fg_color="#C0C0B8",
                                              border_color="#555555", border_width=1,
                                              corner_radius=8)
        output_container_frame.grid(row=3, column=0, pady=(10, 10), padx=20, sticky="nsew")
        output_container_frame.grid_rowconfigure(0, weight=1)
        output_container_frame.grid_columnconfigure(0, weight=1)
        output_container_frame.grid_columnconfigure(1, weight=0) 

        self.output_textbox = ctk.CTkTextbox(output_container_frame, wrap="word", activate_scrollbars=True,
                                             font=ctk.CTkFont(family="Consolas", size=12),
                                             text_color="#2B2B2B",
                                             fg_color="#C0C0B8",
                                             border_width=0)
        self.output_textbox.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.output_textbox.insert("end", f"Welcome to DataWhiz Lookup Tool ({self.current_mode.replace('mobile', 'Mobile Number').replace('cnic', 'CNIC')} Mode)!\n\n")
        self.output_textbox.insert("end", f"{placeholder_text}\n", "info")
        self.output_textbox.configure(state="disabled")

        self.output_textbox._textbox.config(
            selectbackground="#000080",
            selectforeground="white"
        )

        self.output_textbox.tag_config("red", foreground="#CC0000")
        self.output_textbox.tag_config("green", foreground="#008000")
        self.output_textbox.tag_config("yellow", foreground="#CC8000")
        self.output_textbox.tag_config("cyan", foreground="#008080")
        self.output_textbox.tag_config("magenta", foreground="#800080")
        self.output_textbox.tag_config("white", foreground="#2B2B2B")
        self.output_textbox.tag_config("info", foreground="#444444")
        self.output_textbox.tag_config("black_label", foreground="#000000")

        self.copy_all_button = ctk.CTkButton(output_container_frame, text="Copy All", command=self.copy_all_results,
                                             width=60, height=20,
                                             font=ctk.CTkFont(size=9, weight="bold"),
                                             fg_color="#6A5ACD", hover_color="#5B4F9B",
                                             text_color="white",
                                             corner_radius=8)
        self.copy_all_button.grid(row=0, column=1, padx=10, pady=10, sticky="se")

        buttons_frame = ctk.CTkFrame(self, fg_color="#C0C0B8")
        buttons_frame.grid(row=4, column=0, pady=(0, 0), padx=20, sticky="ew") 
        
        buttons_frame.grid_columnconfigure(0, weight=0)
        buttons_frame.grid_columnconfigure(1, weight=1)
        buttons_frame.grid_columnconfigure(2, weight=0)
        
        buttons_frame.grid_rowconfigure(0, weight=1)

        self.save_button = ctk.CTkButton(buttons_frame, text="Save Results", command=self.save_results_to_file,
                                         width=150, height=40,
                                         font=ctk.CTkFont(size=14, weight="bold"),
                                         fg_color="#007BFF", hover_color="#0069D9",
                                         corner_radius=8)
        self.save_button.grid(row=0, column=0, padx=(60, 5), pady=10, sticky="w")

        self.clear_button = ctk.CTkButton(buttons_frame, text="Clear", command=self.clear_all_fields,
                                          width=150, height=40,
                                          font=ctk.CTkFont(size=14, weight="bold"),
                                          fg_color="#FF4500", hover_color="#CC3700",
                                          corner_radius=8)
        self.clear_button.grid(row=0, column=2, padx=(5, 60), pady=10, sticky="e")

        powered_by_label = ctk.CTkLabel(buttons_frame,
                                        text="Powered by the Digital Unseen.",
                                        font=ctk.CTkFont(size=10, slant="italic"),
                                        text_color="#005F7F")
        powered_by_label.grid(row=0, column=1, padx=30, pady=10, sticky="nsew")
        powered_by_label.bind("<Button-1>", self._open_pta_link) 

        self.save_button.configure(state="disabled")
        self.copy_all_button.configure(state="disabled")

        status_frame = ctk.CTkFrame(self, fg_color="#C0C0B8") 
        status_frame.grid(row=5, column=0, pady=(10, 10), padx=20, sticky="ew")
        status_frame.grid_columnconfigure(0, weight=1) 

        self.status_label = ctk.CTkLabel(status_frame, text="Ready.",
                                         font=ctk.CTkFont(size=12),
                                         text_color="#555555")
        self.status_label.grid(row=0, column=0, pady=5, padx=10, sticky="ew") 
        
    def go_back_to_mode_selection(self):
        if self.current_mode:
            self.last_mode_selected = self.current_mode

        self.clear_widgets()
        self.current_mode = None
        self.current_results_text = ""
        self.title("DataWhiz Lookup Tool")
        self.create_mode_selection_screen()
    def update_output(self, message, append=True, color="white"):
        self.output_textbox.configure(state="normal")
        if not append:
            self.output_textbox.delete("1.0", "end")
        self.output_textbox.insert("end", message, color)
        self.output_textbox.see("end")
        self.output_textbox.configure(state="disabled")

    def update_status(self, message, color="#555555"):
        if self.status_label and self.status_label.winfo_exists():
            self.status_label.configure(text=message, text_color=color)

    def start_lookup_thread(self, event=None):
        query_value = self.phone_number_entry.get().strip()
        query_value = re.sub(r"[\s-]+", "", query_value)

        if self.current_mode == "mobile":
            if not query_value:
                messagebox.showwarning("Input Error", "Please enter a phone number.")
                self.update_status("Input required.", "red")
                return
            if not (query_value.isdigit() and len(query_value) >= 10) and not query_value.startswith("+92"):
                messagebox.showwarning("Input Error", "Invalid phone number format. Please enter only digits (e.g., 03xxxxxxxxx) or a valid +92 number (e.g., +923xxxxxxxxx).")
                self.update_status("Invalid input format.", "red")
                return
            if query_value.startswith("+92"):
                query_value = "0" + query_value[3:]
        elif self.current_mode == "cnic":
            if not query_value:
                messagebox.showwarning("Input Error", "Please enter a CNIC.")
                self.update_status("Input required.", "red")
                return
            if not query_value.isdigit() or len(query_value) != 13:
                messagebox.showwarning("Input Error", "Invalid CNIC format. Please enter a 13-digit CNIC (e.g., XXXXXXXXXXXXX).")
                self.update_status("Invalid input format.", "red")
                return

        self.update_output("", append=False)
        self.update_output("Initiating search for data...\n", append=True, color="info")
        self.update_status("Loading, please wait...", "#CC8000")
        
        self.search_button.configure(state="disabled")
        self.save_button.configure(state="disabled")
        self.phone_number_entry.configure(state="disabled")
        self.clear_button.configure(state="disabled")
        self.copy_all_button.configure(state="disabled")

        lookup_thread = threading.Thread(target=self._perform_lookup, args=(query_value,))
        lookup_thread.daemon = True
        lookup_thread.start()

    def _perform_lookup(self, query_value):
        session = create_session()
        
        raw_results_with_ansi = fetch_and_parse_page(query_value, session,
                                                     lambda msg, append, color: self.after(0, self.update_output, msg, append, color),
                                                     self.current_mode)

        self.current_results_text = remove_ansi_escape_codes(raw_results_with_ansi)

        self.after(0, lambda: self.search_button.configure(state="normal"))
        self.after(0, lambda: self.phone_number_entry.configure(state="normal"))
        self.after(0, lambda: self.clear_button.configure(state="normal"))
        
        if self.current_results_text and "No relevant data found" not in self.current_results_text:
             self.after(0, lambda: self.save_button.configure(state="normal"))
             self.after(0, lambda: self.copy_all_button.configure(state="normal"))
        else:
             self.after(0, lambda: self.save_button.configure(state="disabled"))
             self.after(0, lambda: self.copy_all_button.configure(state="disabled"))

        self.after(0, self.update_status, "Search complete.", "green")

    def save_results_to_file(self):
        if not self.current_results_text:
            messagebox.showinfo("Save Results", "No results to save.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            title="Save Results As",
            initialfile="DataWhiz.txt"
        )
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(self.current_results_text)
                messagebox.showinfo("Save Results", f"Results saved successfully to {os.path.basename(file_path)}")
                self.update_status(f"Results saved to {os.path.basename(file_path)}", "green")
            except IOError as e:
                messagebox.showerror("Save Error", f"Error saving results to file: {e}")
                self.update_status("Error saving results.", "red")
        else:
            self.update_status("Save operation cancelled.", "#CC8000")

    def clear_all_fields(self):
        if hasattr(self, 'phone_number_entry') and self.phone_number_entry.winfo_exists():
            self.phone_number_entry.delete(0, "end")
        
        self.update_output("", append=False)
        self.current_results_text = ""
        
        if hasattr(self, 'save_button') and self.save_button.winfo_exists():
            self.save_button.configure(state="disabled")
        if hasattr(self, 'copy_all_button') and self.copy_all_button.winfo_exists():
            self.copy_all_button.configure(state="disabled")
        if hasattr(self, 'search_button') and self.search_button.winfo_exists():
            self.search_button.configure(state="normal")
        if hasattr(self, 'phone_number_entry') and self.phone_number_entry.winfo_exists():
            self.phone_number_entry.configure(state="normal")
        if hasattr(self, 'clear_button') and self.clear_button.winfo_exists():
            self.clear_button.configure(state="normal")

        self.update_status("Ready.") 
        
if __name__ == "__main__":
    check_and_install_packages(REQUIRED_PACKAGES)
    Banner()
    show_launch_animation(duration=2.5, message="Launching Application, please wait...")

    stop_animation_event = threading.Event()

    continuous_animation_thread = threading.Thread(
        target=run_continuous_terminal_animation,
        args=(stop_animation_event,),
        daemon=True
    )
    continuous_animation_thread.start()

    app = PhoneNumberLookupApp(stop_animation_event)
    app.mainloop()
    time.sleep(0.1)
