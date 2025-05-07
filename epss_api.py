from typing import Any, Dict
import httpx

# Constants
EPSS_API_BASE = "https://api.first.org/data/v1/epss?cve="

async def fetch_epss_data(cve_id: str) -> Dict[str, Any] | None:
    """Fetch the EPSS percentile and score for a given CVE ID."""
    url = f"{EPSS_API_BASE}{cve_id}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=30.0)
            response.raise_for_status()
            data = response.json()

            # Validate the JSON structure
            if not isinstance(data, dict) or "data" not in data or not data["data"]:
                return {"epss_percentile": "N/A", "epss_score": "N/A"}

            epss_data = data["data"][0]
            return {
                "epss_percentile": epss_data.get("percentile", "N/A"),
                "epss_score": epss_data.get("epss", "N/A")
            }
        except httpx.RequestError:
            pass
        except httpx.HTTPStatusError:
            pass
        except ValueError:
            pass
        except Exception:
            pass
        return {"epss_percentile": "N/A", "epss_score": "N/A"}