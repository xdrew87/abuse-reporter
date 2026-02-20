# AbuseIPDB Reporter

<div align="center">

![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)
![PyQt6](https://img.shields.io/badge/GUI-PyQt6-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-production%20ready-brightgreen.svg)
![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)

## Professional Abuse Reporter for AbuseIPDB

**Beautiful GUI Application • Windows EXE • Powerful CLI**

### 🎯 Quick Links
[📥 Download EXE](https://github.com/xdrew87/abuse-reporter/releases) • [📖 Setup Guide](EXE_SETUP_GUIDE.md) • [✨ What's New](RELEASE_NOTES_v2.0.0.md) • [📋 Categories](#categories-ids-1-23)

</div>

---

## 🚀 Getting Started

### 🪟 Windows Users (Easiest)
```
1. Download abuse-reporter.exe from GitHub Releases
2. Extract files
3. Run abuse-reporter.exe
4. Settings tab → Paste API key → Save
Done! 🎉
```
[Full Windows Setup Guide →](EXE_SETUP_GUIDE.md)

### 💻 Linux/Mac or Source Code
```bash
git clone https://github.com/xdrew87/abuse-reporter.git
cd abuse-reporter
pip install -r requirements.txt
python3 gui.py  # GUI
# OR
python3 main.py # CLI
```

---

## ✨ Features

### 🎨 GUI Application (PyQt6)
- ✅ Modern, professional interface with dark mode
- ✅ Single & bulk IP reporting 
- ✅ Interactive confidence slider (0-100%)
- ✅ Real-time progress tracking
- ✅ API key management in Settings
- ✅ Browse all 23 categories
- ✅ Dry-run validation mode
- ✅ Windows EXE ready to distribute

### 🖥️ CLI (Command Line)
- ✅ Interactive menu mode
- ✅ Direct command arguments
- ✅ Batch reporting scripts
- ✅ Color-coded output
- ✅ All features in GUI

### 🔒 Both Platforms
- ✅ **All 23 AbuseIPDB Categories**
- ✅ **IPv4 & IPv6 Support**
- ✅ **Secure API Key Storage** (.env file)
- ✅ **Type-Safe** (Complete type hints)
- ✅ **Comprehensive Error Handling**
- ✅ **Cross-Platform** (Windows, Linux, macOS)

---

## 📦 Installation & Setup

### Option 1: Windows EXE (Recommended for Windows Users)
```
✓ Download from GitHub Releases
✓ Extract zip file
✓ Run abuse-reporter.exe
✓ No Python needed!
```
👉 [Detailed Windows Setup Guide](EXE_SETUP_GUIDE.md)

### Option 2: From Source Code (Developers)

**Requirements:**
- Python 3.8+
- pip package manager

**Setup:**
```bash
git clone https://github.com/xdrew87/abuse-reporter.git
cd abuse-reporter
pip install -r requirements.txt
python3 gui.py  # Run GUI
```

**For CLI only (no GUI dependencies):**
```bash
pip install requests python-dotenv
python3 main.py
```

---

## 💡 Usage Guide

### GUI Tabs

| Tab | Purpose |
|-----|---------|
| 📝 **Submit** | Report single IP with confidence level |
| 📦 **Bulk** | Submit multiple IPs at once |
| 📚 **Categories** | Browse all 23 abuse categories |
| ⚙️ **Settings** | API key setup & dark mode |

### Quick Examples

### Quick Examples

**GUI (Windows EXE or Source):**
```bash
python3 gui.py   # Opens beautiful GUI window
```

**CLI - Interactive:**
```bash
python3 main.py  # Menu-driven interface
```

**CLI - Direct Command:**
```bash
python3 main.py --ip 192.0.2.1 --categories brute-force --comment "Attack attempt"
```

**CLI - Bulk Report:**
```bash
python3 main.py --ip 192.0.2.1,198.51.100.1 --categories ssh --comment "Brute force" --confidence 95
```

**Test Before Submitting:**
```bash
python3 main.py --ip 192.0.2.1 --categories phishing --dry-run --verbose
```

---

## 📚 API Documentation

### CLI Arguments

```bash
python3 main.py [OPTIONS]

--ip IP                   IPv4 or IPv6 address
--categories CATS         Category names or IDs (comma-separated)
--comment TEXT            Abuse description (max 1000 chars)
--confidence SCORE        0-100 (default: 100)
--dry-run                 Test without submitting
--verbose                 Show detailed output
--list-categories         List all categories
--help                    Show help message
```

### Examples

### Examples

**Single Abuse Report:**
```bash
python3 main.py --ip 203.0.113.45 \
  --categories brute-force,ssh \
  --comment "Failed SSH login attempts on port 22" \
  --confidence 90
```

**Using Category IDs:**
```bash
python3 main.py --ip 198.51.100.12 \
  --categories 18,22 \
  --comment "SSH brute force attack" \
  --confidence 95
```

**Validate First (Dry-Run):**
```bash
python3 main.py --ip 192.0.2.1 \
  --categories phishing \
  --comment "Phishing attempt" \
  --dry-run --verbose
```

---

## 📋 Categories (IDs 1-23)

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

**💡 Tips:**
- Use by ID: `--categories 18,22,4`
- Use by name: `--categories brute-force,ssh,ddos-attack`
- Mix both: `--categories 18,ssh,4`

---

## 🔐 Security

✅ **Your Data is Safe:**
- API keys stored locally in `.env` file only
- Never hardcoded in source code
- HTTPS-only API communication
- Never exposed in error messages

---

## 📂 Project Structure

```
abuse-reporter/
├── gui.py                 # PyQt6 GUI application
├── main.py               # CLI orchestration
├── client.py             # AbuseIPDB API client
├── categories.py         # 23 category definitions
├── validators.py         # Input validation
├── ui.py                 # Terminal UI utilities
├── build.py              # EXE build script (local only)
│
├── logo.svg              # Application logo
├── requirements.txt      # Python dependencies
├── .env.example          # API key template
├── .gitignore            # Git ignore rules
├── LICENSE               # MIT License
├── README.md             # This file
├── EXE_SETUP_GUIDE.md    # Windows setup guide
└── RELEASE_NOTES_v2.0.0.md # What's new
```

---

## ⚙️ Technical Stack

- **GUI:** PyQt6 6.6.0 (cross-platform)
- **Build:** PyInstaller (Windows EXE)
- **Config:** python-dotenv (secure storage)
- **HTTP:** requests library (API communication)
- **Code:** Full type hints, modular design

**Python 3.8+** | **Windows/Linux/macOS**

---

## 🐛 Error Handling

Gracefully handles:
- ✅ Invalid IP addresses (IPv4/IPv6)
- ✅ Invalid categories
- ✅ Missing/wrong API key
- ✅ Network timeouts
- ✅ API rate limiting
- ✅ Server errors
- ✅ Authentication failures

---

## 🤝 Contributing

Want to help? We'd love it! 

1. Fork the repo
2. Create feature branch: `git checkout -b feature/YourFeature`
3. Commit: `git commit -m 'Add YourFeature'`
4. Push: `git push origin feature/YourFeature`
5. Open a Pull Request

---

## 📄 License

MIT License - Use freely for reporting abuse and improving security!

See [LICENSE](LICENSE) file for details.

---

## 🙏 Thanks

- **[AbuseIPDB](https://www.abuseipdb.com)** - Powerful abuse database API
- **PyQt6** - Beautiful GUI framework
- **Python Community** - Excellent libraries

---

<div align="center">

## 🎯 Quick Links

[📥 Download v2.0.0](https://github.com/xdrew87/abuse-reporter/releases) • 
[📖 Setup Guide](EXE_SETUP_GUIDE.md) • 
[✨ What's New](RELEASE_NOTES_v2.0.0.md) • 
[🐛 Issues](https://github.com/xdrew87/abuse-reporter/issues)

### Made with ❤️ for cybersecurity professionals

**Make the internet safer, one report at a time.** 🛡️

</div>
