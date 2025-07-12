from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
import datetime
from langchain.agents import tool

load_dotenv()

model = ChatGroq(
        model="llama-3.3-70b-versatile"
    )

@tool
def get_time():
    """Returns the current time in the format 'yy-mm-dd HH:MM:SS'."""
    time_now = datetime.datetime.now()
    formatted_time = time_now.strftime("%y-%m-%d %H:%M:%S")
    return f"The current time is: {formatted_time}"

template = "What Is Current Time?"

# prompt_template = ChatPromptTemplate.from_template("{input}")
prompt_template = hub.pull("hwchase17/react") # See from here https://smith.langchain.com/hub/hwchase17/react

tools = [
    get_time,
]

agent = create_react_agent(
    llm=model,
    prompt=prompt_template,
    tools=tools
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

result = agent_executor.invoke({"input": template})

