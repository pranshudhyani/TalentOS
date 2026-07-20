from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseVectorStore(ABC):

    @abstractmethod
    def add_texts(
        self, texts: List[str], metadatas: List[Dict[str, Any]] = None
    ) -> List[str]:
        pass

    @abstractmethod
    def similarity_search(self, query: str, k: int = 4) -> List[Dict[str, Any]]:
        pass
