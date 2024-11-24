import os
import pinecone
from langchain.vectorstores.pinecone import Pinecone

from app.chat.embeddings.openai import embeddings

pinecone.Pinecone(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENVIRONMENT"),
)

vector_store = Pinecone.from_existing_index(
    os.getenv("PINECONE_INDEX_NAME"),
    embeddings,
)


def build_retriever(chat_args, k=2):
    """
    :param chat_args: ChatArgs object containing
        conversation_id, pdf_id, metadata, and streaming flag.

    :return: A VectorStoreRetriever

    Example Usage:

        chain = build_retriever(chat_args)
    """
    search_kwargs = {
        "filter": {"pdf_id": chat_args.pdf_id},
        "k": k,
    }
    return vector_store.as_retriever(
        search_kwards=search_kwargs,
    )
