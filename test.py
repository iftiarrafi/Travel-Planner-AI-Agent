import asyncio
from mcp_client import get_all_tools , tavily_mcp_search

if __name__ == "__main__":
    mcp_tools = asyncio.run(get_all_tools())
    for tool in mcp_tools :
        print(tool.name)
    
    # query = "Latest developments in Agentic AI"
    # res = asyncio.run(tavily_mcp_search(query=query))
    # print(res)