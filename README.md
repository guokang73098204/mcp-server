# AI Sticky Notes MCP Server

A Model Context Protocol (MCP) server that provides AI-powered sticky note functionality. This server allows AI assistants to create, read, and manage persistent notes through a simple file-based system.

## Features

- **Add Notes**: Append new notes to a persistent file
- **Read Notes**: Retrieve all saved notes
- **Latest Note Resource**: Access the most recently added note via MCP resources
- **Note Summary Prompt**: Generate prompts for AI to summarize current notes

## Tools

### `add_note(message: str)`
Appends a new note to the sticky note file.

**Parameters:**
- `message` (str): The note content to be added

**Returns:**
- Confirmation message indicating the note was saved

### `read_notes()`
Reads and returns all notes from the sticky note file.

**Returns:**
- All notes as a single string separated by line breaks
- "no notes yet" if no notes exist

## Resources

### `notes://latest`
Returns the most recently added note.

## Prompts

### `note_summary_prompt()`
Generates a prompt for AI to summarize all current notes.

## Installation

### Prerequisites
- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Using uv (Recommended)

```bash
# Install dependencies
uv sync

# Run the server
uv run mcp install main.py
```

### Using pip

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
python main.py
```

## Configuration

The server stores notes in a `notes.txt` file in the same directory as `main.py`. The file is automatically created on first use.

## Usage with Claude Desktop

To use this MCP server with Claude Desktop, add the following to your Claude Desktop configuration file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "ai-sticky-notes": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\Study\\opensource\\my-project\\mcp-server",
        "run",
        "main.py"
      ]
    }
  }
}
```

Replace the path with your actual project directory.

## Development

### Project Structure

```
mcp-server/
├── main.py           # MCP server implementation
├── notes.txt         # Persistent note storage
├── pyproject.toml    # Project dependencies
└── README.md         # This file
```

### Dependencies

- `mcp[cli]>=1.21.0` - Model Context Protocol implementation

## License

[Add your license here]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

[guokang73098204](https://github.com/guokang73098204)
