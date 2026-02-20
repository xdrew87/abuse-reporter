"""AbuseIPDB CLI tool for submitting abuse reports."""

import argparse
import os
import sys
import json
from typing import Optional
from pathlib import Path

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent / '.env')

from categories import validate_categories, get_category_id
from validators import (
    validate_ip,
    validate_confidence,
    validate_comment,
    validate_api_key
)
from client import AbuseIPDBClient
from ui import (
    print_banner,
    print_menu,
    print_section,
    print_success,
    print_error,
    print_warning,
    print_info,
    print_input_prompt,
    print_category_list,
    print_report_summary,
    print_box,
    print_exit_message,
    get_confidence_input,
    get_ip_input,
    get_categories_input,
    get_comment_input,
    Colors,
    clear_screen,
)


def parse_arguments() -> argparse.Namespace:
    """Parse and return command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Submit abuse reports to AbuseIPDB API v2",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --ip 192.168.1.1 --categories bruteforce,spam --comment "Suspicious activity"
  %(prog)s --ip 192.168.1.1 --categories bruteforce --confidence 75 --verbose
  %(prog)s --ip 192.168.1.1 --categories phishing --comment "Test" --dry-run
  %(prog)s --cli                                          (Interactive menu mode)
  %(prog)s --list-categories
        """
    )
    
    parser.add_argument(
        "--ip",
        type=str,
        help="IPv4 or IPv6 address to report"
    )
    
    parser.add_argument(
        "--categories",
        type=str,
        help="Comma-separated list of category names (e.g., 'bruteforce,spam,phishing')"
    )
    
    parser.add_argument(
        "--comment",
        type=str,
        help="Description of the abuse (up to 1000 characters)"
    )
    
    parser.add_argument(
        "--confidence",
        type=int,
        default=100,
        help="Confidence score 0-100 (default: 100)"
    )
    
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate inputs without submitting the report"
    )
    
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed output including API response JSON"
    )
    
    parser.add_argument(
        "--list-categories",
        action="store_true",
        help="List all available categories and exit"
    )
    
    parser.add_argument(
        "--cli",
        action="store_true",
        help="Launch interactive menu mode"
    )
    
    return parser.parse_args()


def validate_inputs(
    ip: Optional[str],
    categories_str: Optional[str],
    comment: Optional[str],
    confidence: int,
    verbose: bool
) -> tuple[bool, Optional[str], list[int]]:
    """
    Validate all input parameters.
    
    Returns:
        Tuple of (is_valid, error_message, category_ids)
    """
    # Validate IP
    if not ip:
        return False, "Error: --ip is required", []
    
    if not validate_ip(ip):
        return False, f"Error: Invalid IP address: {ip}", []
    
    if verbose:
        print(f"✓ IP address valid: {ip}")
    
    # Validate categories
    if not categories_str:
        return False, "Error: --categories is required", []
    
    category_names = [c.strip() for c in categories_str.split(",")]
    is_valid, category_ids, invalid_names = validate_categories(category_names)
    
    if not is_valid:
        return False, f"Error: Invalid categories: {', '.join(invalid_names)}", []
    
    if not category_ids:
        return False, "Error: At least one valid category is required", []
    
    if verbose:
        print(f"✓ Categories valid: {', '.join(category_names)}")
    
    # Validate comment
    if not comment:
        return False, "Error: --comment is required", []
    
    comment_valid, comment_error = validate_comment(comment)
    if not comment_valid:
        return False, f"Error: {comment_error}", []
    
    if verbose:
        print(f"✓ Comment valid ({len(comment)} characters)")
    
    # Validate confidence
    conf_valid, conf_error = validate_confidence(confidence)
    if not conf_valid:
        return False, f"Error: {conf_error}", []
    
    if verbose:
        print(f"✓ Confidence score valid: {confidence}")
    
    return True, None, category_ids


