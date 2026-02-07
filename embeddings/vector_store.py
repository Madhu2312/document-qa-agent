from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def create_vector_store(chunks):
    print(f"[DEBUG] Number of chunks received: {len(chunks)}")

    chunks = [c for c in chunks if c.page_content.strip()]
    print(f"[DEBUG] Chunks after filtering empty text: {len(chunks)}")

    if not chunks:
        raise ValueError("No valid text chunks to embed")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(chunks, embeddings)
    print("[DEBUG] FAISS index created")

    return db
