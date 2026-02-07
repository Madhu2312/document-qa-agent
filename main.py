from ingestion.loader import load_pdfs
from ingestion.chunker import chunk_documents
from embeddings.vector_store import create_vector_store

from retrieval.qa import (
    retrieve_context,
    retrieve_context_by_document
)

from llm.groq_llm import generate_answer
from llm.router import route_query
from llm.arxiv_tool import search_arxiv
from tools.document_inventory import list_documents


def main():
    # 1. Load PDFs
    documents = load_pdfs("data/pdfs")

    # 2. Chunk documents
    chunks = chunk_documents(documents)

    # 3. Create vector store
    db = create_vector_store(chunks)

    print("\nDocument QA ready.")
    print("• Ask questions about uploaded PDFs")
    print("• Ask document metadata questions (count / names)")
    print("• Ask document-wise questions (each / both documents)")
    print("• Or ask to find a research paper (Arxiv)")
    print("Type 'exit' to quit\n")

    while True:
        question = input("Question: ").strip()

        if question.lower() == "exit":
            print("\nExiting Document QA Agent.")
            break

        # 4. Route query
        route = route_query(question)

        # 5. Document metadata path (DETERMINISTIC, NO LLM)
        if route == "doc_meta":
            count, files = list_documents("data/pdfs")

            print("\nDocument Inventory:\n")
            print(f"Total documents: {count}")
            for f in files:
                print(f"- {f}")
            print("-" * 60)
            continue

        # 6. Arxiv path (BONUS FEATURE)
        if route == "arxiv":
            print("\n[Arxiv Search Results]\n")
            print(search_arxiv(question))
            print("-" * 60)
            continue

        # 7. Document-wise semantic QA (PER DOCUMENT)
        if route == "document_wise":
            context = retrieve_context_by_document(db, question)
            answer = generate_answer(context, question)

            print("\nAnswer:\n")
            print(answer)
            print("-" * 60)
            continue

        # 8. Normal document QA (RAG)
        context = retrieve_context(db, question)
        answer = generate_answer(context, question)

        print("\nAnswer:\n")
        print(answer)
        print("-" * 60)


if __name__ == "__main__":
    main()