def bulk_report_interactive(dry_run: bool = False) -> int:
    """Interactive bulk report submission prompt."""
    print_section("BULK ABUSE REPORT")
    
    num_reports_str = print_input_prompt("How many reports would you like to submit? (1-100)")
    
    try:
        num_reports = int(num_reports_str)
        if num_reports < 1 or num_reports > 100:
            print_error("Please enter a number between 1 and 100")
            return 0
    except ValueError:
        print_error("Invalid number. Please try again.")
        return 0
    
    reports = []
    
    for i in range(num_reports):
        print()
        print_info(f"Report {i + 1}/{num_reports}")
        print("-" * 50)
        
        # Get IP
        ip = get_ip_input()
        print_success(f"IP address valid: {ip}")
        
        # Get categories
        categories_input = get_categories_input()
        is_valid, category_ids, _ = validate_categories(categories_input)
        print_success(f"Categories valid: {', '.join(categories_input)}")
        
        # Get comment
        comment = get_comment_input()
        print_success(f"Comment received ({len(comment)} characters)")
        
        # Get confidence
        confidence = get_confidence_input(100)
        print_success(f"Confidence set to {confidence}%")
        
        # Store report
        reports.append({
            "ip": ip,
            "categories": categories_input,
            "category_ids": category_ids,
            "comment": comment,
            "confidence": confidence
        })
        
        if i < num_reports - 1:
            print_input_prompt("Press Enter to continue to next report")
            clear_screen()
            print_banner()
    
    # Show summary of all reports
    print()
    print_section("BULK REPORT SUMMARY")
    for idx, report in enumerate(reports, 1):
        print(f"{Colors.BRIGHT_YELLOW}Report {idx}:{Colors.RESET}")
        print_report_summary(
            report["ip"],
            report["categories"],
            report["comment"],
            report["confidence"],
            verbose=False
        )
        print()
    
    # Confirm submission
    if not dry_run:
        confirm = print_input_prompt(f"Submit all {num_reports} reports? (yes/no)").lower()
        if confirm not in ["yes", "y"]:
            print_warning("Bulk report cancelled")
            return 0
        
        # Submit all reports
        api_key = os.getenv("ABUSEIPDB_API_KEY")
        key_valid, key_error = validate_api_key(api_key)
        if not key_valid:
            print_error(key_error)
            return 1
        
        client = AbuseIPDBClient(api_key)
        successful = 0
        failed = 0
        
        for idx, report in enumerate(reports, 1):
            result = client.submit_report(
                ip=report["ip"],
                category_ids=report["category_ids"],
                comment=report["comment"],
                confidence=report["confidence"]
            )
            
            if result.success:
                print_success(f"Report {idx}: {report['ip']} submitted successfully")
                successful += 1
            else:
                print_error(f"Report {idx}: {report['ip']} failed ({result.message})")
                failed += 1
        
        print()
        print_section("BULK SUBMISSION COMPLETE")
        print_success(f"Successful: {successful}/{num_reports}")
        if failed > 0:
            print_error(f"Failed: {failed}/{num_reports}")
    else:
        print_success("Bulk report validation completed successfully")
        print_info("Use without --dry-run to submit the reports")
    
    return 0


def submit_report_interactive(dry_run: bool = False) -> int:
    """Interactive report submission prompt."""
    print_section("SUBMIT ABUSE REPORT")
    
    # Get IP
    ip = get_ip_input()
    print_success(f"IP address valid: {ip}")
    
    # Get categories
    categories_input = get_categories_input()
    is_valid, category_ids, _ = validate_categories(categories_input)
    print_success(f"Categories valid: {', '.join(categories_input)}")
    
    # Get comment
    comment = get_comment_input()
    print_success(f"Comment received ({len(comment)} characters)")
    
    # Get confidence
    confidence = get_confidence_input(100)
    print_success(f"Confidence set to {confidence}%")
    
    # Show summary
    print_report_summary(ip, categories_input, comment, confidence, verbose=True)
    
    # Confirm submission
    if not dry_run:
        confirm = print_input_prompt("Submit report? (yes/no)").lower()
        if confirm not in ["yes", "y"]:
            print_warning("Report cancelled")
            return 0
    else:
        print_box("DRY-RUN MODE", "Validation completed successfully (no report submitted)")
        return 0
    
    # Check API key
    api_key = os.getenv("ABUSEIPDB_API_KEY")
    key_valid, key_error = validate_api_key(api_key)
    if not key_valid:
        print_error(key_error)
        print_info("Set your API key:")
        print(f"  {Colors.DIM}export ABUSEIPDB_API_KEY='your_key_here'{Colors.RESET}")
        return 1
    
    # Submit report
    print_section("SUBMITTING REPORT")
    print_info("Sending request to AbuseIPDB...")
    
    client = AbuseIPDBClient(api_key)
    result = client.submit_report(
        ip=ip,
        category_ids=category_ids,
        comment=comment,
        confidence=confidence
    )
    
    if result.success:
        print_box("SUCCESS", "Report submitted successfully!")
        if result.response_data:
            print_info("Response data:")
            print(json.dumps(result.response_data, indent=2))
        return 0
    else:
        print_error(f"{result.message}")
        if result.error:
            print_error(f"Details: {result.error}")
        if result.response_data:
            print(json.dumps(result.response_data, indent=2))
        return 1


