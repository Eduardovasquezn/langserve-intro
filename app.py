import os
from dotenv import load_dotenv
from fastapi import FastAPI
from langserve import add_routes
import uvicorn
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

#
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "langserve-tutorial"


chat_model = ChatOllama(model="llama2")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
        "Convert the user's input into speech fit for a king"),
        MessagesPlaceholder("chat_history"),
        ("human", "{text}")
    ]
)

chain = prompt | chat_model | StrOutputParser()

app = FastAPI(
    title="LangChain",
    version="1.0",
    description="Langserve tutorial"
)

add_routes(app,
           chain,
           path="/king",
           playground_type="chat",
           enable_feedback_endpoint=True,
           enable_public_trace_link_endpoint=True
           )

if __name__ == "__main__":
    uvicorn.run(app, host = "localhost", port =8002)