"""UI utilities for terminal display with professional styling."""

import sys
import os
from typing import Optional


# ANSI color codes
class Colors:
    """ANSI color codes."""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    
    # Foreground colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright foreground colors
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'


def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_banner() -> None:
    """Print the application banner with enhanced ASCII art."""
    banner = f"""
{Colors.BRIGHT_CYAN}{Colors.BOLD}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}{Colors.BG_CYAN}{Colors.BLACK}                                                           {Colors.RESET}{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}        {Colors.BRIGHT_YELLOW}{Colors.BOLD}█████╗ ██████╗ ██╗   ██╗███████╗███████╗{Colors.RESET}         {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}        {Colors.BRIGHT_YELLOW}{Colors.BOLD}██╔══██╗██╔══██╗██║   ██║██╔════╝██╔════╝{Colors.RESET}        {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}        {Colors.BRIGHT_RED}{Colors.BOLD}███████║██████╔╝██║   ██║███████╗█████╗{Colors.RESET}          {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}        {Colors.BRIGHT_MAGENTA}{Colors.BOLD}██╔══██║██╔══██╗██║   ██║╚════██║██╔══╝{Colors.RESET}          {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}        {Colors.BRIGHT_BLUE}{Colors.BOLD}██║  ██║██████╔╝╚██████╔╝███████║███████╗{Colors.RESET}        {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}        {Colors.BRIGHT_YELLOW}{Colors.BOLD}╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝╚══════╝{Colors.RESET}        {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}{Colors.BG_CYAN}{Colors.BLACK}                                                           {Colors.RESET}{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}             {Colors.BRIGHT_GREEN}{Colors.BOLD}→ AbuseIPDB Report Submitter ←{Colors.RESET}             {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}         {Colors.BRIGHT_WHITE}{Colors.DIM}Report malicious IPs directly to AbuseIPDB{Colors.RESET}       {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}{Colors.BG_CYAN}{Colors.BLACK}                                                           {Colors.RESET}{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(banner)


def print_exit_message() -> None:
    """Print an enhanced exit message with celebratory styling."""
    exit_msg = f"""
{Colors.BRIGHT_GREEN}{Colors.BOLD}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}
{Colors.BRIGHT_GREEN}{Colors.BOLD}║{Colors.RESET}{Colors.BG_GREEN}{Colors.BLACK}                                                           {Colors.RESET}{Colors.BRIGHT_GREEN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_GREEN}{Colors.BOLD}║{Colors.RESET}                                                         {Colors.BRIGHT_GREEN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_GREEN}{Colors.BOLD}║{Colors.RESET}      {Colors.BRIGHT_CYAN}{Colors.BOLD}✓ Thank you for using AbuseIPDB Reporter{Colors.RESET}       {Colors.BRIGHT_GREEN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_GREEN}{Colors.BOLD}║{Colors.RESET}                                                         {Colors.BRIGHT_GREEN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_GREEN}{Colors.BOLD}║{Colors.RESET}      {Colors.BRIGHT_WHITE}{Colors.DIM}Stay safe, stay secure, stay vigilant!{Colors.RESET}       {Colors.BRIGHT_GREEN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_GREEN}{Colors.BOLD}║{Colors.RESET}                                                         {Colors.BRIGHT_GREEN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_GREEN}{Colors.BOLD}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(exit_msg)


