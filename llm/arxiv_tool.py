import arxiv
import time

def clean_query(query: str):
    stop_phrases = [
        "find", "a", "research", "paper", "about", "on", "in", "the"
    ]
    words = query.lower().split()
    cleaned = [w for w in words if w not in stop_phrases]
    return " ".join(cleaned) or query


def search_arxiv(query: str, max_results: int = 3):
    cleaned_query = clean_query(query)

    search = arxiv.Search(
        query=cleaned_query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )

    results = []

    try:
        for paper in search.results():
            results.append(
                f"Title: {paper.title}\n"
                f"Authors: {', '.join(a.name for a in paper.authors)}\n"
                f"Published: {paper.published.date()}\n"
                f"Summary: {paper.summary[:400]}...\n"
                f"Link: {paper.entry_id}\n"
                f"{'-'*40}"
            )
            time.sleep(1)  # respect rate limits

    except Exception as e:
        return f"Arxiv search failed due to rate limiting. Please try again.\nDetails: {str(e)}"

    if not results:
        return "No papers found for this topic."

    return "\n".join(results)
