def retrieve_context(db, question, k=4):
    """
    Standard RAG retrieval across all documents
    """
    docs = db.similarity_search(question, k=k)
    return "\n\n".join(d.page_content for d in docs)


def retrieve_context_by_document(db, question, k=3):
    """
    Document-wise retrieval: groups context by source document
    """
    docs = db.similarity_search(question, k=k)

    grouped = {}
    for d in docs:
        source = d.metadata.get("source", "Unknown Document")
        grouped.setdefault(source, []).append(d.page_content)

    context = []
    for source, texts in grouped.items():
        context.append(f"\n--- {source} ---\n")
        context.extend(texts)

    return "\n".join(context)