def print_menu() -> None:
    """Print the main menu with enhanced styling."""
    menu = f"""
{Colors.BRIGHT_CYAN}{Colors.BOLD}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}                   {Colors.BRIGHT_MAGENTA}{Colors.BOLD}▶ MAIN MENU ◀{Colors.RESET}                     {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}                                                         {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}  {Colors.BRIGHT_YELLOW}{Colors.BOLD}[1]{Colors.RESET}  {Colors.BRIGHT_WHITE}Submit Abuse Report{Colors.RESET}                      {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}      {Colors.DIM}Report a single malicious IP address{Colors.RESET}          {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}                                                         {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}  {Colors.BRIGHT_YELLOW}{Colors.BOLD}[2]{Colors.RESET}  {Colors.BRIGHT_WHITE}View Categories{Colors.RESET}                          {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}      {Colors.DIM}Browse all 23 abuse categories{Colors.RESET}                   {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}                                                         {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}  {Colors.BRIGHT_YELLOW}{Colors.BOLD}[3]{Colors.RESET}  {Colors.BRIGHT_WHITE}Test Report (Dry-Run){Colors.RESET}                    {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}      {Colors.DIM}Validate report without submitting{Colors.RESET}                {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}                                                         {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}  {Colors.BRIGHT_YELLOW}{Colors.BOLD}[4]{Colors.RESET}  {Colors.BRIGHT_WHITE}Bulk Report{Colors.RESET}                              {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}      {Colors.DIM}Submit multiple reports at once{Colors.RESET}                  {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}                                                         {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}  {Colors.BRIGHT_YELLOW}{Colors.BOLD}[0]{Colors.RESET}  {Colors.BRIGHT_WHITE}Exit{Colors.RESET}                                       {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}      {Colors.DIM}Quit the application{Colors.RESET}                             {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}                                                         {Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.RESET}
{Colors.BRIGHT_CYAN}{Colors.BOLD}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(menu)


def print_section(title: str) -> None:
    """Print a section header with enhanced styling and decorative elements."""
    width = 62
    title_with_arrows = f"▶ {title} ◀"
    padding = (width - len(title_with_arrows)) // 2
    
    # Enhanced section with gradient-like color effect
    print()
    print(f"{Colors.BRIGHT_YELLOW}{Colors.BOLD}{'═' * width}{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}{Colors.BOLD}{'═' * padding}{Colors.BRIGHT_CYAN}{Colors.BOLD}{title_with_arrows}{Colors.BRIGHT_YELLOW}{Colors.BOLD}{'═' * padding}{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}{Colors.BOLD}{'═' * width}{Colors.RESET}\n")


def print_success(message: str) -> None:
    """Print a success message with enhanced styling."""
    print(f"{Colors.BRIGHT_GREEN}{Colors.BOLD}✓{Colors.RESET} {Colors.BRIGHT_GREEN}{message}{Colors.RESET}")


def print_error(message: str) -> None:
    """Print an error message with enhanced styling."""
    print(f"{Colors.BRIGHT_RED}{Colors.BOLD}✗ {message}{Colors.RESET}", file=sys.stderr)


def print_warning(message: str) -> None:
    """Print a warning message with enhanced styling."""
    print(f"{Colors.BRIGHT_YELLOW}{Colors.BOLD}⚠  {message}{Colors.RESET}")


def print_info(message: str) -> None:
    """Print an info message with enhanced styling."""
    print(f"{Colors.BRIGHT_BLUE}{Colors.BOLD}ℹ  {message}{Colors.RESET}")


def print_input_prompt(prompt: str) -> str:
    """Print an input prompt with enhanced styling and better formatting."""
    formatted_prompt = f"\n{Colors.BRIGHT_YELLOW}{Colors.BOLD}→{Colors.RESET} {Colors.BRIGHT_WHITE}{prompt}{Colors.RESET}\n  {Colors.BRIGHT_CYAN}{Colors.BOLD}❯{Colors.RESET} "
    return input(formatted_prompt).strip()


def print_category_list() -> None:
    """Print all available categories in a formatted list with enhanced visuals."""
    from categories import CATEGORIES
    
    print_section("AVAILABLE CATEGORIES")
    
    # Header with enhanced styling
    header = f"{Colors.BRIGHT_CYAN}{Colors.BOLD}┌─────┬──────────────────────┬─────┬──────────────────────┐{Colors.RESET}"
    print(header)
    print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}│  ID │ Category{Colors.RESET}             {Colors.BRIGHT_CYAN}{Colors.BOLD}│  ID │ Category{Colors.RESET}             {Colors.BRIGHT_CYAN}{Colors.BOLD}│{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}├─────┼──────────────────────┼─────┼──────────────────────┤{Colors.RESET}")
    
    category_items = sorted(CATEGORIES.items())
    mid = len(category_items) // 2
    
    for i in range(mid):
        left_id, left_name = category_items[i]
        right_id, right_name = category_items[mid + i] if mid + i < len(category_items) else (None, None)
        
        left_str = f"{Colors.BRIGHT_YELLOW}{Colors.BOLD}{left_id:2}{Colors.RESET}  {Colors.BRIGHT_WHITE}{left_name:<18}{Colors.RESET}"
        if right_id:
            right_str = f"{Colors.BRIGHT_YELLOW}{Colors.BOLD}{right_id:2}{Colors.RESET}  {Colors.BRIGHT_WHITE}{right_name:<18}{Colors.RESET}"
            print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}│{Colors.RESET} {left_str} {Colors.BRIGHT_CYAN}{Colors.BOLD}│{Colors.RESET} {right_str} {Colors.BRIGHT_CYAN}{Colors.BOLD}│{Colors.RESET}")
        else:
            print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}│{Colors.RESET} {left_str} {Colors.BRIGHT_CYAN}{Colors.BOLD}│{Colors.RESET}      {' ' * 20} {Colors.BRIGHT_CYAN}{Colors.BOLD}│{Colors.RESET}")
    
    footer = f"{Colors.BRIGHT_CYAN}{Colors.BOLD}└─────┴──────────────────────┴─────┴──────────────────────┘{Colors.RESET}"
    print(footer)
    print()


def print_report_summary(
    ip: str,
    categories: list[str],
    comment: str,
    confidence: int,
    verbose: bool = False
) -> None:
    """Print a formatted report summary with enhanced visuals."""
    from categories import get_category_id
    
    print_section("REPORT SUMMARY")
    
    # Get category IDs to show
    category_ids = [get_category_id(cat) for cat in categories]
    
    # Enhanced summary box with color gradient
    print(f"{Colors.BRIGHT_MAGENTA}{Colors.BOLD}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{Colors.RESET}")
    print(f"{Colors.BRIGHT_MAGENTA}{Colors.BOLD}┃{Colors.RESET}  {Colors.BRIGHT_YELLOW}{Colors.BOLD}IP Address:{Colors.RESET}        {Colors.BRIGHT_CYAN}{ip:<43}{Colors.BRIGHT_MAGENTA}{Colors.BOLD}┃{Colors.RESET}")
    print(f"{Colors.BRIGHT_MAGENTA}{Colors.BOLD}┃{Colors.RESET}  {Colors.BRIGHT_YELLOW}{Colors.BOLD}Categories:{Colors.RESET}        {Colors.BRIGHT_GREEN}{', '.join(categories):<43}{Colors.BRIGHT_MAGENTA}{Colors.BOLD}┃{Colors.RESET}")
    print(f"{Colors.BRIGHT_MAGENTA}{Colors.BOLD}┃{Colors.RESET}  {Colors.BRIGHT_YELLOW}{Colors.BOLD}Category IDs:{Colors.RESET}      {Colors.BRIGHT_BLUE}{', '.join(str(cid) for cid in category_ids):<43}{Colors.BRIGHT_MAGENTA}{Colors.BOLD}┃{Colors.RESET}")
    
    # Confidence bar visualization
    bar_length = 20
    filled = int((confidence / 100) * bar_length)
    bar = "█" * filled + "░" * (bar_length - filled)
    conf_color = Colors.BRIGHT_GREEN if confidence >= 75 else Colors.BRIGHT_YELLOW if confidence >= 50 else Colors.BRIGHT_RED
    print(f"{Colors.BRIGHT_MAGENTA}{Colors.BOLD}┃{Colors.RESET}  {Colors.BRIGHT_YELLOW}{Colors.BOLD}Confidence:{Colors.RESET}        {conf_color}{bar}{Colors.RESET} {confidence}%{' ' * (31 - len(str(confidence)))}{Colors.BRIGHT_MAGENTA}{Colors.BOLD}┃{Colors.RESET}")
    
    comment_preview = comment[:39] + ('...' if len(comment) > 39 else '')
    print(f"{Colors.BRIGHT_MAGENTA}{Colors.BOLD}┃{Colors.RESET}  {Colors.BRIGHT_YELLOW}{Colors.BOLD}Comment:{Colors.RESET}           {Colors.BRIGHT_WHITE}{comment_preview:<43}{Colors.BRIGHT_MAGENTA}{Colors.BOLD}┃{Colors.RESET}")
    
    if verbose:
        print(f"{Colors.BRIGHT_MAGENTA}{Colors.BOLD}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫{Colors.RESET}")
        print(f"{Colors.BRIGHT_MAGENTA}{Colors.BOLD}┃{Colors.RESET}  {Colors.DIM}{Colors.BRIGHT_WHITE}Full Comment:{Colors.RESET}{Colors.DIM}")
        # Print comment wrapped if needed
        for line in [comment[i:i+50] for i in range(0, len(comment), 50)]:
            print(f"{Colors.BRIGHT_MAGENTA}{Colors.BOLD}┃{Colors.RESET}  {Colors.DIM}{line:<51}{Colors.BRIGHT_MAGENTA}{Colors.BOLD}┃{Colors.RESET}")
        print(f"{Colors.BRIGHT_MAGENTA}{Colors.BOLD}┃{Colors.RESET}  {Colors.RESET}")
    
    print(f"{Colors.BRIGHT_MAGENTA}{Colors.BOLD}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{Colors.RESET}\n")


def print_separator(char: str = "─", length: int = 60) -> None:
    """Print a separator line with enhanced styling."""
    print(f"\n{Colors.BRIGHT_YELLOW}{Colors.BOLD}{char * length}{Colors.RESET}\n")


def print_box(title: str, content: str) -> None:
    """Print a formatted box with title and content with enhanced visuals."""
    box_width = max(len(title) + 6, len(content) + 4, 62)
    
    print(f"\n{Colors.BRIGHT_GREEN}{Colors.BOLD}╔{'═' * (box_width - 2)}╗{Colors.RESET}")
    print(f"{Colors.BRIGHT_GREEN}{Colors.BOLD}║{Colors.RESET}{Colors.BG_GREEN}{Colors.BLACK} {Colors.BRIGHT_GREEN}{Colors.BOLD}{title.center(box_width - 6)}{Colors.RESET}{Colors.BG_GREEN}{Colors.BLACK} {Colors.RESET}{Colors.BRIGHT_GREEN}{Colors.BOLD}║{Colors.RESET}")
    print(f"{Colors.BRIGHT_GREEN}{Colors.BOLD}╠{'═' * (box_width - 2)}╣{Colors.RESET}")
    print(f"{Colors.BRIGHT_GREEN}{Colors.BOLD}║{Colors.RESET} {Colors.BRIGHT_WHITE}{content.ljust(box_width - 4)}{Colors.RESET} {Colors.BRIGHT_GREEN}{Colors.BOLD}║{Colors.RESET}")
    print(f"{Colors.BRIGHT_GREEN}{Colors.BOLD}╚{'═' * (box_width - 2)}╝{Colors.RESET}\n")


def get_confidence_input(default: int = 100) -> int:
    """Get confidence score with enhanced visual validation."""
    while True:
        try:
            confidence_str = print_input_prompt(
                f"Confidence score {Colors.BRIGHT_BLUE}[0-100]{Colors.RESET} (default {Colors.BRIGHT_YELLOW}{default}{Colors.RESET})"
            )
            
            if not confidence_str:
                return default
            
            confidence = int(confidence_str)
            if 0 <= confidence <= 100:
                print_success(f"Confidence set to {confidence}%")
                return confidence
            else:
                print_error("Confidence must be between 0 and 100")
        except ValueError:
            print_error("Please enter a valid number")


def get_ip_input() -> str:
    """Get IP address with enhanced validation feedback."""
    from validators import validate_ip
    
    while True:
        ip = print_input_prompt("IP address (IPv4 or IPv6)")
        
        if validate_ip(ip):
            print_success(f"IP address valid: {ip}")
            return ip
        else:
            print_error(f"'{ip}' is not a valid IP address")


def get_categories_input() -> list[str]:
    """Get categories by selecting from ID list with enhanced visual display."""
    from categories import CATEGORIES, get_category_name
    
    print_section("SELECT ABUSE CATEGORIES")
    
    # Display all categories with enhanced styling
    header = f"{Colors.BRIGHT_CYAN}{Colors.BOLD}┌─────┬──────────────────────┬─────┬──────────────────────┐{Colors.RESET}"
    print(header)
    print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}│  ID │ Category{Colors.RESET}             {Colors.BRIGHT_CYAN}{Colors.BOLD}│  ID │ Category{Colors.RESET}             {Colors.BRIGHT_CYAN}{Colors.BOLD}│{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}├─────┼──────────────────────┼─────┼──────────────────────┤{Colors.RESET}")
    
    category_items = sorted(CATEGORIES.items())
    mid = len(category_items) // 2
    
    for i in range(mid):
        left_id, left_name = category_items[i]
        right_id, right_name = category_items[mid + i] if mid + i < len(category_items) else (None, None)
        
        left_str = f"{Colors.BRIGHT_YELLOW}{Colors.BOLD}{left_id:2}{Colors.RESET}  {Colors.BRIGHT_WHITE}{left_name:<18}{Colors.RESET}"
        if right_id:
            right_str = f"{Colors.BRIGHT_YELLOW}{Colors.BOLD}{right_id:2}{Colors.RESET}  {Colors.BRIGHT_WHITE}{right_name:<18}{Colors.RESET}"
            print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}│{Colors.RESET} {left_str} {Colors.BRIGHT_CYAN}{Colors.BOLD}│{Colors.RESET} {right_str} {Colors.BRIGHT_CYAN}{Colors.BOLD}│{Colors.RESET}")
        else:
            print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}│{Colors.RESET} {left_str} {Colors.BRIGHT_CYAN}{Colors.BOLD}│{Colors.RESET}      {' ' * 20} {Colors.BRIGHT_CYAN}{Colors.BOLD}│{Colors.RESET}")
    
    footer = f"{Colors.BRIGHT_CYAN}{Colors.BOLD}└─────┴──────────────────────┴─────┴──────────────────────┘{Colors.RESET}"
    print(footer)
    print()
    
    # Get category IDs from user
    while True:
        ids_str = print_input_prompt(
            "Select category IDs (comma-separated, e.g., 18,22)"
        )
        
        try:
            category_ids = [int(id_str.strip()) for id_str in ids_str.split(",")]
            
            # Validate all IDs
            invalid_ids = [cid for cid in category_ids if cid not in CATEGORIES]
            if invalid_ids:
                print_error(f"Invalid category IDs: {', '.join(str(cid) for cid in invalid_ids)}")
                continue
            
            # Get category names for the selected IDs
            category_names = [get_category_name(cid) for cid in category_ids]
            return category_names
            
        except ValueError:
            print_error("Please enter valid numbers separated by commas (e.g., 18,22)")


def get_comment_input() -> str:
    """Get comment with enhanced visual validation."""
    from validators import validate_comment
    
    while True:
        comment = print_input_prompt(
            "Comment/Description (up to 1000 characters)"
        )
        
        is_valid, error = validate_comment(comment)
        if is_valid:
            print_success(f"Comment received ({len(comment)} characters)")
            return comment
        else:
            print_error(error)
