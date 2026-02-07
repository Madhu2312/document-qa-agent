import os

def list_documents(pdf_dir="data/pdfs"):
    """
    Returns the number of PDF documents and their filenames.
    """
    if not os.path.exists(pdf_dir):
        return 0, []

    pdfs = [
        f for f in os.listdir(pdf_dir)
        if f.lower().endswith(".pdf")
    ]

    return len(pdfs), sorted(pdfs)
