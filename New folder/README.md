# MCP Chatbot

A simple chatbot that queries Firecrawl MCP and summarizes answers using OpenAI GPT-4, built with Flask.

## Setup

1. Clone this repo and navigate to the folder.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set your OpenAI API key as an environment variable:
   - On Windows (CMD):
     ```
     set OPENAI_API_KEY=your_openai_key_here
     ```
   - On PowerShell:
     ```
     $env:OPENAI_API_KEY="your_openai_key_here"
     ```
   - On Mac/Linux:
     ```
     export OPENAI_API_KEY=your_openai_key_here
     ```
4. Run the app:
   ```
   python app.py
   ```
5. Open your browser to http://127.0.0.1:5000

## How it works
- Enter a question in plain English.
- The app queries Firecrawl MCP and summarizes the result using OpenAI GPT-4.
- The answer is displayed in the web UI.

## Customize
- You can swap Firecrawl MCP for another MCP server by editing the API URL in `app.py`. 