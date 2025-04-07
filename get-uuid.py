import uuid
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("uuid")

@mcp.tool()
async def get_uuid() -> str:
    return uuid.uuid4()

if __name__ == "__main__":
    mcp.run(transport='stdio')