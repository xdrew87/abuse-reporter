# 🚀 AbuseIPDB Reporter - EXE Setup Guide

## For Windows Users Running the `.exe` File

### ✅ Quick Start (5 minutes)

1. **Extract Files**
   - Download the release package
   - Extract all files to a folder (e.g., `C:\Users\YourName\abuse-reporter\`)
   - Files should include:
     - `abuse-reporter.exe` (main application)
     - `logo.svg` (logo file)
     - `.env.example` (configuration template)

2. **Get Your API Key**
   - Go to: https://www.abuseipdb.com/api
   - Sign up for a FREE account
   - Create an API key (API v2)
   - Copy the key to clipboard

3. **Configure API Key in App**
   - Run `abuse-reporter.exe`
   - Click the **⚙️ Settings** tab
   - Paste your API key in the input field
   - Click **💾 Save Key**
   - ✅ You'll see: "✅ API Key: xxxx...xxxx" (masked)

4. **Start Reporting**
   - Click **📝 Submit** tab
   - Enter IP address
   - Select category
   - Write comment
   - Click **🚀 Submit Report**

### 📋 Detailed Setup

#### Step 1: Extract the Package

```
download/
├── abuse-reporter.exe         ← Run this
├── logo.svg                   ← App logo
├── .env.example              ← Configuration template (for reference)
├── README.md                 ← Documentation
└── GUI_DOCUMENTATION.md      ← GUI guide
```

**Important:** Keep all files in the **same folder**. The app needs the logo to display properly.

#### Step 2: Get API Key

1. Visit: https://www.abuseipdb.com/api
2. Click "Create an Account" (if you don't have one)
3. Log in to your account
4. Click "API" in the menu
5. Under "Reserved Authorization Tokens", copy your API key
6. **Keep this secret!** Don't share it with anyone

#### Step 3: Save API Key in the App

**Method 1: Through GUI (Easiest)**

1. Launch `abuse-reporter.exe`
2. Go to **Settings** tab (⚙️)
3. You'll see "❌ API Key: Not configured"
4. Paste your API key in the text field
5. Click **💾 Save Key**
6. Success message appears: "API key saved successfully!"
7. Now shows: "✅ API Key: xxxxx...xxxxx"

**Method 2: Manual .env File (Advanced)**

If you prefer to create the .env file manually:

1. In the folder with `abuse-reporter.exe`, create a new file
2. Name it: `.env` (exactly this)
3. Add one line:
   ```
   ABUSEIPDB_API_KEY=your_actual_key_here
   ```
4. Save the file
5. Close and reopen `abuse-reporter.exe`
6. Settings tab will show ✅ API Key configured

### 🎯 Using the Application

#### Submit Single IP

1. Click **📝 Submit Report** tab
2. **IP Address**
   - Enter IPv4: `192.0.2.1`
   - Or IPv6: `2001:db8::1`
3. **Category**
   - Click dropdown to see all 23 categories
   - Examples: Brute Force, SSH, Phishing, Fraud
4. **Comment** (required)
   - Describe the abuse
   - e.g., "Multiple SSH login attempts on port 22"
5. **Confidence Score**
   - Slider: 0-100%
   - Default: 100% (you're very confident)
   - Lower if unsure (e.g., 50%)
6. **Dry-Run Mode** (optional)
   - Check to validate without submitting
   - Good for testing first
7. Click **🚀 Submit Report**

#### Submit Multiple IPs (Bulk)

1. Click **📦 Bulk Report** tab
2. **IP Addresses**
   - One per line:
     ```
     192.0.2.1
     192.0.2.2
     203.0.113.45
     ```
3. **Category** - Select one for all IPs
4. **Comment** - Same comment for all
5. **Confidence** - Same level for all
6. Click **🚀 Submit Bulk Report**
7. Watch progress bar fill as reports submit

#### View Categories

1. Click **📚 Categories** tab
2. Browse all 23 official AbuseIPDB categories
3. Each shows:
   - Category ID (e.g., 18 = Brute Force)
   - Category name
   - Description

### 🌙 Dark Mode

**Toggle at any time:**
1. Go to **Settings** tab
2. Click **🌙 Dark Mode: ON/OFF**
3. App will refresh with new theme
4. Setting persists between sessions

### ⚙️ Settings Tab

**Shows:**
- 🎨 **Appearance** - Dark mode toggle
- 🔐 **API Configuration** - API key status
- 📝 **Setup Instructions** - How to configure
- ℹ️ **About** - Version and features

### 🔒 Security & Privacy

✅ **Your API Key is Safe:**
- Stored only in local `.env` file (never uploaded)
- Masked in the GUI (you see `xxxx...xxxx`)
- Kept secure on your computer
- Not shared with anyone

⚠️ **Keep it Secret:**
- Don't share your `.env` file
- Don't commit it to GitHub
- Only one person should know your key per account

### ❓ Troubleshooting

#### "API Key: Not configured"

**Problem:** App shows ❌ API Key not configured

**Solutions:**
1. **Paste API Key**
   - Go to Settings tab
   - Paste your key in the input field
   - Click "💾 Save Key"

2. **Create .env File**
   - Create `.env` file in same folder as exe
   - Add: `ABUSEIPDB_API_KEY=your_key`
   - Restart app

3. **Check File Permissions**
   - Make sure folder is writable
   - Try running as Administrator
   - Try different folder location

#### App Won't Start

**Problem:** Can't run the exe

**Solutions:**
1. **Install Python** (not needed, exe is standalone)
2. **Check Windows Version** - Requires Windows 7+
3. **Install Visual C++ Redistributable** - If app crashes
4. **Run as Administrator** - Right-click exe → "Run as administrator"

#### Reports Won't Submit

**Problem:** Submission fails or times out

**Solutions:**
1. **Check Internet** - Need working internet connection
2. **Check API Key** - Verify it's correct in Settings
3. **Test with Dry-Run** - Check "🔍 Dry-run mode" first
4. **Check AbuseIPDB** - Website might be temporarily down

### 📊 Example Workflows

#### Workflow 1: Report SSH Attack
```
1. IP Address: 203.0.113.42
2. Category: SSH (ID 22)
3. Comment: "Multiple failed SSH login attempts on port 22 detected"
4. Confidence: 95%
5. Submit → ✅ Success
```

#### Workflow 2: Bulk Report Botnet
```
1. IPs (paste 5 addresses)
2. Category: Brute Force (ID 18)
3. Comment: "Part of botnet, scanning network for vulnerabilities"
4. Confidence: 100%
5. Submit → ✅ All submitted
```

#### Workflow 3: Test First, Then Submit
```
1. Fill in report details
2. Check "🔍 Dry-run mode"
3. Click Submit
4. See validation pass ✅
5. Uncheck dry-run
6. Submit for real
```

### 📖 Need More Help?

- **Category Guide** → Click 📚 Categories tab in app
- **API Documentation** → https://www.abuseipdb.com/api
- **Report Status** → Check AbuseIPDB website for your IP history

### 🎓 Tips & Best Practices

✅ **Do:**
- Provide detailed comments describing the abuse
- Use appropriate confidence levels (100% = very sure)
- Report quickly while evidence is fresh
- Use categories that match the abuse type

❌ **Don't:**
- Report accidentally - use dry-run first
- Submit the same IP multiple times same day
- Guess at confidence level if unsure (use 50-75%)
- Use non-English comments (use English)

### 🔄 Updates

To get the latest version:
1. Check GitHub releases
2. Download new exe
3. Run to overwrite old version
4. Your API key (.env) is preserved

---

**Questions?** Check the README.md or visit https://github.com/xdrew87/abuse-reporter

**Stay Safe!** 🛡️
