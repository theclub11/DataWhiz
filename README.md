# **DataWhiz: Pakistan Mobile/CNIC OSINT Tool**

**DataWhiz** is a Python-based application designed to retrieve information related to Pakistani mobile numbers and CNICs (Computerized National Identity Cards). It was developed in response to community requests for a tool focused on this region. The application offers both a Command Line Interface (CLI) and a Graphical User Interface (GUI), serving as an OSINT (Open Source Intelligence) utility for research and verification purposes.

## Table of Contents
- [Demo (POC)](#demo-poc)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Access Notice](#️-api-access-notice)
- [Build Your Own Binary](#build-your-own-precompiled-binary)
- [Community Notice](#community-notice)
- [Binary Integrity](#binary-integrity--scan-reports)
- [Disclaimer](#disclaimer)
- [Credits](#credits)
- [Author](#author)

## Demo (POC)

<video src="https://github.com/user-attachments/assets/eba49e0f-ddf1-4f35-a39d-9e9091f2aebb" controls width="100%"></video>

> **Note:** This is a short proof-of-concept demonstrating both the CLI and GUI modes of DataWhiz.

## **Features**

* **Dual Interface**: Provides both an interactive Command Line Interface (CLI) and a user-friendly Graphical User Interface (GUI).
* **Mobile Number Lookup**: Fetches details associated with Pakistani mobile numbers.
* **CNIC Lookup**: Retrieves information linked to Pakistani CNICs.
* **Results Saving**: Allows users to save lookup results to a text file.
* **Clipboard Integration (GUI)**: Enables quick copying of results to the clipboard.

## **Prerequisites**

> **For Precompiled Binaries:**

* Linux system with **GLIBC 2.38 or higher**. For issues related to missing GLIBC versions, see the [GLIBC Compatibility Guide](./GLIBC.md).

> **For Running from Source:**

* Python 3.x (3.10+ recommended)
* `requests` (For making internal data requests)
* `beautifulsoup4` (For data parsing)
* `fake_useragent` (For generating random user agents)
* `customtkinter` (GUI only)
* `Pillow` (Dependency of customtkinter, GUI only)
* `colorama` (Colored terminal output)
* `prompt_toolkit` (CLI only)

For **GUI version only** (Source and Binary), ensure `python3-tk` and `libxcb1` are installed [see GUI Prerequisites](#gui-prerequisites).

## **Installation**

### Option 1: Use Precompiled Binaries (No Setup Required)

Download the latest precompiled executables for CLI and GUI from the [Releases](https://github.com/AnonKryptiQuz/DataWhiz/releases) page.

> **Note:** The API endpoint is embedded in the precompiled binaries, so you don’t need to manually set it. This bypasses the API restrictions present in the source code version.

### Option 2: Run from Source

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AnonKryptiQuz/DataWhiz.git
   cd DataWhiz
   ```

2. **Install required Python packages:**

   ```bash
   pip install -r requirements.txt
   ```

   Ensure that `requirements.txt` contains the following:

   ```text
   requests
   beautifulsoup4
   fake_useragent
   customtkinter
   Pillow
   colorama
   prompt_toolkit
   ```

### CLI Prerequisites

1. **For Precompiled CLI Binary**
   No additional setup is required. The CLI binary is fully standalone and includes all necessary dependencies, including Python.

2. **For Running CLI from Source**
   Ensure Python packages are installed. You can install them via:

   ```bash
   pip install -r requirements.txt
   ```

> These packages are required for CLI interaction, input handling, and colorized output.

### GUI Prerequisites
   
1. **Install Required System Packages (GUI Only)**

   If you plan to use the **GUI version** (Source or Binary), install the required system-level dependencies:

   #### **Debian / Ubuntu / Kali / Linux Mint**

   ```bash
   sudo apt install -y python3-tk libxcb1
   ```

   #### **Arch / Manjaro**

   ```bash
   sudo pacman -S tk libxcb
   ```

   #### **Fedora**

   ```bash
   sudo dnf install -y python3-tkinter libxcb
   ```

   #### **openSUSE**

   ```bash
   sudo zypper install -y python3-tk libxcb1
   ```

   #### **Pop!\_OS**

   ```bash
   sudo apt install -y python3-tk libxcb1
   ```

> These packages are required for graphical display support. Without them, the GUI binary or source version may fail to launch with errors related to `tkinter` or `libxcb`.

## **⚠️ API Access Notice**

```python
# 🔐 API endpoint removed to prevent abuse or scraping.
# 📬 Reach out on X (formerly Twitter): @AnonKryptiQuz (https://x.com/AnonKryptiQuz) for access or download the precompiled binary to bypass API restrictions.

_cr_u = API_ENDPOINT = "REDACTED_FOR_PUBLIC_RELEASE_CONTACT_X_@AnonKryptiQuz"
```

> In order for the tool to function correctly when running the source code version, you must **manually replace the `_cr_u` variable above with the actual API URL**.
> To obtain it, please contact [@AnonKryptiQuz](https://x.com/AnonKryptiQuz).
> Alternatively, you may [download the precompiled PyInstaller binary](https://github.com/AnonKryptiQuz/DataWhiz/releases), which includes the API and bypasses this restriction.

## **Build Your Own Precompiled Binary**

To create your own standalone executable (binary) for **CLI** or **GUI**, follow these steps:

1. **Create the necessary hook for `fake_useragent`:**

   ```bash
   mkdir -p hooks
   echo "from PyInstaller.utils.hooks import collect_data_files
   datas = collect_data_files('fake_useragent')" > hooks/hook-fake_useragent.py
   ```

2. **Compile the CLI version:**

   ```bash
   pyinstaller --onefile --additional-hooks-dir=hooks DataWhiz_CLI_NEW.py
   ```

3. **Compile the GUI version:**

   ```bash
   pyinstaller --onefile --additional-hooks-dir=hooks DataWhiz_GUI_NEW.py
   ```

This will generate standalone executables for both CLI and GUI versions that include all necessary dependencies.

## **Usage**

DataWhiz provides two modes of operation: a Command Line Interface (CLI) and a Graphical User Interface (GUI). The tool will automatically check and install necessary dependencies when launched.

### **CLI Usage**

1. **Run the CLI version (source code):**

   ```bash
   python DataWhiz_CLI.py
   ```

   **Or run the precompiled binary (no setup required):**

   ```bash
   ./DataWhiz_CLI
   ```

2. **Follow the prompts:**

   * Enter a valid Pakistani mobile number (e.g., `03xxxxxxxxx` or `+923xxxxxxxxx`) or a CNIC number (e.g., `xxxxxxxxxxxxx`).
   * The results will be displayed directly in the terminal.
   * You will be prompted to save the results to a text file.

### **GUI Usage**

1. **Run the GUI version (source code):**

   ```bash
   python DataWhiz_GUI.py
   ```

   **Or run the precompiled binary (no setup required):**

   ```bash
   ./DataWhiz_GUI
   ```

2. **Follow the on-screen instructions:**

   * You'll briefly see a launch animation in your terminal before the GUI window opens.
   * On the initial screen, select either "Mobile Number Lookup" or "CNIC Lookup".
   * Enter the mobile number or CNIC into the input field.
   * Click the "Search" button to retrieve information.
   * Results will be displayed in the text box. You can then use the "Save Results" or "Copy All" buttons.
   * Use the "Clear" button to clear the input and output fields.
   * You can go back to the mode selection screen using the "Back" button.

## **Community Notice**

This tool was developed in response to frequent requests from OSINT researchers and cybersecurity professionals seeking mobile and identity data access within the South Asian region.

Interested in support for other regions? Feel free to reach out on X (formerly Twitter): [@AnonKryptiQuz](https://x.com/AnonKryptiQuz).

Found a bug or want to suggest a feature? [Open an issue](https://github.com/AnonKryptiQuz/DataWhiz/issues)

## Binary Integrity & Scan Reports

Precompiled binaries are scanned and verified clean.  
You can view the full MD5 hashes and VirusTotal reports in [RELEASE.md](./RELEASE.md).

> Always verify the hash before running any binaries for your security.

## **Disclaimer**

* **Educational and Research Purposes Only**
  DataWhiz is intended solely for educational, research, and personal verification purposes.

* **Legal Notice**
  Unauthorized or malicious use of this tool against individuals or for illegal activities is strictly prohibited and may violate local and international laws. Users assume full responsibility for their actions while using this software.

* **Precompiled Binary Advisory**
  The distributed precompiled binaries have been verified to be free of malicious code. Nonetheless, as a best practice, users are advised to execute these binaries within a controlled or isolated environment (e.g., virtual machine or sandbox) to mitigate any potential security risks.

## **Credits**

This tool relies on various open-source libraries and frameworks. We extend our sincere gratitude to the developers and communities behind these projects for their invaluable contributions to the software ecosystem. All credits for the underlying technologies and data sources utilized within DataWhiz go to their rightful owners and creators.

## **Contributors:**

* [Naho666](https://github.com/Naho666)
* [Nuknov](https://github.com/Nuknov)
* [PaKnonymous](https://github.com/PaKnonymous)
* [coffinxp](https://github.com/coffinxp)
* [Hghost0x00](https://github.com/Hghost0x00)
* [1hehaq](https://github.com/1hehaq)

## **Author**

**Created by:** [AnonKryptiQuz](https://AnonKryptiQuz.github.io/)
