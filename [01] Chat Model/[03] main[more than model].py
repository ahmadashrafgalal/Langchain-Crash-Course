from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

messages = [
    SystemMessage(content="You are special in social media content strategy"),
    HumanMessage(content="Give a short tip to create engaging posts on Instagram"),
]
# Initialize the Groq model
groq_model = ChatGroq(
        model="llama-3.3-70b-versatile"
    )

response = groq_model.invoke(messages)

print(f"Groq Model Response:\n {response.content}")

# Initialize the Google model
google_model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash"
)

response = google_model.invoke(messages)

print(f"{'#'*20}\nGoogle Model Response:\n {response.content}")