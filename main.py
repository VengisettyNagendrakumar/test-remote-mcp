from fastmcp import FastMCP
import random 
import json 

#create the mcp server instance
mcp = FastMCP("simple calculator")

@mcp.tool 
def add(a: int, b: int) -> int:
    """Add two numbers together.
    Args:
        a (int): The first number.
        b (int): The second number.
    Returns:
        int: The sum of the two numbers.
        
    """
    
    return a + b


#generate a random number
@mcp.tool
def random_number(min_value: int=1, max_value: int=100) -> int:
    """Generate a random number between min_value and max_value.
    Args:
        min_value (int): The minimum value of the random number.
        max_value (int): The maximum value of the random number.
    Returns:
        int: A random number between min_value and max_value.
    """
    return random.randint(min_value, max_value)

@mcp.resource("info://server")
def server_info()->str:
    """Get information about the server.
    Returns:
        str: A JSON string containing information about the server.
    """
    info = {
        "name": "simple calculator server",
        "version":"1.0",
        "description": "basic server with math tools",
        "tools": ["add", "random_number"],
        "author": "Nagendra",
    }
  
    return json.dumps(info,indent=2)

if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)