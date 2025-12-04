from langchain_community.chat_models import ChatOllama
import streamlit as st
llm=ChatOllama(model="gemma:2b")

st.title("I am your ChatBot: Ask me anything and I will answer it to my best of my knowledge")

question=st.text_input("Enter the Prompt")

if question:
    response=llm.invoke(question)
    st.write(response.content)