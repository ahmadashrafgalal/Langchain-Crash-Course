from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatGroq(
        model="llama-3.3-70b-versatile"
    )

############
# Example 1
############

template = "write a {tone} email to {company} expressing interest in {position}, mentioning {skill} as a key strength. keep it to 4 lines max"

prompt_template = ChatPromptTemplate.from_template(template)

prompt = prompt_template.invoke({
    "tone": "professional",
    "company": "Acme Corp",
    "position": "Software Engineer",
    "skill": "problem-solving"
})

result = model.invoke(prompt)

print(result.content)

############
# Example 2 
############
messages = [
    ("system", "you are a comedian who tells jokes about {topic}."),
    ("human", "tell me {jokes_count} jokes")
]

prompt_template = ChatPromptTemplate.from_messages(messages)

prompt = prompt_template.invoke({
    "topic": "Python",
    "jokes_count": 3
})

print(prompt)

result = model.invoke(prompt)

print(result.content)
 