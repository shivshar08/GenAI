import os
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate

#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_KEY ="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"

llm=ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)
prompt_template = ChatPromptTemplate.from_messages(
[
    ("system","You are an AI Tools Recommender. You are required to suggest Top 5 AI Tools to solve "
    "problems of folks line improving productivity, saving time, saving effort etc. You just need to recommend tools with a one "
    "liner in that AI tool"),
    ("human", "{input}")
]
)

st.title("I can help you use AI for your work")

input = st.text_input("Enter the question:")

chain = prompt_template | llm

if input:
    response = chain.invoke({"input":input})
    st.write(response.content)
