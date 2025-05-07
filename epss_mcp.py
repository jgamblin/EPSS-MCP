from typing import Any, Dict
import httpx
from mcp.server.fastmcp import FastMCP
from nvd_api import fetch_cve_details
from epss_api import fetch_epss_data
import logging


# Initialize FastMCP server
mcp = FastMCP("EPSS-MCP")

@mcp.tool()
async def get_cve_info(cve_id: str) -> str:
    """Get CVE information including description, CWE, CVSS score, and EPSS data.

    Args:
        cve_id: The CVE ID to fetch (e.g., CVE-2022-0087)
    """
    logging.debug(f"Fetching CVE information for: {cve_id}")

    nvd_data = await fetch_cve_details(cve_id)
    logging.debug(f"NVD Data: {nvd_data}")

    epss_data = await fetch_epss_data(cve_id)
    logging.debug(f"EPSS Data: {epss_data}")

    if not nvd_data:
        return f"Unable to fetch CVE details for {cve_id}. Please check the CVE ID or try again later."

    description = nvd_data.get("description", "No description available")
    cwe = nvd_data.get("cwe", "N/A")
    cvss_score = nvd_data.get("cvss_score", "N/A")
    epss_percentile = f"{float(epss_data.get('epss_percentile', 0)) * 100:.2f}%" if epss_data.get("epss_percentile") != "N/A" else "N/A"
    epss_score = f"{float(epss_data.get('epss_score', 0)):.4f}" if epss_data.get("epss_score") != "N/A" else "N/A"

    response = f"""
CVE ID: {cve_id}
Description: {description}
CWE: {cwe}
CVSS Score: {cvss_score}
EPSS Percentile: {epss_percentile}
EPSS Score: {epss_score}
"""
    return response

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")