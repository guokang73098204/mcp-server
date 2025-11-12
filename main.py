# server.py
from mcp.server.fastmcp import FastMCP

# create an MCP server
mcp = FastMCP("AI Sticky Notes")

# add an additional tool
@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

 # add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """get a personalized greeting"""
    return f"hello, {name}!"