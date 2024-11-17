from typing import Optional, List, Dict, Any

from langchain.embeddings.base import Embeddings
from langchain.vectorstores.chroma import Chroma
from langchain.schema import BaseRetriever
from langchain_core.callbacks import Callbacks
from langchain_core.documents import Document
from pydantic import Field


class RedundantFilterRetriever(BaseRetriever):
    embeddings: Embeddings = Field(..., description="Embeddings object")
    chroma: Chroma = Field(..., description="Chroma object")

    def __init__(self, embeddings: Embeddings, chroma: Chroma):
        super().__init__()
        self.embeddings = embeddings
        self.chroma = chroma

    def get_relevant_documents(
        self,
        query: str,
        *,
        callbacks: Callbacks = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        run_name: Optional[str] = None,
        **kwargs: Any,
    ) -> List[Document]:
        # Calculate embeddings for the 'query' string
        emb = self.embeddings.embed_query(query)

        # take embeddings and feed them into that
        # max_marginal_relevance_search_by_vector
        return self.chroma.max_marginal_relevance_search_by_vector(
            embedding=emb,
            lambda_mult=0.8,
        )

    async def get_relevant_documents_async(
        self,
        query: str,
    ) -> List[Document]:
        # Calculate embeddings for the 'query' string
        emb = self.embeddings.embed_query(query)

        # take embeddings and feed them into that
        # max_marginal_relevance_search_by_vector
        return self.chroma.max_marginal_relevance_search_by_vector(
            embedding=emb,
            lambda_mult=0.8,
        )

    class Config:
        arbitrary_types_allowed = True
