from typing import Any, Dict, List
from app.vectorstore.base import BaseVectorStore


class PGVectorStore(BaseVectorStore):

    def __init__(
        self, connection_string: str, collection_name: str = "embeddings"
    ):
        self.connection_string = connection_string
        self.collection_name = collection_name

    def add_texts(
        self, texts: List[str], metadatas: List[Dict[str, Any]] = None
    ) -> List[str]:
        # Placeholder for pgvector insertion
        return []

    def similarity_search(self, query: str, k: int = 4) -> List[Dict[str, Any]]:
        # Placeholder for pgvector similarity search
        return []
