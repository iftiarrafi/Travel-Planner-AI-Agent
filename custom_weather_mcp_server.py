from mcp.server.fastmcp import FastMCP
import requests
import os
from dotenv import load_dotenv
load_dotenv()

mcp = FastMCP("Weather MCP Server")

@mcp.tool()
def get_current_weather():
    return "good"


@mcp.tool()
def get_forecast():
    return "good forcast"


if __name__ == "__main__":
    mcp.run(transport="stdio")
