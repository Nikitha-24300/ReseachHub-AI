# ResearchHub AI


## Overview

With the exponential growth of academic publications, staying current with scientific literature is increasingly difficult. Traditional methods of managing papers—searching, downloading, organizing, and reading—are time-consuming and limit research productivity.  

**ResearchHub AI** is an intelligent, agentic AI-powered platform designed to streamline research paper discovery, organization, and analysis. It enables researchers to interact with their curated literature through an AI assistant, saving time and enabling rapid comprehension of complex topics.

**Tech Stack:**
- **Frontend:** React, TypeScript, Tailwind CSS  
- **Backend:** FastAPI, Python  
- **AI Model:** Groq Llama 3.3 70B via Groq API  
- **Database:** PostgreSQL (or any supported relational database)  

---

## Features

- **Secure Authentication:** JWT-based user registration and login  
- **Paper Search & Import:** Query academic databases and import papers with metadata  
- **Workspace Management:** Project-specific organization of research papers  
- **AI Chatbot:** Context-aware research assistant powered by Groq LLM  
- **Semantic Search:** Vector-based search for concept-driven queries  
- **Conversation History:** Multi-turn AI interactions with context retention  
- **PDF Upload:** Add personal research papers  
- **Doc Space:** Central repository for all project-related documents  

---

## Usage Scenarios

### 1️⃣ Efficient Research Paper Discovery
- Query multiple academic databases using an intelligent search interface  
- Curated results with metadata (title, authors, abstract, date)  
- One-click import into personal workspaces  

### 2️⃣ AI-Powered Contextual Analysis
- Ask domain-specific questions (e.g., transformer vs CNN architectures)  
- Summarize findings across multiple papers  
- Reduce manual reading and accelerate comprehension  

### 3️⃣ Organized Workspace Collaboration
- Create multiple project-specific workspaces  
- Maintain context-aware AI conversations  
- Track paper relationships and conversation history  

---

## Project Structure

```text
ResearchHub-AI/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── models/
│   ├── routers/
│   └── utils/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── utils/
│   │   └── App.tsx
│   ├── package.json
│   └── tailwind.config.js
└── README.md
React Documentation

Tailwind CSS

