from papers.embedding_utils import search

def build_context(question: str, k: int = 3):
    docs = search(question, k)
    return "\n".join(docs)