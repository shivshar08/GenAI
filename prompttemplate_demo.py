from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.prompts import PromptTemplate

OPENAI_API_KEY="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"

llm=ChatOpenAI(api_key=OPENAI_API_KEY,model="gpt-4o")

prompt_template=PromptTemplate(
input_variables=["city","month","language","budget"],


template="""You are a Travel Expert in India who know all the tourist attradtions in any particular city.

Please provide information about

1. Must visit attractions in the {city}
2. Local Cuisine
3. Useful Phrases in the {city} in the language {language}
4. Tips for travelling in the given {budget}

Please provide all the above information for the month {month}

Avoid giving information about fictional places. If the city is fictional or non existent, answer: I don't know.
If  budget is less than 5000,please answer no tourist place available for visit in this budget.
"""
)

st.title("Traveller Help ChatBot")

city=st.text_input("Enter the city")
budget=st.number_input("Enter tthe budget",min_value=5000,max_value=500000000)
language=st.text_input("Enter the Language")
month = st.text_input("Enter the month")

if city:
    response=llm.invoke(prompt_template.format(city=city,budget=budget,language=language,month = month))
    st.write(response.content)