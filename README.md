# LangChain Gemini Project

A LangChain-based project featuring a FastAPI server and a Streamlit chatbot application, both powered by Google's Gemini AI model.

## Project Structure

```
langchain1/
├── api/
│   └── api.py          # FastAPI server with LangServe routes
├── chatbot/
│   └── app.py          # Streamlit chatbot application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Features

- **FastAPI Server**: RESTful API endpoints for interacting with Google Gemini AI
  - `/google_genai`: Direct access to the Gemini model
  - `/essay`: Generate essays on any topic (100 words)

- **Streamlit Chatbot**: Interactive web-based chatbot interface
  - User-friendly chat interface
  - Real-time responses from Gemini AI
  - LangSmith tracing support (optional)

## Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- (Optional) LangSmith API key for tracing

## Installation

1. Clone or navigate to this repository:
   ```bash
   cd langchain1
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with your API keys:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   LANGSMITH_API_KEY=your_langsmith_api_key_here  # Optional
   ```

## Usage

### Running the FastAPI Server

Navigate to the `api` directory and run:
```bash
cd api
python api.py
```

The server will start on `http://localhost:8000`

**Available Endpoints:**
- `POST /google_genai/invoke` - Direct model invocation
- `POST /essay/invoke` - Generate an essay (requires `topic` parameter)

**Example API Request:**
```bash
curl -X POST "http://localhost:8000/essay/invoke" \
  -H "Content-Type: application/json" \
  -d '{"input": {"topic": "artificial intelligence"}}'
```

### Running the Streamlit Chatbot

Navigate to the `chatbot` directory and run:
```bash
cd chatbot
streamlit run app.py
```

The chatbot will open in your default web browser at `http://localhost:8501`

Simply enter your question or topic in the text input field and receive AI-generated responses.

## Configuration

### Environment Variables

- `GEMINI_API_KEY`: Required - Your Google Gemini API key
- `LANGSMITH_API_KEY`: Optional - For LangSmith tracing and monitoring

### Model Configuration

The project uses `gemini-2.5-flash` model by default. You can modify the model name in:
- `api/api.py` (line 19)
- `chatbot/app.py` (line 35)

## Dependencies

- `langchain_core` - Core LangChain functionality
- `langchain_google_genai` - Google Gemini integration
- `langserve` - LangChain server utilities
- `fastapi` - Web framework for the API server
- `uvicorn` - ASGI server for FastAPI
- `streamlit` - Web framework for the chatbot
- `python-dotenv` - Environment variable management
- `langchain_community` - Community LangChain integrations

## Notes

- The API server includes commented-out code for Ollama integration (using Llama2 model)
- Make sure your `.env` file is in the root directory and not committed to version control
- The FastAPI server includes a hardcoded path to Google Application Credentials JSON file (line 12 in `api.py`) - you may need to update this path or remove it if not needed

## License

This project is provided as-is for educational and development purposes.

