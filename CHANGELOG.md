# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2024-02-20

### Added
- **Bulk Reporting Feature** - Submit multiple IP reports in a single session
- **Interactive Category Selection** - Visual table showing all categories with IDs
- **Enhanced Terminal UI** - Professional color-coded interface with gradient effects
- **Confidence Score Visualization** - Visual bar showing confidence level (0-100)
- **Better Exit Message** - Improved goodbye screen with better styling
- **Full Type Hints** - Complete type annotations throughout codebase
- **Comprehensive Documentation** - README, ABOUT.md, CONTRIBUTING.md

### Changed
- **Category ID-Based Selection** - Users select by numeric ID instead of typing names
- **Menu Structure** - Updated menu items (option 0 for exit, option 4 for bulk)
- **Input Validation** - Enhanced validation feedback during input
- **Error Messages** - More helpful and descriptive error messages
- **API Parameter** - Fixed category parameter from singular to plural

### Fixed
- **Category ID Mappings** - Corrected all 23 category IDs to match official AbuseIPDB
- **HTTP Status Handling** - Now accepts both 200 and 201 responses
- **Response Data Detection** - Improved detection of successful submissions
- **Color Code Issues** - Fixed ANSI color code compatibility

### Security
- **No Hardcoded Keys** - API keys only from .env file
- **Input Sanitization** - All inputs validated before API submission
- **HTTPS Only** - All communications encrypted
- **Timeout Protection** - 15-second timeout prevents hanging

## [1.0.0] - 2024-02-15

### Added
- Initial production release
- Interactive menu interface
- CLI argument support
- All 23 AbuseIPDB categories
- IPv4/IPv6 validation
- Dry-run mode
- Verbose output option
- Beautiful terminal UI with colors
- .env configuration support
- Comprehensive error handling

### Features
- Submit single abuse reports
- View available categories
- Test reports before submission
- Validate inputs before API call
- Proper exit codes for scripting
- Type-safe Python code with hints

---

## Version 2.0.0 Highlights

### What's New?
- **Bulk Operations** - Report multiple IPs efficiently
- **Better Visual Design** - More professional terminal interface
- **Improved UX** - Visual category table makes selection easier
- **Confidence Visualization** - See confidence level at a glance
- **Enhanced Feedback** - Real-time validation messages

### Breaking Changes
- Category selection now uses numeric IDs instead of names
- Menu option numbering changed (exit moved to [0])
- Some command-line options may have subtle changes

### Migration from 1.0.0
If upgrading from v1.0.0:

```bash
# Old way (still works but not preferred)
python main.py --categories brute-force,ssh

# New way (preferred)
python main.py --categories 18,22
```

### Deprecated
- None yet, all features from v1.0.0 still supported

---

## Reporting Issues

Found a bug? Have suggestions? Please:
1. Check [existing issues](issues)
2. Open a [new issue](issues/new) with details
3. Follow the issue template
4. Include steps to reproduce

## Contributing

Interested in contributing? See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Development setup
- Code guidelines
- Pull request process
- Testing procedures

---

## Future Roadmap

### Planned Features
- Report history/logging
- CSV batch import
- Report verification
- Statistics dashboard
- Webhook integration

### Under Consideration
- Configuration profiles
- Report scheduling
- Integration with SIEM systems
- Multi-language support
- Desktop GUI version

---

**[View All Releases](../../releases)**
