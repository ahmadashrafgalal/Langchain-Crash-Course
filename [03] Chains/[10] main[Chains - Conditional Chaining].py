from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableBranch
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
        model="llama-3.3-70b-versatile"
    )


classification_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("human", "Classify the sentiment of this feedback as positive, negative, neutral, or escalate: {feedback}."),
    ])

positive_feedback_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("human", "Generate a thank you note for this positive feedback: {feedback}."),
    ])

negative_feedback_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("human", "Generate a response addressing this negative feedback: {feedback}."),
    ])

neutral_feedback_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("human", "Generate a request for more details for this neutral feedback: {feedback}.",),
    ])

escalate_feedback_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("human",  "Generate a message to escalate this feedback to a human agent: {feedback}.",),
    ])


branches = RunnableBranch(
    (
        lambda x: "positive" in x, # type: ignore
        positive_feedback_template | model | StrOutputParser()  # Positive feedback chain
    ),
    (
        lambda x: "negative" in x, # type: ignore
        negative_feedback_template | model | StrOutputParser()  # Negative feedback chain
    ),
    (
        lambda x: "neutral" in x, # type: ignore
        neutral_feedback_template | model | StrOutputParser()  # Neutral feedback chain
    ),
    escalate_feedback_template | model | StrOutputParser() # Defult feedback chain
)

classification_chain = classification_template | model | StrOutputParser()

chain = classification_chain | branches

review = "The product is terrible. It broke after just one use and the quality is very poor."
result = chain.invoke({"feedback": review})

print(result)