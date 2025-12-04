import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser

OPENAI_API_KEY =""
llm1=ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)
llm2=ChatOllama(model="gemma:2b")
# Input as a Topic
# generate a creative Title for a Speech on that Topic
# generate a speech for this title

llm=ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)

title_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""You are an experienced speech writer.
    You need to craft an impactful, viral, thoughtful title for a speech on the
    following topic: {topic}
    Answer exactky with one title ideally the best one.
    """
)

speech_prompt = PromptTemplate(
    input_variables=["title","emotion"],
    template="""You are an experienced speech writer.
    You need to write a powerful {emotion} speech of 300 words with 
    a great hook on following title: {title}
    """
)

first_chain=title_prompt | llm1 | StrOutputParser() | (lambda title :(st.write(title),title)[1])
second_chain=speech_prompt | llm2
final_chain=first_chain |(lambda title:{"title":title,"emotion":emotion})|second_chain

st.title("Sanjay's Speech Generator")

topic = st.text_input("What's on your mind today:")
emotion = st.text_input("Enter the emotion:")



if topic:

    response = final_chain.invoke({"topic":topic})
    st.write(response.content)