# EPSS MCP Project


The EPSS MCP Project is a powerful server designed to retrieve CVE details from the NVD API and fetch EPSS scores from the EPSS server. It provides users with comprehensive vulnerability information, including CVE descriptions, CWEs, CVSS scores, and EPSS percentiles, all in one place.

## Features

- **Comprehensive CVE Information**: Fetch detailed vulnerability data, including descriptions, CWEs, and CVSS scores, directly from the NVD API.
- **EPSS Integration**: Retrieve EPSS scores and percentiles to assess the likelihood of exploitation for specific vulnerabilities.
- **MCP Server**: Serve data through a robust and extensible MCP server for seamless integration with other tools.
- **Docker Support**: Easily deploy the server using Docker for a consistent and portable runtime environment.
- **VS Code Compatibility**: Integrate with VS Code MCP for enhanced developer workflows and real-time vulnerability insights.

## Prerequisites

- Python 3.13 or higher
- Docker (optional, for containerized deployment)
- An NVD API key (add it to the `.env` file as `NVD_API_KEY`)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd epss-mcp-project
```

### 2. Install Dependencies

It is recommended to use a virtual environment. You can create one using `venv` or `conda`. Then, install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Add Your NVD API Key

Create a `.env` file in the project root and add your NVD API key:

```env
NVD_API_KEY=your-nvd-api-key
```

## Usage

### Installing via Smithery

To install EPSS Vulnerability Scoring Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@jgamblin/EPSS-MCP):

```bash
npx -y @smithery/cli install @jgamblin/EPSS-MCP --client claude
```

### Running the MCP Server Locally

To start the MCP server locally, run:

```bash
python epss_mcp.py
```

Once the server is running, you can make requests to retrieve CVE details by specifying the CVE ID.

### Example Request

To get details for a specific CVE, use the following format:

```
GET /cve/<CVE-ID>
```

Replace `<CVE-ID>` with the actual CVE identifier (e.g., `CVE-2022-1234`).

## Docker Deployment (for Open-WebUI)

If you want to run the MCP server in Open-WebUI, follow these steps:

### 1. Build the Docker Image

To build the Docker container, run:

```bash
docker build -t epss_mcp .
```

### 2. Run the Docker Container

Run the container and expose it on port `8000`:

```bash
docker run -p 8000:8000 epss_mcp
```

The MCP server will now be accessible at `http://localhost:8000`.

### WebUI Screenshot

Below is a screenshot of the MCP server running in the Open-WebUI:

![EPSS MCP WebUI Screenshot](epss_mcp_webui.png)

### Suggested System Prompt for WebUI

When using the MCP server in Open-WebUI, you can configure the following system prompt to guide interactions:

```text
You are a specialized AI Assistant focused on the Exploit Prediction Scoring System (EPSS). Your expertise lies in delivering and interpreting EPSS data, which includes daily updated probability scores (0-1) and percentiles for Common Vulnerabilities and Exposures (CVEs), indicating the likelihood of their exploitation in the wild within the next 30 days. You are to help cybersecurity professionals understand these predictions, compare them with other metrics like CVSS scores, and use this information to prioritize vulnerability remediation efforts effectively. Provide actionable, data-driven insights in a clear, technically accurate, professional, and solution-oriented manner.
```

## Serving to VS Code MCP

To serve the MCP server to VS Code MCP, follow these steps:

1. **Add the Local Server to VS Code**:
   Open your VS Code `settings.json` file and add the following configuration to register the local server:

   ```json
   "mcp.servers": {
       "EPSS_MCP": {
           "type": "stdio",
           "command": "python",
           "args": [
               "/Github/EPSS-MCP/epss_mcp.py"
           ]
       }
   }
   ```

   **Note**: Make sure to update the `args` path to match the location of the `epss_mcp.py` file on your local machine.

2. **Connect to VS Code**:
   - Open VS Code.
   - Install the [Microsoft Copilot Labs](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-labs) extension if not already installed.
   - Ensure the MCP server is listed and active in the extension.

3. **Start Using the MCP Server**:
   Once connected, VS Code will call the Python file directly to fetch CVE details and EPSS scores.

### VS Code Screenshot

Below is a screenshot of the MCP server integrated with VS Code:

![EPSS MCP VS Code Screenshot](epss_mcp_vscode.png)

## Project Structure

```
epss-mcp-project
├── epss_mcp.py               # Main entry point for the MCP server
├── nvd_api.py                # Functions to interact with the NVD API
├── epss_api.py               # Functions to interact with the EPSS API
├── epss_mcp_test.py          # Test script for the MCP server
├── requirements.txt          # Project dependencies
├── Dockerfile                # Docker configuration
├── .env                      # Environment variables (e.g., API keys)
└── README.md                 # Project documentation
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

[![smithery badge](https://smithery.ai/badge/@jgamblin/EPSS-MCP)](https://smithery.ai/server/@jgamblin/EPSS-MCP)
