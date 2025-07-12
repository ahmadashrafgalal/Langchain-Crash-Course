from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableSequence

load_dotenv()

model = ChatGroq(
        model="llama-3.3-70b-versatile"
    )

prompt_template = ChatPromptTemplate.from_messages(
     [
        ("system", "You love facts and you tell facts about {animal}"),
        ("human", "Tell me {count} facts."),
    ]
)


format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages())) # type: ignore
parse_output = RunnableLambda(lambda x: x.content)

chain = RunnableSequence(first=format_prompt, middle=[invoke_model], last=parse_output)

response = chain.invoke({"animal": "cat", "count": 2})

print(response)