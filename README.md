# 🧠 HealthMind — Agentic AI Health Behavior Assistant

HealthMind is a memory-aware, agentic AI health coach that tracks behavioral data, retrieves long-term patterns using vector memory, and generates personalized, empathetic responses using a local LLM.

Unlike simple chatbots, HealthMind is built as a stateful reasoning agent using:

- 🧠 LangGraph (agent orchestration)
- 🔍 FAISS (vector memory)
- 📊 Behavioral tracking (mood, sleep, stress)
- 🤖 Local LLM via Ollama (Mistral / LLaMA3)
- ⚡ FastAPI backend
- 🔐 Identity-aware architecture

---

## 🚀 Why HealthMind?

Most AI health applications:
- Respond statelessly
- Forget previous interactions
- Rely entirely on LLM reasoning

HealthMind instead:
- Stores behavioral summaries
- Converts them into embeddings
- Retrieves relevant past context
- Applies structured decision logic
- Uses an LLM only to generate grounded, empathetic responses

This makes it:

✔ Memory-aware  
✔ Cost-free (local LLM)  
✔ Privacy-first  
✔ Agentic (decision-driven)  
✔ Production-structured  

---

## 🏗️ Architecture Overview

User Input  
   ↓  
LangGraph Agent  
   ↓  
Retrieve Memory (FAISS)  
   ↓  
Analyze Patterns  
   ↓  
Decision Logic  
   ↓  
LLM Response (Ollama)  

---

## 🧩 Tech Stack

**Backend:** FastAPI  
**Agent Orchestration:** LangGraph  
**Memory Store:** FAISS  
**Embeddings:** Sentence Transformers (MiniLM)  
**LLM:** Ollama (Mistral / LLaMA3)  
**Vector Retrieval:** Semantic Search  
**Authentication:** JWT-based  

---

## 📁 Project Structure

backend/  
│  
├── app/  
│   ├── agents/         # LangGraph agent logic  
│   ├── api/            # FastAPI routes  
│   ├── memory/         # FAISS + embeddings  
│   ├── core/           # LLM configuration  
│   ├── models/         # Data models  
│   └── schemas/        # Pydantic schemas  
│  
├── tests/  
├── docs/  
└── requirements.txt  

---

## 🧠 How It Works

### 1️⃣ User Submits Check-in

```json
{
  "mood": 7,
  "sleep_hours": 6.5,
  "stress": 4,
  "notes": "Felt okay today"
}
```

### System:
- Generates behavioral summary
- Converts summary into embeddings
- Stores vector in FAISS memory index

### User Asks Agent

```json
{
  "user_input": "I feel exhausted and stressed lately"
}
```

### Agent Pipeline:
- Embeds user input
- Retrieves similar past memories
- Analyzes behavioral patterns
- Makes structured decision
- Sends grounded context to LLM
- Returns empathetic response

## 🛠️ Setup Instructions

### 1️⃣ Clone Repository
```
git clone https://github.com/whatsupwithdeepti/HealthMind.git
cd HealthMind/backend
```

### 2️⃣ Create Virtual Environment
```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 4️⃣ Install Ollama

Download from:
https://ollama.com
Pull a model:
```
ollama pull model
```

### 5️⃣ Run Backend
```
uvicorn app.main:app --reload
```

### 6️⃣ Test API
Open:

http://127.0.0.1:8000/docs

Test:
- POST /checkin
- POST /agent/ask

---

## 🔥 Key Features

🧠 Long-term semantic memory
🔍 Similarity-based pattern retrieval
🏗️ LangGraph-based state machine agent
🤖 Fully local LLM (no paid APIs)
📈 Behavioral trend awareness
🔐 Identity-aware structure
🛡️ Safe prompting (no medical diagnosis)

---

## 🎯 Engineering Highlights
- Designed contract-based agent state system
- Implemented defensive FAISS memory retrieval
- Separated decision logic from LLM generation
- Built fully local AI pipeline
- Maintained modular architecture and clean commits

---

## 🚧 Future Improvements
- Add persistent database (PostgreSQL)
- Long-term user identity memory
- Multi-goal coaching workflows
- Analytics dashboard
- Docker deployment
- Model fallback strategy

---

## 📌 Example Response

“It sounds like work has been draining your energy lately. Based on your recent stress patterns, taking short breaks and prioritizing rest this week could help restore balance.”

---

## 🏁 Final Outcome
HealthMind demonstrates:

- Agentic AI architecture
- Memory-aware reasoning
- Retrieval-Augmented Generation
- Local LLM integration
- Real-world backend system design

---

## 👩‍💻 Author
Deepti Jethwani

