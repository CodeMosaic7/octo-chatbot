from langchain_community.chat_models import ChatOllama
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import FileChatMessageHistory
from langchain.chains import ConversationChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)


llm = ChatOllama(model="llama3.2:1b", temperature=0.1)


history = FileChatMessageHistory("chat_history.txt")
memory = ConversationBufferMemory(chat_memory=history, return_messages=True)


chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "You are a helpful personal assistant for Manika. Be friendly and kind. Make sure answers are concise and complete."
    ),
    MessagesPlaceholder(variable_name="history"),  
    HumanMessagePromptTemplate.from_template("{input}"),
])


conversation_chain = ConversationChain(
    llm=llm,
    prompt=chat_prompt,
    memory=memory,
    verbose=True,
)
