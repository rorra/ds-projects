from langchain.chains import ConversationalRetrievalChain
from app.chat.chains.stremeable import StremeableChain


class StreamingConversationalRetrievalChain(StremeableChain, ConversationalRetrievalChain):
    pass
