from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
        model="llama-3.3-70b-versatile"
    )

messages = [
    SystemMessage(content="You are special in social media content strategy"),
    HumanMessage(content="Give a short tip to create engaging posts on Instagram"),
]

response = llm.invoke(messages)

print(response.content)