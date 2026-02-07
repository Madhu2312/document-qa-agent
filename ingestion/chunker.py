from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    # Safety debug (important for evaluation)
    print(f"[DEBUG] Number of chunks received: {len(chunks)}")

    return chunks
