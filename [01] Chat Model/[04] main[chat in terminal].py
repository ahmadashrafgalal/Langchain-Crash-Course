from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
        model="llama-3.3-70b-versatile"
    )

chat_history = []

system_message = SystemMessage(content="You are a helpful assistant.")
chat_history.append(system_message)

while True:
    query = input("You : ")
    if query.lower() == 'exit' :
        break

    chat_history.append(HumanMessage(content=query))

    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))

    print("AI : ", response)