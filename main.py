from langchain.chat_models import ChatOpenAI
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

# load env vars
load_dotenv()

# create instance of chat model
chat = ChatOpenAI()

prompt = ChatPromptTemplate(
    input_variables=["content"],
    messages=[
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = LLMChain(
    llm=chat,
    prompt=prompt
)

while True:
    # built in fn - will pause execution and wait for user input + user hits Enter
    content = input(">> ")

    result = chain({"content": content})
    print(result["text"])