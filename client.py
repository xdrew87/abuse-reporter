"""AbuseIPDB API client."""

import json
import requests
from typing import Optional, Dict, Any
from dataclasses import dataclass


API_ENDPOINT = "https://api.abuseipdb.com/api/v2/report"
API_TIMEOUT = 15


@dataclass
class ReportResult:
    """Represents the result of a report submission."""
    success: bool
    message: str
    status_code: Optional[int] = None
    response_data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None


class AbuseIPDBClient:
    """Client for interacting with AbuseIPDB API v2."""
    
    def __init__(self, api_key: str):
        """
        Initialize the AbuseIPDB client.
        
        Args:
            api_key: The AbuseIPDB API key
        """
        self.api_key = api_key
        self.headers = {
            "Key": api_key,
            "Accept": "application/json"
        }
    
    def submit_report(
        self,
        ip: str,
        category_ids: list[int],
        comment: str,
        confidence: int = 100
    ) -> ReportResult:
        """
        Submit an abuse report to AbuseIPDB.
        
        Args:
            ip: The IP address to report
            category_ids: List of numeric category IDs
            comment: Report comment/description
            confidence: Confidence score (0-100, default 100)
            
        Returns:
            ReportResult object containing the outcome
        """
        try:
            data = {
                "ip": ip,
                "categories": ",".join(str(cid) for cid in category_ids),
                "comment": comment,
                "confidence": confidence
            }
            
            response = requests.post(
                API_ENDPOINT,
                headers=self.headers,
                data=data,
                timeout=API_TIMEOUT
            )
            
            return self._handle_response(response)
            
        except requests.exceptions.Timeout:
            return ReportResult(
                success=False,
                message="Request timed out",
                error="The API request exceeded 15 seconds"
            )
        except requests.exceptions.ConnectionError as e:
            return ReportResult(
                success=False,
                message="Connection error",
                error=str(e)
            )
        except requests.exceptions.RequestException as e:
            return ReportResult(
                success=False,
                message="Request failed",
                error=str(e)
            )
        except Exception as e:
            return ReportResult(
                success=False,
                message="Unexpected error",
                error=str(e)
            )
    
    def _handle_response(self, response: requests.Response) -> ReportResult:
        """
        Handle and parse the API response.
        
        Args:
            response: The requests Response object
            
        Returns:
            ReportResult object
        """
        status_code = response.status_code
        
        try:
            response_data = response.json()
        except json.JSONDecodeError:
            return ReportResult(
                success=False,
                message="Failed to parse API response",
                status_code=status_code,
                error="Invalid JSON in response body"
            )
        
        # Success responses - check for 200/201 status AND presence of data
        if status_code in [200, 201] and "data" in response_data:
            return ReportResult(
                success=True,
                message="Report submitted successfully",
                status_code=status_code,
                response_data=response_data
            )
        
        # 400 Bad Request
        if status_code == 400:
            error_msg = response_data.get("errors", [{}])[0].get("detail", "Bad request")
            return ReportResult(
                success=False,
                message="Bad request",
                status_code=status_code,
                response_data=response_data,
                error=error_msg
            )
        
        # 401 Unauthorized / Invalid key
        if status_code == 401:
            return ReportResult(
                success=False,
                message="Authentication failed",
                status_code=status_code,
                response_data=response_data,
                error="Invalid API key"
            )
        
        # 429 Rate limit
        if status_code == 429:
            return ReportResult(
                success=False,
                message="Rate limit exceeded",
                status_code=status_code,
                response_data=response_data,
                error="Too many requests - please wait before trying again"
            )
        
        # 500+ Server errors
        if status_code >= 500:
            return ReportResult(
                success=False,
                message="Server error",
                status_code=status_code,
                response_data=response_data,
                error="AbuseIPDB API server error"
            )
        
        # Other errors
        error_msg = response_data.get("errors", [{}])[0].get("detail", "Unknown error")
        return ReportResult(
            success=False,
            message="API error",
            status_code=status_code,
            response_data=response_data,
            error=error_msg
        )
