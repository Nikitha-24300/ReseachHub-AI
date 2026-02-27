from typing import List
import numpy as np

# Dummy embedding function - replace with actual embedding model
def generate_embedding(text: str) -> List[float]:
    # Example: simple vector of character codes
    vec = [ord(c) for c in text[:512]]  # limit to 512 chars
    return vec + [0]*(512-len(vec))  # pad to fixed length

# Convert multiple papers into embeddings
def generate_paper_embeddings(papers: list) -> dict:
    embeddings = {}
    for paper in papers:
        embeddings[paper.id] = generate_embedding(paper.content)
    return embeddings