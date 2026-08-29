# ✈️ Voyara — Multi-Agent Travel Planner with LangGraph

**Voyara** is an open-source, multi-agent AI travel planner that transforms a natural-language travel request into a practical trip plan with **flight research, hotel suggestions, and a day-by-day itinerary**.

The system is built around a **LangGraph workflow** that coordinates specialized agents, each responsible for a specific part of the travel-planning process.

> **User Request → Flight Agent → Hotel Agent → Itinerary Agent → Final Response**

---

## ✨ Why Voyara?

Planning a trip often requires switching between multiple platforms for flights, hotels, destinations, and itinerary research.

Voyara brings these tasks into a single AI workflow.

Instead of building one large agent responsible for everything, Voyara separates responsibilities into specialized agents:

* ✈️ **Flight Agent** — researches available flight information
* 🏨 **Hotel Agent** — discovers accommodation options
* 🗺️ **Itinerary Agent** — builds a structured day-by-day plan
* 🧠 **Final Response Agent** — combines the results into a user-friendly response

These agents are coordinated through **LangGraph**, allowing the workflow to maintain state and pass information between different stages.

---

## 🚀 Features

* ✈️ Flight research using **AviationStack**
* 🏨 Hotel and travel research using **Tavily**
* 🧠 Multi-agent orchestration with **LangGraph**
* 🔗 LLM integration using **LangChain + Groq**
* 📝 Structured day-by-day itinerary generation
* 🌐 FastAPI backend
* 💻 Lightweight HTML/CSS/JavaScript frontend
* 💾 Conversation state persistence with **PostgreSQL**
* 🔄 Stateful agent workflow
* ⚙️ Environment-based configuration
* 📦 Dependency and project management with **uv**

---

## 🏗️ Architecture

Voyara follows a state-driven multi-agent architecture:

```text
                         ┌──────────────────┐
                         │   User Request   │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    FastAPI API   │
                         └────────┬─────────┘
                                  │
                                  ▼
                       ┌──────────────────────┐
                       │   LangGraph Workflow │
                       └──────────┬───────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              ▼                   ▼                   ▼
      ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
      │ Flight Agent │    │  Hotel Agent │    │ Itinerary    │
      │              │    │              │    │    Agent     │
      └──────┬───────┘    └──────┬───────┘    └──────┬───────┘
             │                   │                   │
             ▼                   ▼                   ▼
      AviationStack           Tavily             Groq/LLM
             │                   │                   │
             └───────────────────┼───────────────────┘
                                 ▼
                       ┌────────────────────┐
                       │ Final Response Agent│
                       └──────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │  Travel Plan     │
                         └──────────────────┘
```

### Workflow

1. The user submits a natural-language travel request.
2. FastAPI receives and validates the request.
3. LangGraph initializes the workflow state.
4. The **Flight Agent** gathers flight-related information.
5. The **Hotel Agent** researches accommodation options.
6. The **Itinerary Agent** generates a practical travel schedule.
7. The **Final Response Agent** combines the collected information.
8. The final travel plan is returned to the user.
9. Conversation state can be persisted in PostgreSQL.

---

## 🧰 Tech Stack

| Layer                  | Technology                   |
| ---------------------- | ---------------------------- |
| Language               | Python 3.10+                 |
| Package Manager        | **uv**                       |
| API                    | FastAPI                      |
| Frontend               | Jinja2 + HTML/CSS/JavaScript |
| Agent Orchestration    | LangGraph                    |
| LLM Framework          | LangChain                    |
| LLM Provider           | Groq                         |
| Database               | PostgreSQL                   |
| Flight Data            | AviationStack                |
| Web Research           | Tavily                       |
| Environment Management | python-dotenv                |

---

## 📁 Project Structure

```text
.
├── app.py                 # FastAPI application entry point
├── backend.py             # LangGraph travel workflow
├── pyproject.toml         # Project metadata and dependencies
├── uv.lock                # Locked dependency versions
├── static/                # Frontend static assets
├── templates/             # Jinja2 templates
└── tools/
    ├── flight.py          # AviationStack integration
    └── search.py          # Tavily search integration
```

> The exact contents of `tools/` may vary depending on the implementation.

---

# ⚡ Getting Started

## Prerequisites

Make sure you have:

