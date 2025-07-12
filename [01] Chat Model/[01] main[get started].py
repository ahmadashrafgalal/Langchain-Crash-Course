from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
        model="llama-3.3-70b-versatile"
    )

response = llm.invoke("what is square root of 49")

print(response.content)