def run_interactive_menu() -> int:
    """Run the interactive menu mode."""
    clear_screen()
    print_banner()
    
    api_key = os.getenv("ABUSEIPDB_API_KEY")
    if not api_key:
        print_warning("ABUSEIPDB_API_KEY environment variable not set")
        print_info("Set it with: export ABUSEIPDB_API_KEY='your_key_here'")
        print()
    
    while True:
        print_menu()
        choice = print_input_prompt("Select an option").strip()
        
        if choice == "1":
            clear_screen()
            print_banner()
            submit_report_interactive(dry_run=False)
            print_input_prompt("\nPress Enter to continue")
            clear_screen()
            print_banner()
        
        elif choice == "2":
            clear_screen()
            print_banner()
            print_category_list()
            print_input_prompt("Press Enter to continue")
            clear_screen()
            print_banner()
        
        elif choice == "3":
            clear_screen()
            print_banner()
            submit_report_interactive(dry_run=True)
            print_input_prompt("\nPress Enter to continue")
            clear_screen()
            print_banner()
        
        elif choice == "4":
            clear_screen()
            print_banner()
            bulk_report_interactive(dry_run=False)
            print_input_prompt("\nPress Enter to continue")
            clear_screen()
            print_banner()
        
        elif choice == "0":
            clear_screen()
            print_banner()
            print_exit_message()
            return 0
        
        else:
            print_error("Invalid option. Please try again.")
            print()


def main() -> int:
    """Main entry point."""
    args = parse_arguments()
    
    # Handle list-categories flag
    if args.list_categories:
        clear_screen()
        print_banner()
        print_category_list()
        return 0
    
    # Handle interactive mode
    if args.cli or (len(sys.argv) == 1):
        return run_interactive_menu()
    
    # Command-line mode with arguments
    if not args.ip and not args.cli:
        parser = argparse.ArgumentParser(
            description="Submit abuse reports to AbuseIPDB API v2"
        )
        parser.print_help()
        return 0
    
    # Validate inputs
    is_valid, error_msg, category_ids = validate_inputs(
        args.ip,
        args.categories,
        args.comment,
        args.confidence,
        args.verbose
    )
    
    if not is_valid:
        print_error(error_msg)
        return 1
    
    # Dry-run mode
    if args.dry_run:
        if args.verbose:
            print_section("DRY-RUN MODE")
            print_success("Report validation completed successfully")
            print_info("Use without --dry-run to submit the report")
        else:
            print_success("Report validation passed (dry-run mode)")
        return 0
    
    # Validate API key
    api_key = os.getenv("ABUSEIPDB_API_KEY")
    key_valid, key_error = validate_api_key(api_key)
    if not key_valid:
        print_error(key_error)
        print_info("Set the API key with:")
        print(f"  {Colors.DIM}export ABUSEIPDB_API_KEY='your_api_key_here'{Colors.RESET}")
        return 1
    
    # Create client and submit report
    if args.verbose:
        print_section("SUBMITTING REPORT")
    
    client = AbuseIPDBClient(api_key)
    result = client.submit_report(
        ip=args.ip,
        category_ids=category_ids,
        comment=args.comment,
        confidence=args.confidence
    )
    
    # Display results
    if result.success:
        print_success("Report submitted successfully")
        
        if args.verbose and result.response_data:
            print("\nResponse JSON:")
            print(json.dumps(result.response_data, indent=2))
        
        return 0
    else:
        print_error(f"{result.message}")
        if result.error:
            print_error(f"Details: {result.error}")
        
        if args.verbose and result.response_data:
            print("\nResponse JSON:")
            print(json.dumps(result.response_data, indent=2))
        
        return 1


if __name__ == "__main__":
    sys.exit(main())
