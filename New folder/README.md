# MCP Chatbot with Gemini & Firecrawl

## Overview
This project is a working chatbot interface that connects to an MCP (Model Context Protocol) server and/or Gemini LLM. It demonstrates how user input is mapped to an MCP query and returns a summarized, human-readable response.

---

## Demo
- **Video Demo:** [https://drive.google.com/drive/folders/1amy09n-A5cxREAxWUebCivBv4NwCPuSv?fbclid=PAZXh0bgNhZW0CMTEAAabCQwGlAtU01KS1aQYmTYJc7rGxj1ka5yAfdAkV0oKeJkWtH6tPXSOFiu0_aem_HFxp9mS9P4k0Uocf96BW3g]

- **Local Demo:**
  1. Run the Flask app as described below.
  2. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.
  3. Enter a question and see the chatbot's response.

---

## MCP Server Connection
- This project connects to the public Firecrawl MCP server (`https://app.firecrawl.dev/api/mcp/query`) for structured data queries.
- It also supports Gemini LLM for natural language answers.

---

## How It Works: User Input → MCP Query → Response
1. **User Input:**
   - The user enters a question in plain English via the web interface or API.
2. **MCP Query:**
   - The backend maps the question to an MCP-compatible query (for Firecrawl, it sends the question as a JSON payload to the REST endpoint).
   - For Gemini, the question is sent to the Gemini LLM for a direct answer.
3. **Response:**
   - The response from the MCP server (or Gemini) is summarized and returned to the user in a human-readable format (HTML or JSON).

---

## Setup & Usage

### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/your-mcp-chatbot-repo.git
cd your-mcp-chatbot-repo
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. (If using Gemini) Set your API key in `app.py` or as an environment variable.

### 4. Run the App
```sh
python app.py
```

### 5. Test the Chatbot
- Open your browser to [http://127.0.0.1:5000](http://127.0.0.1:5000)
- Or, send a POST request to `/` with JSON:
  ```sh
  curl -X POST -H "Content-Type: application/json" -d '{"question": "What is AI?"}' http://127.0.0.1:5000/
  ```

---

## File Structure
- `app.py` — Flask app, chatbot logic, Gemini integration
- `templates/index.html` — Web UI
- `requirements.txt` — Python dependencies
- `README.md` — This file

---

## Customization
- You can swap Firecrawl for another MCP server by changing the endpoint in the code.
- To use only Gemini, comment out the MCP logic and use the Gemini LLM for all responses.

---

## License
[MIT License] 
