from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

## Simple prompt
llm = ChatOpenAI(model="gpt-4o-mini")

response = llm.invoke("how can langsmith help with testing?")

print(response.content)

## Prompt with system message
messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="What is the difference in python between import and from? provide an example of each.")
]

response = llm.invoke(messages)

print(response.content)

## Prompt with prompt template

system_template = "You are an expert translator from English to French"
human_template = "{text}"

prompt = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("human", human_template)
])


chain = prompt | llm
chain_response = chain.invoke({"text": "Hello, how are you?"})

print(chain_response.content)
