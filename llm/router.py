def route_query(question: str) -> str:
    q = question.lower()

    # 1. Document metadata (DETERMINISTIC)
    doc_meta_keywords = [
        "how many documents",
        "number of documents",
        "names of the documents",
        "list documents",
        "what documents",
        "which documents"
    ]

    if any(k in q for k in doc_meta_keywords):
        return "doc_meta"

    # 2. Arxiv / research paper queries (BONUS)
    arxiv_keywords = [
        "research paper",
        "arxiv",
        "find a paper",
        "academic paper"
    ]

    if any(k in q for k in arxiv_keywords):
        return "arxiv"

    # 3. Document-wise explanation
    document_wise_keywords = [
        "each document",
        "both documents",
        "per document",
        "separately"
    ]

    if any(k in q for k in document_wise_keywords):
        return "document_wise"

    # 4. Default → RAG
    return "rag"
