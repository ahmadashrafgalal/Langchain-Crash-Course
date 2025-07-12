# LangChain Crash Course 🚀

This repository contains a structured and practical crash course for working with **LangChain** and **LLMs** like OpenAI and Groq. It's designed to be modular and beginner-friendly, moving from basic chat models to advanced concepts like chains and RAG.

---

## 📁 Project Structure

```

LangChain Crash Course/
│
├── .vscode/                  # VSCode settings (optional)
├── \[01] Chat Model/          # Basic chat model examples
│   ├── \[01] main\[get started].py
│   ├── \[02] main\[messages].py
│   ├── \[03] main\[more than model!].py
│   └── \[04] main\[chat in terminal].py
│
├── \[02] Prompt Template/
│   └── \[05] main\[Prompt Templates].py
│
├── \[03] Chains/
│   ├── \[06] main\[Chains].py
│   ├── \[07] main\[Chains - Inner Workings].py
│   ├── \[08] main\[Chains - Sequential Chaining].py
│   ├── \[09] main\[Chains - Parallel Chaining].py
│   └── \[10] main\[Chains - Conditional Chaining].py
│
├── \[04] RAG/
│   ├── db/                   # Vector store and Chroma DB
│   │   └── chroma\_db/
│   │       ├── chroma.sqlite3
│   │       └── <embeddings folders>
│   ├── \[11] main\[RAGs Intro] copy.py
│   └── \[12] main\[RAGs Intro 2].py
│
├── documents/                # Example documents for RAG
│   ├── Lec 2 Alt.txt
│   └── temp.txt
│
├── .env                      # Environment variables (gitignored)
├── .gitignore                # Ignore .env and db folder
├── \[00] Chain Class Explain.ipynb
└── README.md                 # This file

````

---

## 📦 Key Technologies
- **LangChain**  
- **OpenAI / Groq LLMs**  
- **Chroma DB** for vector storage  
- **Python** for logic and chaining  
- **Jupyter Notebooks** for explainability

---

## 🛑 Environment Setup

1. Create your `.env` file:
```env
OPENAI_API_KEY=your_openai_key_here
GROQ_API_KEY=your_groq_key_here
````

---

## ✅ What's Covered?

* Basic usage of chat models
* Prompt engineering with templates
* Chaining multiple tools using LangChain
* Working with **RAG**: Retrieval-Augmented Generation
* Saving and querying embeddings via Chroma

---

## 📌 Notes

* The `db/` folder is **gitignored** to avoid committing vector stores.
* The `.env` file is also **excluded from Git** for security reasons.

---

## 📬 Contact

Built by **Ahmad Ashraf Galal**
Feel free to connect or give feedback on [LinkedIn](https://www.linkedin.com/in/ahmadashrafgalal)
