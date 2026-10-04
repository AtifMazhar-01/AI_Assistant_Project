# AI Personal Assistant

A terminal-based AI personal assistant that can chat with you and perform actions using tool calls. The assistant can help with normal conversation as well as execute tasks like booking meetings, managing your todo list, booking flights, and placing orders.

## Features

- **Natural chat** – Talk with the assistant like a normal conversation
- **Meeting booking** – Book meetings with participants, dates, and times
- **Todo/task tracker** – Add, update, and list tasks with status tracking
- **Flight booking** – Simulate flight bookings to destinations
- **Order placement** – Place shopping orders for items with quantities
- **Configurable LLM provider** – Use Groq, Gemini, or OpenAI via `.env` settings
- **Conversation memory** – Assistant remembers earlier messages in the conversation

## Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd AI_Assistant_Project
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate       # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Copy the example environment file:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your API keys. At minimum you'll need:
     - `OPENAAI_API_KEY` (if using OpenAI) **or**
     - `GROQ_API_KEY` (if using Groq) **or**
     - `GEMINI_API_KEY` (if using Gemini)

   The `LLM_PROVIDER` variable controls which service to use (default: `groq`).
   Available options: `groq`, `gemini`, `openai`.

## Usage

Start the assistant:

```bash
python app.py
```

You'll see a welcome message and be prompted for input:

```
AI PERSONAL ASSISTANT
Type 'exit' or 'quit' to leave.

You: <your message>
```

### Available Actions

The assistant can help with normal conversation or invoke tools for specific actions:

| Tool | Required Parameters | Example |
|------|---------------------|---------|
| `book_meeting` | `participants`, `date`, `time` | `book_meeting(participants=["Alice","Bob"], date="2026-09-15", time="15:00")` |
| `add_task` | `task_name` | `add_task("Finish README")` |
| `update_task_status` | `task_name`, `status` | `update_task_status(task_name="Finish README", status="completed")` |
| `list_tasks` | (optional) `status` | `list_tasks(status="pending")` |
| `book_flight` | `destination`, `date`, `time` | `book_flight(destination="Delhi", date="2026-10-01", time="10:00")` |
| `place_order` | `items` (list of dicts with `name` and `quantity`) | `place_order(items=[{"name":"notebook","quantity":2}])` |

**Tips:**
- Type `exit` or `quit` to end the chat.
- The assistant remembers conversation context — you can follow up on previous actions (e.g., "mark that as completed").
- If the assistant asks for missing information, provide the requested details.

## Project Structure

```
AI_Assistant_Project/
├── app.py                 # Entry point — starts the terminal chat loop
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment variables
├── .gitignore             # Files excluded from version control
│
├── src/                   # Source modules
│   ├── __init__.py
│   ├── assistant.py       # Assistant logic — LLM + tool calling + memory
│   ├── llm.py             # LLM provider setup (Groq/Gemini/OpenAI)
│   ├── memory.py          # Simple conversation memory
│   └── tools.py           # All available tools (book_meeting, add_task, etc.)
│
├── data/                  # CSV data files (created at runtime)
│   ├── todo.csv
│   ├── meetings.csv
│   ├── flight_bookings.csv
│   └── orders.csv
│
└── prompts/
    └── assistant_prompt.txt  # System prompt for the assistant
```

## Configuration

### `.env` file

Copy `.env.example` to `.env` and modify as needed:

```env
# Which LLM provider to use: groq OR gemini (default: groq)
LLM_PROVIDER=groq

# OpenAI settings (used when LLM_PROVIDER=openai)
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini

# Gemini settings (used when LLM_PROVIDER=gemini)
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.0-flash

# Groq settings (used when LLM_PROVIDER=groq)
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=openai/gpt-oss-120b
```

## Dependencies

See `requirements.txt` for the full list. Key packages:

- `langchain>=0.3.0` — LLM framework
- `langchain-core>=0.3.0` — Core LangChain utilities
- `langchain-openai>=0.2.0` — OpenAI integration
- `langchain-google-genai>=2.0.0` — Google Gemini integration
- `langchain-groq>=0.0.0` — Groq integration
- `python-dotenv>=1.0.0` — Environment variable loading

## License

This project is for educational/demo purposes. Feel free to modify and use it as a starting point for your own AI assistant projects.