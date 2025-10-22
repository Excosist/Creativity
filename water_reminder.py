import asyncio
import json
from mcp.server.models import InitializationOptions
import mcp.types as types
from mcp.server import NotificationOptions, Server
import mcp.server.stdio
from win11toast import toast
from datetime import datetime
import time
import threading

reminder_active = False
reminder_thread = None

app = Server("water-reminder")

def water_reminder_loop():
    """The main water reminder loop that runs in a separate thread"""
    global reminder_active
    
    while reminder_active:
        if not reminder_active:
            break
            
        f = toast('Hi', 'Did you drink water?', buttons=["Yes", "No"])

        if f.get("arguments") == 'http:Yes':
            now = datetime.now()
            current_date = now.date()
            current_time = now.time()
            print(f"yes at {current_date} {current_time}")
            toast('😊', 'Keep it up!')

        elif f.get("arguments") == 'http:No':
            now = datetime.now()
            current_date = now.date()
            current_time = now.time()
            print(f"no at {current_date} {current_time}")
            toast('😤', 'Do it next time!!')
        
        # Check every second if we should stop, but only remind every 30 minutes
        for _ in range(1800):
            if not reminder_active:
                return
            time.sleep(1)

@app.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available tools"""
    return [
        types.Tool(
            name="start_water_reminder",
            description="Start the water drinking reminder notifications",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        types.Tool(
            name="stop_water_reminder", 
            description="Stop the water drinking reminder notifications",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        types.Tool(
            name="reminder_status",
            description="Check if the water reminder is currently running",
            inputSchema={
                "type": "object", 
                "properties": {},
                "required": []
            },
        )
    ]

@app.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[types.TextContent]:
    """Handle tool calls"""
    global reminder_active, reminder_thread
    
    if name == "start_water_reminder":
        if reminder_active:
            return [types.TextContent(
                type="text",
                text="Water reminder is already running!"
            )]
        
        reminder_active = True
        reminder_thread = threading.Thread(target=water_reminder_loop, daemon=True)
        reminder_thread.start()
        
        return [types.TextContent(
            type="text", 
            text="Water reminder started! You'll get notifications every 30 minutes."
        )]
    
    elif name == "stop_water_reminder":
        if not reminder_active:
            return [types.TextContent(
                type="text",
                text="Water reminder is not currently running."
            )]
        
        reminder_active = False
        if reminder_thread:
            reminder_thread.join(timeout=2)
        
        return [types.TextContent(
            type="text",
            text="Water reminder stopped!"
        )]
    
    elif name == "reminder_status":
        status = "running" if reminder_active else "stopped"
        return [types.TextContent(
            type="text",
            text=f"Water reminder is currently {status}."
        )]
    
    else:
        raise ValueError(f"Unknown tool: {name}")

async def main():
    # Run the server using stdin/stdout streams
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="water-reminder",
                server_version="0.1.0",
                capabilities=app.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    asyncio.run(main())