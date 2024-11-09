from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory, ConversationSummaryMemory
from dotenv import load_dotenv
from numpy.f2py.crackfortran import verbose

load_dotenv()

chat = ChatOpenAI()

memory = ConversationSummaryMemory(
    # chat_memory=FileChatMessageHistory("messages.json"),  # memory to store the conversation history
    memory_key="messages",  # key to store the conversation history
    return_messages=True,  # return the conversation history as a list of messages
    llm=chat,  # the language model to use
)

prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = LLMChain(
    llm=chat,
    prompt=prompt,
    memory=memory,
    verbose=True,
)

while True:
    content = input(">> ")
    result = chain({"content": content})
    print(result["text"])
