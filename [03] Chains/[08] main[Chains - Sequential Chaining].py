from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
        model="llama-3.3-70b-versatile"
    )

animal_facts_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You like telling facts and you tell facts about {animal}."),
        ("human", "Tell me {count} facts."),
    ]
)

translation_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a translator and convert the provided text into {language}."),
        ("human", "Translate the following text to {language}: {text}"),
    ]
)

count_words = RunnableLambda(lambda x: f"Word count: {len(str(x).split())}\n{x}")
prepare_for_translation = RunnableLambda(lambda output: {"text": output, "language": "frensh"})

chain = animal_facts_template | model | StrOutputParser() | prepare_for_translation | translation_template | model | StrOutputParser() 

result = chain.invoke({"animal": "cat", "count": 2})

print(result)