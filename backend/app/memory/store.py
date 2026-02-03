import faiss
import numpy as np
from typing import List

DIMENSION = 384 

index = faiss.IndexFlatL2(DIMENSION)
memory_texts: List[str] = []

def add_to_memory(embedding: List[float], text: str):
    vector = np.array([embedding]).astype("float32")
    index.add(vector)
    memory_texts.append(text)

def search_memory(embedding: List[float], k: int = 3):
    if index.ntotal == 0:
        return []

    vector = np.array([embedding]).astype("float32")
    distances, indices = index.search(vector, k)

    results = []
    for i in indices[0]:
        if 0 <= i < len(memory_texts):
            results.append(memory_texts[i])

    return results


def retrieve_similar_memories(text_embedding: List[float], k: int = 3):
    return search_memory(text_embedding, k)
