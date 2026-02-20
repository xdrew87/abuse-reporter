# AbuseIPDB Reporter CLI

<div align="center">

![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-production%20ready-brightgreen.svg)

**A beautiful, production-ready Python CLI tool for submitting abuse reports to AbuseIPDB API v2**

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Examples](#examples)

</div>

---

A powerful command-line interface for reporting malicious IP addresses to AbuseIPDB without leaving your terminal. Features an elegant interactive menu, bulk reporting capabilities, and comprehensive validation.

## ✨ Features

- **Beautiful Terminal UI** - Color-coded interface with formatted menus and real-time feedback
- **Interactive & CLI Modes** - Choose between guided prompts or direct command-line arguments
- **Bulk Reporting** - Submit multiple reports in one session with progress tracking
- **All 23 Categories** - Full support for official AbuseIPDB categories with ID-based selection
- **IPv4 & IPv6** - Validates both IPv4 and IPv6 address formats
- **Type-Safe** - Complete type hints for reliability and IDE support
- **Secure** - API key loaded from `.env` file, never hardcoded
- **Dry-Run Mode** - Validate reports before submission
- **Verbose Output** - Inspect full API responses for debugging
- **Production-Ready** - Comprehensive error handling and proper exit codes

## 📦 Installation

### Requirements
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone/Download the repository**
   ```bash
   git clone https://github.com/xdrew87/abuse-reporter.git
   cd abuse-reporter
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API key**
   ```bash
   # Create .env file from template
   cp .env.example .env
   
   # Edit .env and add your AbuseIPDB API key
   # ABUSEIPDB_API_KEY=your_api_key_here
   ```

   Get your API key from [AbuseIPDB](https://www.abuseipdb.com/api)

4. **Verify installation**
   ```bash
   python main.py --list-categories
   ```

## 🚀 Quick Start

### Interactive Mode (Recommended)
```bash
python main.py
```

Launches an intuitive menu:
- Submit Abuse Report
- View Categories
- Test Report (Dry-Run)
- Bulk Report
- Exit

### Command-Line Mode
```bash
# Single report
python main.py --ip 192.0.2.1 --categories brute-force,ssh --comment "SSH attack"

# List all categories
python main.py --list-categories
```

## 📖 Usage

### Interactive Menu

Simply run without arguments to launch the interactive menu:
```bash
python main.py
```

**Menu Options:**

| Option | Description |
|--------|-------------|
| [1] Submit Abuse Report | Report a single IP with guided input |
| [2] View Categories | Browse all 23 abuse categories |
| [3] Test Report | Validate without submitting (dry-run) |
| [4] Bulk Report | Submit multiple reports at once |
| [0] Exit | Quit the application |

### Command-Line Options

```
Usage: python main.py [OPTIONS]

Arguments:
  --ip IP                    IPv4 or IPv6 address to report
  --categories CATS          Comma-separated category names or IDs
  --comment TEXT             Abuse description (max 1000 characters)
  --confidence SCORE         Confidence level 0-100 (default: 100)
  --dry-run                  Validate without submitting to API
  --verbose                  Show detailed output and API response
  --cli                      Force interactive menu mode
  --list-categories          List all categories and exit
```

## 📚 Examples

### Single Report via CLI
```bash
python main.py \
  --ip 203.0.113.45 \
  --categories brute-force,ssh \
  --comment "Multiple failed SSH login attempts on port 22" \
  --confidence 90
```

### Using Category IDs
```bash
# Category IDs: 18=brute-force, 22=ssh
python main.py \
  --ip 198.51.100.12 \
  --categories 18,22 \
  --comment "SSH brute force attack" \
  --confidence 95
```

### Test Before Submitting
```bash
python main.py \
  --ip 192.0.2.1 \
  --categories phishing,fraud-orders \
  --comment "Phishing attempt targeting bank customers" \
  --dry-run \
  --verbose
```

### View Available Categories
```bash
python main.py --list-categories
```

### Bulk Reporting
```bash
python main.py
# Then select option [4] Bulk Report
```

## 🏷️ Categories (IDs 1-23)

| ID | Category | ID | Category |
|----|----------|----|----|
| 1 | dns-compromise | 13 | vpn-ip |
| 2 | dns-poisoning | 14 | port-scan |
| 3 | fraud-orders | 15 | hacking |
| 4 | ddos-attack | 16 | sql-injection |
| 5 | ftp-brute-force | 17 | spoofing |
| 6 | ping-of-death | 18 | brute-force |
| 7 | phishing | 19 | bad-web-bot |
| 8 | fraud-voip | 20 | exploited-host |
| 9 | open-proxy | 21 | web-app-attack |
| 10 | web-spam | 22 | ssh |
| 11 | email-spam | 23 | iot-targeted |
| 12 | blog-spam | | |

**Usage Tips:**
- Use format: `--categories 18,22,4` for multiple by ID
- Or use names: `--categories brute-force,ssh,ddos-attack`
- IDs and names can be mixed: `--categories 18,ssh,4`
- Interactive mode displays the full table for easy selection

## 🔐 Security

- **No Secrets in Repo**: API keys stored in `.env` file (excluded from git)
- **Input Validation**: All parameters validated before API submission
- **HTTPS Only**: All API communications encrypted
- **Timeout Protection**: 15-second timeout prevents hanging requests
- **Clean Error Messages**: Sensitive information never exposed in errors

## 📋 File Structure

```
abuse-reporter/
├── main.py           # CLI orchestration & menu system
├── ui.py             # Terminal UI (colors, prompts, formatting)
├── client.py         # AbuseIPDB API client
├── categories.py     # Category definitions & mappings
├── validators.py     # Input validation functions
├── requirements.txt  # Python dependencies
├── .env.example      # Example environment configuration
├── .gitignore        # Git ignore patterns
└── README.md         # This file
```

## 🛠️ Technical Details

### Architecture
- **Modular Design** - Separation of concerns across 5 Python modules
- **Type Hints** - Full type annotations for IDE support
- **Error Handling** - Comprehensive error handling throughout
- **Input Validation** - All inputs validated before API calls

### API Integration
- **Endpoint**: `https://api.abuseipdb.com/api/v2/report`
- **Method**: POST with JSON payload
- **Authentication**: API key in HTTP header
- **Success Response**: HTTP 201 or 200 with data confirmation
- **Timeout**: 15 seconds per request

### Supported OS
- Linux ✅
- macOS ✅
- Windows ✅

## 🐛 Error Handling

The tool gracefully handles:
- Invalid IP addresses (IPv4/IPv6 validation)
- Invalid categories (with helpful suggestions)
- Missing/invalid API key
- Rate limiting (429 Too Many Requests)
- Authentication failures (401 Unauthorized)
- Server errors (5xx responses)
- Network timeouts and connection issues

## 📊 Exit Codes

- `0` - Success or validation passed
- `1` - Validation error, API error, or invalid input

## 💡 Tips & Tricks

### Setting API Key

**Option 1: `.env` file (Recommended)**
```bash
cp .env.example .env
# Edit .env with your API key
```

**Option 2: Environment variable**
```bash
export ABUSEIPDB_API_KEY='your_key_here'
python main.py
```

**Option 3: PowerShell (Windows)**
```powershell
$env:ABUSEIPDB_API_KEY='your_key_here'
python main.py
```

### Batch Reporting Script
```bash
#!/bin/bash
for ip in 192.0.2.1 198.51.100.1 203.0.113.1; do
  python main.py --ip $ip --categories brute-force --comment "Suspicious activity" --confidence 75
done
```

## 💻 Development

### Project Setup
```bash
# Clone repository
git clone https://github.com/xdrew87/abuse-reporter.git
cd abuse-reporter

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running Tests
```bash
# Test dry-run mode
python main.py --dry-run --ip 198.51.100.1 --categories brute-force --comment "Test"

# Test with verbose output
python main.py --ip 192.0.2.1 --categories phishing --comment "Test" --verbose
```

## 📝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

MIT License - See LICENSE file for details. Feel free to use this tool for reporting abuse and improving internet security.

## 🙏 Acknowledgments

- [AbuseIPDB](https://www.abuseipdb.com) - For providing the API and documentation
- Built with ❤️ for cybersecurity professionals and network administrators

## 📧 Support

For issues, questions, or feedback:
- Check the [Examples](#examples) section first
- Use `--help` flag for quick reference
- Use `--verbose` to see detailed API responses
- Review error messages - they provide helpful hints
- Check [AbuseIPDB API docs](https://www.abuseipdb.com/api)

---

<div align="center">

**Make the internet safer, one report at a time.**

[Back to top](#abuseipdb-reporter-cli)

</div>
