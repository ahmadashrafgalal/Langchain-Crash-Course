from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

model = ChatGroq(
        model="llama-3.3-70b-versatile"
    )

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "you are facts expert who know facts about {topic}"),
    ("human", "tell me {facts_count} facts about {topic}")
])

# Chain Using Langchain Expression Language (LCEL)
chain = prompt_template | model | StrOutputParser()

result = chain.invoke({
    "topic": "Python",
    "facts_count": 5
})

print(result)