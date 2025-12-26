from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


gemini_api_key = os.getenv("GEMINI_API_KEY")
langchain_api_key = os.getenv("LANGSMITH_API_KEY")


os.environ["LANGCHAIN_TRACING_V2"] = "true"

if langchain_api_key:
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant for answering questions."),
    ("user", "Question: {question}")
])


st.title("LangChain Gemini Chatbot")
input_text = st.text_input("Enter a topic or question:")


if not gemini_api_key:
    st.error("GEMINI_API_KEY not found! Please check your .env file.")
else:
   
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=gemini_api_key
    )

   
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    
    if input_text:
        with st.spinner("Thinking..."):
            try:
                response = chain.invoke({"question": input_text})
                st.subheader("Response:")
                st.write(response)
            except Exception as e:
                st.error(f"Error: {e}")
