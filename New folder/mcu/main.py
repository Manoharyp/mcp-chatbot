import os
import asyncio
from google import genai
from google.genai import types
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import requests

async def run_session():
    print("✅ MCP Gemini + Flight Search Started")

    gemini_api_key = os.getenv("GEMINI_API_KEY")
    serp_api_key = os.getenv("SERP_API_KEY")
    if not gemini_api_key or not serp_api_key:
        print("❌ Error: GEMINI_API_KEY or SERP_API_KEY not set in environment")
        return

    try:
        client = genai.Client(api_key=gemini_api_key)

        server_params = StdioServerParameters(
            command="mcp-flight-search",
            args=["--connection_type", "stdio"],
            env={"SERP_API_KEY": serp_api_key},
        )

        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                print("🔗 MCP Server Connected")
                await session.initialize()
                tools_info = await session.list_tools()

                if not tools_info or not tools_info.tools:
                    print("⚠️ Warning: No tools available from MCP server")
                    return

                tools = [
                    types.Tool(
                        function_declarations=[
                            {
                                "name": tool.name,
                                "description": tool.description,
                                "parameters": {
                                    k: v for k, v in tool.inputSchema.items()
                                    if k not in ["$schema", "additionalProperties"]
                                },
                            }
                        ]
                    )
                    for tool in tools_info.tools
                ]

                return client, session, tools

    except Exception as e:
        print(f"❌ Error: Failed to initialize MCP session or Gemini client - {str(e)}")
        return None, None, None

def get_user_input():
    while True:
        prompt = input("You: ")
        if prompt.lower() in ["exit", "quit"]:
            return None
        return prompt

async def main():
    client, session, tools = await run_session()
    if client is None or session is None or tools is None:
        return

    while True:
        prompt = get_user_input()
        if prompt is None:
            break

        try:
            response = client.models.generate_content(
                model="gemini-1.5-pro-latest",
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.2,
                    tools=tools
                )
            )

            function_call = response.candidates[0].content.parts[0].function_call
            print("🔧 Gemini Function:", function_call.name)
            print("📦 Params:", function_call.args)

            result = await session.call_tool(function_call.name, arguments=function_call.args)
            print("🛫 Result:", result)

        except Exception as e:
            print(f"❌ Error: {str(e)}")
            continue

def query_firecrawl(query):
    payload = {"query": query}
    response = requests.post("https://app.firecrawl.dev/api/mcp/query", json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}

if __name__ == "__main__":
    asyncio.run(main())