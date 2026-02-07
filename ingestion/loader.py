import os
from langchain_community.document_loaders import PyPDFLoader

def load_pdfs(pdf_dir):
    documents = []

    for file in os.listdir(pdf_dir):
        if file.lower().endswith(".pdf"):
            path = os.path.join(pdf_dir, file)
            loader = PyPDFLoader(path)
            pages = loader.load()

            for page in pages:
                page.metadata["source"] = file  
                documents.append(page)

    return documents
