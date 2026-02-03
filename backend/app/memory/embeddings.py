from sentence_transformers import SentenceTransformer
from typing import List

_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts: List[str]) -> List[List[float]]:
    embedding = _model.encode(texts)
    return embedding.tolist()