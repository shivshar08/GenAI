from langchain_openai import ChatOpenAI

OPENAI_API_KEY="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"

llm=ChatOpenAI(api_key=OPENAI_API_KEY,model="gpt-4o")

question=input("Enter Your Question")
response=llm.invoke(question)
print(response.content)