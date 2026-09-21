# Digital Twin – AI-Powered Career Assistant

An interactive AI-powered digital twin that represents my professional background, skills, education and career experience.

The application allows visitors such as recruiters, hiring managers and potential collaborators to have a conversational interaction with an AI representation of my professional profile.

## Live Demo

**Try the Digital Twin:**
https://twin-project-u04s.onrender.com/

## Overview

This project was developed to explore how Large Language Models (LLMs) can be used to create an interactive professional profile rather than presenting career information only through a traditional CV or LinkedIn profile.

The Digital Twin can answer career-related questions based on my professional profile and is designed to communicate my background in a clear and conversational way.

The application combines an OpenAI language model with a structured system prompt, profile information extracted from a LinkedIn PDF, conversation history and custom tools.

## Key Features

* **AI-powered conversational interface** for exploring my professional background
* **Professional profile context** using information extracted from my LinkedIn profile
* **Conversation-aware responses** using previous messages in the current conversation
* **Tool calling** for handling specific actions during conversations
* **Interest capture** when a visitor wants to get in touch
* **Unknown-question handling** when the assistant does not have sufficient information
* **Interactive Gradio interface**
* **Web deployment** for direct access through a live application

## How It Works

The application follows a simple LLM-based conversational architecture:

```text
User
  │
  ▼
Gradio Chat Interface
  │
  ▼
Conversation History
  │
  ▼
System Prompt
  ├── Professional Summary
  └── LinkedIn Profile Context
  │
  ▼
OpenAI LLM
  │
  ├── Normal Response
  │
  └── Tool Call
       ├── Record User Interest
       └── Record Unknown Question
  │
  ▼
Final Response
  │
  ▼
User
```

## Technical Architecture

### 1. Profile Context

The application loads professional information from two sources:

* `summary.txt` – personal and career summary
* `linkedin.pdf` – LinkedIn profile information

The PDF content is extracted programmatically using `pypdf` and incorporated into the application's system context.

### 2. LLM Integration

The application uses the OpenAI API to generate conversational responses.

The model receives:

* System instructions
* Professional profile information
* Conversation history
* The current user message
* Available tools

### 3. Tool Calling

The application implements function-based tool calling.

Two tools are currently available:

#### `record_user_details`

Used when a visitor provides contact information and wants to get in touch.

#### `record_unknown_question`

Used when the assistant does not know the answer to a visitor's question.

These events are sent through the Pushover API for notification and follow-up.

### 4. Conversation Handling

The application maintains the conversation history and sends previous messages together with each new user request.

When the LLM requests a tool, the application:

1. Identifies the requested tool.
2. Extracts the tool arguments.
3. Executes the corresponding Python function.
4. Returns the tool result to the model.
5. Generates the final response.

## Technology Stack

| Technology    | Purpose                                |
| ------------- | -------------------------------------- |
| Python        | Application development                |
| OpenAI API    | Large Language Model integration       |
| Gradio        | Interactive web interface              |
| PyPDF         | PDF text extraction                    |
| Requests      | API communication                      |
| python-dotenv | Environment variable management        |
| Pushover API  | Notifications and interaction tracking |
| Render        | Application deployment                 |

## Project Structure

```text
Twin-Project-
│
├── app.py
├── context.py
├── tools.py
├── styles.py
├── summary.txt
├── linkedin.pdf
├── requirements.txt
├── .gitignore
└── README.md
```

### File Responsibilities

**`app.py`**
Main application entry point. Initializes the OpenAI client, manages conversations, handles tool calls and launches the Gradio interface.

**`context.py`**
Builds the system prompt and loads professional profile information from `summary.txt` and `linkedin.pdf`.

**`tools.py`**
Defines and handles the application's tools for recording visitor interest and unknown questions.

**`styles.py`**
Contains the interface styling, JavaScript and example prompts used by the Gradio application.

**`summary.txt`**
Contains the professional and career summary used by the Digital Twin.

**`linkedin.pdf`**
Provides additional professional profile information that is extracted and included in the model context.

**`requirements.txt`**
Contains the Python dependencies required to run the application.

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/teju98patil/Twin-Project-.git
cd Twin-Project-
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file and provide the required API credentials.

Example:

```text
OPENAI_API_KEY=your_openai_api_key
PUSHOVER_USER=your_pushover_user
PUSHOVER_TOKEN=your_pushover_token
```

Do not commit API keys or other secrets to the repository.

### 5. Run the application

```bash
python app.py
```

The Gradio application will start locally.

## Design Principles

The Digital Twin is designed around several principles:

### Professional Focus

The assistant is restricted to career, background, skills and professional experience rather than acting as a general-purpose chatbot.

### Transparency

When asked, the assistant identifies itself as an AI digital twin rather than presenting itself as the actual person.

### No Fabricated Information

The system prompt instructs the assistant not to invent information. When information is unavailable, the application records the unanswered question for later review.

### Human Follow-Up

When a visitor expresses interest in getting in touch, the application can collect contact information for follow-up.

## Current Limitations

The current version uses profile information directly in the model context. It does not currently implement:

* Retrieval-Augmented Generation (RAG)
* Vector database search
* Semantic document retrieval
* Automated response evaluation
* Source-level citations for individual answers
* A dedicated CV parsing pipeline

These are potential areas for future development.

## Future Development

Planned improvements include:

* Integrating my current CV as an additional knowledge source
* Improving the professional profile summary
* Separating professional experience, education, training and projects
* Adding structured CV-based knowledge
* Exploring Retrieval-Augmented Generation (RAG)
* Adding response evaluation and factuality testing
* Improving the user interface
* Adding better conversation analytics
* Improving grounding and traceability of responses

## What I Learned

Through this project, I gained practical experience in:

* Integrating LLM APIs into a Python application
* Designing system prompts for a specific professional use case
* Working with conversational context and message history
* Implementing function/tool calling
* Connecting an LLM application with external APIs
* Extracting information from PDF documents
* Building an interactive Gradio application
* Managing environment variables and API credentials
* Deploying an AI application as a web service

## Author

**Tejaswini Patil**

Master's Student – Data Science for Society and Business
Germany

Interested in **Data Analytics, Business Intelligence, AI and LLM applications**.

## Links

* **Live Demo:** https://twin-project-u04s.onrender.com/
* **GitHub Repository:** https://github.com/teju98patil/Twin-Project-

---

## Disclaimer

This project is a personal technical project created to explore the application of Large Language Models to professional profile representation.

The Digital Twin is an AI-generated representation and should not be treated as a replacement for direct communication with the author.

