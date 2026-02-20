# Release Notes - v2.0.0

## 🎉 Major Release: Professional GUI + Windows Distribution

AbuseIPDB Reporter v2.0.0 is a complete rewrite introducing a beautiful PyQt6 GUI, Windows exe distribution, and powerful new features for reporting abuse.

---

## ✨ What's New

### 🖥️ Beautiful GUI Application
- Modern PyQt6 interface with professional styling
- 4 functional tabs: Submit, Bulk, Categories, Settings
- Dark mode support with light/dark theme toggle
- Color-coded status messages (green ✅ success, red ❌ error)
- Interactive confidence slider (0-100%)
- Progress bar for bulk operations

### 🪟 Windows EXE Distribution
- Standalone executable - no Python installation required
- One-click setup for Windows users
- All dependencies bundled
- Ready to distribute and run anywhere

### 🔐 API Key Persistence
- Save API key directly in the GUI (Settings tab)
- Automatically saves to local `.env` file
- Secure masked display (shows `xxxx...xxxx`)
- One-time setup - key persists between sessions

### 📊 Enhanced Reporting
- **Single IP submission** with confidence control
- **Bulk IP submission** - submit multiple IPs simultaneously
- **Dry-run validation** - test before submitting
- Progress tracking for bulk operations
- All 23 AbuseIPDB categories fully supported

### ⚙️ Settings Tab
- API key input and save button
- Dark mode toggle
- IP validation
- User-friendly configuration

### 🌙 Dark Mode
- Beautiful dark theme with proper contrast
- Light mode with professional colors
- Automatic color adaptation for text visibility
- Toggle between themes anytime

---

## 📦 Distribution

### For Windows Users
Download `abuse-reporter.exe` from releases - no installation needed!

**Quick Start:**
1. Extract files
2. Run `abuse-reporter.exe`
3. Go to Settings tab
4. Paste API key
5. Start reporting!

See [EXE_SETUP_GUIDE.md](EXE_SETUP_GUIDE.md) for detailed instructions.

### For Developers
```bash
git clone https://github.com/xdrew87/abuse-reporter.git
cd abuse-reporter
pip install -r requirements.txt
python3 gui.py  # Run GUI
python3 main.py # Run CLI
```

---

## 🔧 Technical Improvements

### Architecture
- Modular Python design with clear separation of concerns
- Complete type hints for IDE support
- Comprehensive error handling
- Input validation on all fields

### GUI Framework
- **Framework**: PyQt6 6.6.0
- **Cross-platform**: Windows, Linux, macOS
- **Responsive**: Handles bulk submissions with progress tracking
- **Accessible**: Keyboard shortcuts, clear labeling

### API Integration
- Full AbuseIPDB API v2 support
- All 23 official categories implemented
- IPv4 and IPv6 validation
- Timeout protection (15-second limit)
- Rate-limit aware error messages

### Security
- API keys stored locally only (`.env` file)
- Never hardcoded in source
- Secure display (masked in GUI)
- HTTPS-only API communication

---

## 📋 Files Included in Release

```
abuse-reporter-v2.0.0.zip
├── abuse-reporter.exe         ← Main application
├── logo.svg                   ← App icon/logo
├── .env.example              ← Configuration template
├── README.md                 ← Full documentation
├── EXE_SETUP_GUIDE.md        ← Windows setup guide
└── LICENSE                   ← MIT License
```

---

## 🐛 Bug Fixes & Improvements

- Fixed category text visibility in light mode (proper color contrast)
- Removed QSvgWidget dependency issues - now uses QPixmap
- Improved error handling for API failures
- Better user feedback with color-coded messages
- Proper file encoding for cross-platform compatibility

---

## 📚 Documentation

- **README.md** - Complete project overview
- **EXE_SETUP_GUIDE.md** - Windows exe setup instructions
- **In-app help** - Settings tab includes setup instructions
- **Categories guide** - View all 23 categories in Categories tab

---

## 🎯 Use Cases

### Single IP Reporting
Report a suspicious IP with details and confidence level.

### Bulk Reporting  
Submit multiple IPs at once with same category/comment.

### Dry-Run Validation
Test your report before actually submitting to AbuseIPDB.

### Category Reference
Browse all 23 abuse categories directly in the app.

---

## 🔄 Platform Support

- ✅ Windows 7+ (exe distribution)
- ✅ Windows 10/11 (recommended)
- ✅ Linux (run from source)
- ✅ macOS (run from source)

---

## 📊 Categories Supported

All 23 official AbuseIPDB categories:
- Brute Force, SSH, Phishing, DDoS
- SQL Injection, Web App Attack
- Spam, Fraud, Hacking
- And 14 more!

See Categories tab in app or `categories.py` for full list.

---

## 💡 Tips

- Use dark mode for nighttime work
- Always test with dry-run first
- Provide detailed comments for better reports
- Set confidence based on how certain you are

---

## 🙏 Thanks

Special thanks to:
- [AbuseIPDB](https://www.abuseipdb.com) for the API
- PyQt6 for the GUI framework
- Python community for excellent libraries

---

## 📞 Support

For issues or questions:
- Check [EXE_SETUP_GUIDE.md](EXE_SETUP_GUIDE.md) for Windows help
- Review [README.md](README.md) for detailed docs
- Report issues on GitHub

---

**Version**: 2.0.0  
**Release Date**: February 2026  
**License**: MIT  
**Status**: Production Ready ✅

**Download v2.0.0**: [Releases Page](https://github.com/xdrew87/abuse-reporter/releases)

---

Make the internet safer, one report at a time. 🛡️
