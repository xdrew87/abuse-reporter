"""Input validation utilities."""

import re
from ipaddress import IPv4Address, IPv6Address, AddressValueError
from typing import Optional


def validate_ipv4(ip: str) -> bool:
    """
    Validate an IPv4 address.
    
    Args:
        ip: The IP address string to validate
        
    Returns:
        True if valid IPv4, False otherwise
    """
    try:
        IPv4Address(ip)
        return True
    except AddressValueError:
        return False


def validate_ipv6(ip: str) -> bool:
    """
    Validate an IPv6 address.
    
    Args:
        ip: The IP address string to validate
        
    Returns:
        True if valid IPv6, False otherwise
    """
    try:
        IPv6Address(ip)
        return True
    except AddressValueError:
        return False


def validate_ip(ip: str) -> bool:
    """
    Validate either IPv4 or IPv6 address.
    
    Args:
        ip: The IP address string to validate
        
    Returns:
        True if valid IPv4 or IPv6, False otherwise
    """
    return validate_ipv4(ip) or validate_ipv6(ip)


def validate_confidence(confidence: int) -> tuple[bool, Optional[str]]:
    """
    Validate confidence score (0-100).
    
    Args:
        confidence: The confidence score to validate
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not isinstance(confidence, int):
        return False, "Confidence must be an integer"
    
    if confidence < 0 or confidence > 100:
        return False, "Confidence must be between 0 and 100"
    
    return True, None


def validate_comment(comment: str) -> tuple[bool, Optional[str]]:
    """
    Validate comment string.
    
    Args:
        comment: The comment string to validate
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not comment:
        return False, "Comment cannot be empty"
    
    if len(comment) > 1000:
        return False, "Comment cannot exceed 1000 characters"
    
    return True, None


def validate_api_key(api_key: Optional[str]) -> tuple[bool, Optional[str]]:
    """
    Validate API key format.
    
    Args:
        api_key: The API key string to validate
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not api_key:
        return False, "ABUSEIPDB_API_KEY environment variable not set"
    
    # AbuseIPDB API keys are hexadecimal strings (typically 64+ characters)
    # Accept any string that's at least 32 hex characters to be flexible
    if not re.match(r'^[a-f0-9]{32,}$', api_key.strip()):
        return False, "Invalid API key format (must be hexadecimal)"
    
    return True, None
