# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some Oxlint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the Oxlint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and Oxlint's TypeScript related rules in your project.

Project Introduction
# AI-First CRM HCP Module – Log Interaction Screen

## Project Overview

This project is developed as part of the Round 1 Technical Assignment.

The application is an AI-First CRM system for Healthcare Professionals (HCPs). It allows medical representatives to log interactions with doctors using either a structured form or a conversational AI chat interface.

The system uses React for the frontend, FastAPI for the backend, LangGraph for AI workflow orchestration, Groq LLM for intelligent processing, and MySQL for data storage.

---

## Tech Stack

### Frontend
- React.js
- Redux Toolkit
- React Router DOM
- Bootstrap
- Axios

### Backend
- Python
- FastAPI
- LangGraph
- Groq API (gemma2-9b-it)

### Database
- MySQL

### Font
- Google Inter

---

## Features

- Dashboard
- HCP Interaction Form
- AI Chat Interface
- Interaction Summary
- Entity Extraction
- Store Interaction History
- Responsive UI

---

## LangGraph Agent

The LangGraph agent acts as an intelligent assistant for medical representatives.

It receives user input, understands the interaction, decides which tool should be executed, processes the information using the LLM, and stores or updates interaction records.

---

## LangGraph Tools

### 1. Log Interaction
Logs interaction details between the sales representative and HCP.

### 2. Edit Interaction
Allows modification of previously logged interaction records.

### 3. Interaction Summary
Generates a concise summary using the LLM.

### 4. Entity Extraction
Extracts important entities such as:

- Doctor Name
- Hospital
- Products
- Follow-up Date
- Speciality

### 5. Follow-up Recommendation
Suggests the next best action based on previous interaction history.

---

## Folder Structure

```
Project
│
├── frontend
│   ├── src
│   ├── components
│   ├── pages
│   ├── redux
│   ├── services
│   └── styles
│
├── backend
│   ├── main.py
│   ├── langgraph_agent.py
│   ├── tools.py
│   ├── requirements.txt
│
├── README.md
└── database.sql
```

---

## Installation

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Runs on:

```
http://localhost:5173
```

---

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Runs on:

```
http://127.0.0.1:8000
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Backend Status |
| POST | /log-interaction | Save Interaction |
| PUT | /edit-interaction | Update Interaction |
| POST | /summary | Generate Summary |
| POST | /entities | Extract Entities |
| POST | /followup | Suggest Follow-up |

---

## Future Enhancements

- User Authentication
- CRM Dashboard Analytics
- Voice Interaction
- Email Integration
- Calendar Integration
- Multi-user Support

---

## Developed By

**Diksha Rode**
