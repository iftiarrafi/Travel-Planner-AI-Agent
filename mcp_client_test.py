import os
import certifi
import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient
from dotenv import load_dotenv

load_dotenv()

os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
AVIATIONSTACK_API_KEY = os.getenv("TAVILY_API_KEY")

client = MultiServerMCPClient(
    {
        "tavily": {
            "transport": "streamable_http",
            "url": f"https://mcp.tavily.com/mcp/?tavilyApiKey={TAVILY_API_KEY}"
        }
    }
)

async def get_all_tools():
    tools = await client.get_tools()

    print("MCP Tools:\n")

    for tool in tools:
        print(tool.name)

    return tools


tavily_search_tool = None

async def get_tavily_search_tool():
    global tavily_search_tool

    if tavily_search_tool is not None:
        return tavily_search_tool

    tools = await client.get_tools()

    tavily_search_tool = next(
        tool for tool in tools
        if tool.name == "tavily_search"
    )

    return tavily_search_tool


async def tavily_mcp_search(query: str):
    tool = await get_tavily_search_tool()

    result = await tool.ainvoke({
        "query": query
    })

    return result
