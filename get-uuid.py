import uuid
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("uuid")

@mcp.tool()
async def get_uuid() -> str:
    return uuid.uuid4()

@mcp.tool()
async def get_multiple_uuids(count: int = 1) -> list[str]:
    if count <= 0:
        raise ValueError("count must be greater than or equal to 1")
    if count > 100:
        raise ValueError("count must be less than or equal to 100")
    return [str(uuid.uuid4()) for _ in range(count)]

if __name__ == "__main__":
    mcp.run(transport='stdio')