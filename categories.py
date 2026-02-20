"""AbuseIPDB category definitions and mappings."""

from typing import Dict, Optional

# Official AbuseIPDB categories (ID: name mapping)
CATEGORIES: Dict[int, str] = {
    1: "dns-compromise",
    2: "dns-poisoning",
    3: "fraud-orders",
    4: "ddos-attack",
    5: "ftp-brute-force",
    6: "ping-of-death",
    7: "phishing",
    8: "fraud-voip",
    9: "open-proxy",
    10: "web-spam",
    11: "email-spam",
    12: "blog-spam",
    13: "vpn-ip",
    14: "port-scan",
    15: "hacking",
    16: "sql-injection",
    17: "spoofing",
    18: "brute-force",
    19: "bad-web-bot",
    20: "exploited-host",
    21: "web-app-attack",
    22: "ssh",
    23: "iot-targeted",
}

# Reverse mapping for human-readable name -> ID
NAME_TO_ID: Dict[str, int] = {v.lower(): k for k, v in CATEGORIES.items()}

# Add aliases for backward compatibility and ease of use (without hyphens)
ALIASES: Dict[str, int] = {
    "bruteforce": 18,
    "brute": 18,
    "ddos": 4,
    "ftpbruteforce": 5,
    "ftpbrute": 5,
    "ioittargeted": 23,
    "iot": 23,
    "pingdeath": 6,
    "voipfraud": 8,
    "vpn": 13,
    "sqli": 16,
    "websqli": 16,
}

# Combine all mappings
ALL_NAMES: Dict[str, int] = {**NAME_TO_ID, **ALIASES}


def get_category_id(category_name: str) -> Optional[int]:
    """
    Convert a human-readable category name to its numeric ID.
    Supports both hyphenated and non-hyphenated formats.
    
    Args:
        category_name: The human-readable category name (case-insensitive)
        
    Returns:
        The numeric category ID, or None if not found
    """
    # Try exact match first
    normalized = category_name.lower().strip()
    if normalized in ALL_NAMES:
        return ALL_NAMES[normalized]
    
    # Try removing hyphens
    normalized_no_hyphens = normalized.replace("-", "")
    if normalized_no_hyphens in ALL_NAMES:
        return ALL_NAMES[normalized_no_hyphens]
    
    # Try removing spaces
    normalized_no_spaces = normalized.replace(" ", "")
    if normalized_no_spaces in ALL_NAMES:
        return ALL_NAMES[normalized_no_spaces]
    
    return None


def get_category_name(category_id: int) -> Optional[str]:
    """
    Convert a numeric category ID to its human-readable name.
    
    Args:
        category_id: The numeric category ID
        
    Returns:
        The human-readable category name, or None if not found
    """
    return CATEGORIES.get(category_id)


def validate_categories(category_names: list[str]) -> tuple[bool, list[int], list[str]]:
    """
    Validate a list of category names and convert to IDs.
    
    Args:
        category_names: List of human-readable category names
        
    Returns:
        Tuple of (is_valid, category_ids, invalid_names)
    """
    category_ids = []
    invalid_names = []
    
    for name in category_names:
        category_id = get_category_id(name)
        if category_id is None:
            invalid_names.append(name)
        else:
            category_ids.append(category_id)
    
    is_valid = len(invalid_names) == 0
    return is_valid, category_ids, invalid_names


def list_all_categories() -> None:
    """Print all available categories."""
    print("\nAvailable AbuseIPDB Categories:")
    print("-" * 50)
    for category_id, name in sorted(CATEGORIES.items()):
        print(f"  {name:<20} (ID: {category_id})")
    print()
