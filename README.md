# Document Q&A AI Agent

A Document Question-Answering (Q&A) AI Agent that ingests multiple PDF documents, extracts and indexes their content, and allows users to query the documents using natural language.

The system is built using Retrieval-Augmented Generation (RAG) and also includes a bonus feature to search relevant research papers from Arxiv.

---

## Overview

This project demonstrates how to build a lightweight AI agent capable of:

- Processing multiple PDF documents
- Performing semantic search over document content
- Answering user questions grounded in document context
- Providing deterministic document metadata (count, names)
- Fetching related research papers from Arxiv

The application runs entirely from the command line and is designed to be modular, extensible, and easy to reproduce.

---

## Features

- **Multi-PDF Ingestion**  
  Automatically loads all PDF files from a specified directory.

- **Text Chunking**  
  Splits documents into overlapping chunks to improve retrieval accuracy.

- **Vector-Based Retrieval**  
  Uses sentence embeddings and FAISS for fast semantic similarity search.

- **LLM-Powered Answers**  
  Generates answers using a Large Language Model via the Groq API.  
  Responses are strictly grounded in retrieved document context.

- **Deterministic Document Metadata**  
  Accurately reports:
  - Number of documents
  - Names of documents  
  Uses filesystem-based logic to avoid hallucination.

- **Arxiv Integration (Bonus Feature)**  
  Searches for relevant research papers and returns:
  - Title
  - Authors
  - Publication date
  - Summary
  - Direct link

---

## Project Structure

```text
document_qa_agent/
│
├── data/
│   └── pdfs/                    # Input PDF documents (user-provided)
│
├── ingestion/
│   ├── loader.py                # PDF loading logic
│   └── chunker.py               # Text chunking logic
│
├── embeddings/
│   └── vector_store.py          # FAISS vector store creation
│
├── retrieval/
│   └── qa.py                    # Context retrieval logic
│
├── llm/
│   ├── groq_llm.py              # LLM interaction (Groq)
│   ├── router.py                # Query routing logic
│   └── arxiv_tool.py            # Arxiv search integration
│
├── tools/
│   └── document_inventory.py    # Deterministic document listing
│
├── main.py                      # Application entry point
├── requirements.txt             # Project dependencies
├── README.md
└── .gitignore

```
## Technology Stack

Python 3.11+

LangChain

FAISS (CPU)

Sentence-Transformers

Groq LLM API

Arxiv API

PyPDF (via LangChain PyPDFLoader)

All core libraries are open-source, and the application uses free-tier APIs.



## Setup Instructions
1. Clone the Repository
git clone https://github.com/Madhu2312/document-qa-agent.git
cd document-qa-agent

2. Create and Activate Virtual Environment (Windows)
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Set Environment Variables

# Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key_here


# Note: The .env file must not be committed to version control.

# How to Run

# Place your PDF files inside:

data/pdfs/


# Start the application:

python main.py


3. Interact via the terminal.
Type exit to quit the application.


## Example Queries
# Document Content Queries

What is the task described in the documents?

Explain the lab experiment described

Summarize the main points of the document

# Document Metadata Queries

How many documents are present?

What are the names of the documents?

## Arxiv Queries

Find a research paper about AI in medical imaging

Search for papers on transformers in healthcare

## Design Highlights

Uses Retrieval-Augmented Generation (RAG) to ground answers in document content

Separates deterministic logic (document metadata) from LLM-based reasoning

Modular design allows easy extension to new tools or LLM providers

Avoids paid embedding APIs by using local sentence-transformer models

## Limitations

Command-line interface only

Performance depends on document size and number of chunks

Arxiv API may impose rate limits for frequent requests

## Future Enhancements

Web-based interface (Streamlit or FastAPI)

Persistent vector store

Advanced document-level summaries

Support for additional document formats

## License

This project is intended for educational and experimental purposes.
