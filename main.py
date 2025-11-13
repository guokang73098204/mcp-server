# # server.py
# from mcp.server.fastmcp import FastMCP

# # create an MCP server
# mcp = FastMCP("AI Sticky Notes")

# # add an additional tool
# @mcp.tool()
# def add(a: int, b: int) -> int:
#     return a + b

#  # add a dynamic greeting resource
# @mcp.resource("greeting://{name}")
# def get_greeting(name: str) -> str:
#     """get a personalized greeting"""
#     return f"hello, {name}!"

from mcp.server.fastmcp import FastMCP
import os

# create an MCP server
mcp = FastMCP("AI Sticky Notes")

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.txt")

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")

@mcp.tool()
def add_note(message: str) -> str:
    """
    Append a new note to the sticky note file

    Args:
        message (str): THe note content to be added.

    Returns:
        str: confirmation message indicating the note was saved

    """
    ensure_file()
    with open(NOTES_FILE, "a") as f:
        f.write(message + "\n")
    return f"note saved!"

@mcp.tool()
def read_notes() -> str:
    """
    Read and retrun all notes from the sticky note file

    Returns:
        str: All notes as a single string seperatd by line breaks
             if no notes exist, a default confirmation message indicating the note was saved

    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    return content or "no notes yet"

@mcp.resource("notes://latest")
def get_latest_note() -> str:
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "no notes yet."
    
@mcp.prompt()
def note_summary_prompt() -> str:
    """
    generate prmpt

    Returns:
        str: A prompt string

    """    
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    if not content:
            return "ther are no notes yet"
    return f"summarize the current notes: {content}"