* Python **3.10+**
* [`uv`](https://docs.astral.sh/uv/)
* PostgreSQL
* Groq API key
* Tavily API key
* AviationStack API key

---

## 1. Clone the Repository

```bash
git clone https://github.com/Anshuman-sharma2006/voyara.git

cd voyara
```

---

## 2. Install Dependencies

Voyara uses **uv** for dependency and environment management.

Sync the project:

```bash
uv sync
```

This creates the project environment and installs the dependencies defined by the project.

---

## 3. Configure Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/travel_db

GROQ_API_KEY=your_groq_api_key
AVIATIONSTACK_API_KEY=your_aviationstack_api_key
TAVILY_API_KEY=your_tavily_api_key

DEFAULT_ORIGIN_IATA=DAC
```

### Environment Variables

| Variable                | Description                         |
| ----------------------- | ----------------------------------- |
| `DATABASE_URL`          | PostgreSQL connection string        |
| `GROQ_API_KEY`          | API key for Groq                    |
| `AVIATIONSTACK_API_KEY` | AviationStack API key               |
| `TAVILY_API_KEY`        | Tavily API key                      |
| `DEFAULT_ORIGIN_IATA`   | Default departure airport IATA code |

> Never commit your `.env` file or API keys to version control.

---

# ▶️ Running the Application

Start the FastAPI application through `uv`:

```bash
uv run  app.py
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

For development with auto-reload:

```bash
uv run uvicorn app:app --reload
```

---

# 🔌 API

## Health Check

```http
GET /health
```

Used to verify that the backend is running.

---

## Travel Planning

```http
POST /api/travel
```

Example:

```bash
curl -X POST http://127.0.0.1:8000/api/travel \
  -H "Content-Type: application/json" \
  -d '{"message":"Plan a 3-day trip to Tokyo with a budget of $1200"}'
```

Example user request:

```text
Plan a 3-day trip to Tokyo with a budget of $1200.
```

The workflow can use the request to research:

* Flight information
* Accommodation options
* Destination information
* Daily activities
* Estimated trip structure

---

# 🧠 Multi-Agent Workflow

Voyara uses a **specialized-agent architecture** rather than a single monolithic agent.

### Flight Agent

Responsible for flight-related research.

```text
User Request
     │
     ▼
Flight Agent
     │
     ▼
AviationStack
     │
     ▼
Flight Information
```

### Hotel Agent

Researches accommodation and travel-related information using Tavily.

```text
User Request
     │
     ▼
Hotel Agent
     │
     ▼
Tavily Search
     │
     ▼
Hotel / Destination Research
```

### Itinerary Agent

Uses the available trip information to construct a practical day-by-day itinerary.

```text
Trip Information
       │
       ▼
Itinerary Agent
       │
       ▼
Day-by-Day Plan
```

### Final Response Agent

Combines the outputs from the different stages and produces the final response presented to the user.

---

# 🗃️ State & Persistence

Voyara uses **LangGraph state** to pass information between agents during execution.

The workflow can maintain information such as:

```text
User Request
    │
    ├── Destination
    ├── Dates
    ├── Budget
    ├── Flight Research
    ├── Hotel Research
    └── Itinerary
```

PostgreSQL is used for conversation/state persistence so that travel-planning interactions can be maintained beyond a single request.

---

# 🛠️ Development

Because the project uses `uv`, development commands are executed through `uv run`.

### Run Python File

```bash
uv run File_name
```

### Run the FastAPI server

```bash
uv run uvicorn app:app --reload
```

### Add a dependency

```bash
uv add package-name
```

### Add a development dependency

```bash
uv add --dev package-name
```

### Remove a dependency

```bash
uv remove package-name
```

### Update the lockfile

```bash
uv lock
```

### Sync the environment

```bash
uv sync
```

---

# 🔐 Security

API keys should always be provided through environment variables.

Do **not** commit:

```text
.env
```

or expose:

```text
GROQ_API_KEY
TAVILY_API_KEY
AVIATIONSTACK_API_KEY
DATABASE_URL
```

A `.env.example` file can be used to document the required configuration without exposing secrets.



---

# 🤝 Contributing

Contributions are welcome.

To contribute:

```bash
git fork
```

Create a feature branch:

```bash
git checkout -b feature/your-feature
```

Install dependencies:

```bash
uv sync
```

Make your changes, test them locally, and open a pull request.

For larger changes, consider opening an issue first to discuss the proposed architecture or feature.

---

# 📄 License

This project is open source. Add your preferred license here, for example:

```text
MIT License
```

---

# 🙌 Acknowledgments

Voyara is built using modern AI and developer tooling, including:

* **LangGraph** for stateful agent orchestration
* **LangChain** for LLM application development
* **Groq** for LLM inference
* **FastAPI** for the backend API
* **AviationStack** for flight data
* **Tavily** for web research
* **PostgreSQL** for persistence

The project is intended as a practical example of building a **real-world multi-agent AI application** with external tools, persistent state, and a production-oriented backend architecture.
