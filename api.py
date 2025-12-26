from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv
load_dotenv()

os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\prasa\Downloads\banded-water-475413-q5-5d596263ade5.json"

app=FastAPI(
    title="Langchain server",
    version="0.1.0",
    description="simple api server"
)
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

add_routes(
  app,
  model,
  path="/google_genai"
  
)
#model=ChatGoogleGenerativeAI()
#llm=Ollama(model="llama2")


prompt1=ChatPromptTemplate.from_template("Write an essay about {topic} in 100 words.")
#prompt2=ChatPromptTemplate.from_template("write a poem about {topic} in 100 words.")

add_routes(
    app,
    prompt1|model,
    path="/essay"
)

'''add_routes(
    app,
    prompt2|llm,
    path="/poem"
)'''
 
if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
