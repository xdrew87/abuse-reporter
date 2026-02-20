# Contributing to AbuseIPDB Reporter

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help make this a welcoming community
- Report code of conduct violations appropriately

## How to Contribute

### Reporting Issues

Found a bug? Have a feature request? Please open an issue!

**Before opening an issue, please:**
- Check existing issues to avoid duplicates
- Use a clear, descriptive title
- Provide as much context as possible
- Include screenshots or error messages if applicable
- Specify your OS and Python version

**Issue Template:**
```
**Description**
Brief description of the issue

**Steps to Reproduce**
1. Step one
2. Step two
3. ...

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**Environment**
- OS: [Windows/macOS/Linux]
- Python: [version]
- Tool: [version or commit]
```

### Submitting Pull Requests

**Before Starting:**
- Fork the repository
- Create a feature branch from `main`
- Make sure you have Python 3.8+ installed

**Development Setup:**
```bash
# Clone your fork
git clone https://github.com/your-username/abuse-reporter.git
cd abuse-reporter

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Make changes and test
python main.py --list-categories
```

**Code Guidelines:**
- Follow PEP 8 style guide
- Use type hints for all functions
- Add docstrings to functions
- Keep functions focused and modular
- Test your changes before submitting

**Commit Messages:**
```
[Type] Brief description

More detailed explanation if needed.

- Bullet points for changes
- One change per line
```

Commit types:
- `[feat]` - New feature
- `[fix]` - Bug fix
- `[docs]` - Documentation
- `[style]` - Code style (formatting, missing semicolons, etc.)
- `[refactor]` - Code reorganization without behavior change
- `[test]` - Adding tests
- `[chore]` - Maintenance, updates, etc.

**Pull Request Guidelines:**
1. Ensure code follows project style
2. Update documentation if needed
3. Test thoroughly
4. Keep PRs focused on single changes
5. Provide clear PR description

**PR Template:**
```
**Description**
What does this PR do?

**Related Issues**
Closes #123

**Changes Made**
- Change one
- Change two

**Testing**
How was this tested?

**Checklist**
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes
```

## Development Areas

### Areas We're Working On

1. **Bulk Reporting** - Optimize for large batches
2. **Report History** - Track submitted reports
3. **Category Search** - Better category discovery
4. **Error Messages** - Even more helpful feedback
5. **Performance** - Faster validation and submission

### Ways to Help

- **Documentation** - Improve README, examples, or docstrings
- **Code Quality** - Refactor, optimize, or simplify code
- **Testing** - Add more test coverage
- **Features** - Implement new capabilities
- **Bug Fixes** - Fix reported issues
- **Examples** - Add real-world usage examples

## Testing

### Manual Testing

Before submitting a PR, test these scenarios:

```bash
# List categories
python main.py --list-categories

# Dry-run validation
python main.py --ip 192.0.2.1 --categories brute-force --comment "Test" --dry-run --verbose

# Interactive mode
python main.py

# Multiple categories
python main.py --ip 198.51.100.1 --categories 18,22,4 --comment "Multi-category test"

# Invalid inputs (error handling)
python main.py --ip invalid --categories unknown --comment ""
```

### Code Style

Use consistent formatting:
```python
# Type hints required
def function_name(param: str) -> bool:
    """Docstring explaining function."""
    return True

# Comments for non-obvious logic
if complex_condition:  # This handles edge case X
    do_something()
```

## Documentation

### Updating Documentation

- Keep README.md current with features and changes
- Update docstrings when changing function behavior
- Add examples for new features
- Write clear, accessible documentation

### Documentation Style

```python
"""
Brief one-line description.

More detailed explanation if needed.

Args:
    param1: Description of param1
    param2: Description of param2

Returns:
    Description of return value

Raises:
    ValueError: When invalid input provided
    
Example:
    >>> result = function("test")
    >>> print(result)
```

## Project Structure

```
.
├── main.py           # Entry point and CLI logic
├── ui.py             # User interface and formatting
├── client.py         # API client
├── categories.py     # Category mappings
├── validators.py     # Input validation
├── requirements.txt  # Dependencies
├── .env.example      # Example config
├── README.md         # Main documentation
├── ABOUT.md          # Project info
├── LICENSE           # MIT License
└── CONTRIBUTING.md   # This file
```

## Review Process

- Maintainers will review PRs within a reasonable timeframe
- Changes might be requested before merging
- Once approved, PR will be merged into main
- Your contribution will be acknowledged publicly

## Questions?

- Check existing documentation
- Look at similar code for patterns
- Open an issue to discuss major changes
- Comment on PRs for clarification

## Recognition

Contributors will be recognized in:
- Commit history
- Project README (if applicable)
- Release notes

Thank you for helping make this project better! 🎉
