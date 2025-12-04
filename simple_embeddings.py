from langchain_openai import OpenAIEmbeddings

OPENAI_API_KEY ="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"

llm=OpenAIEmbeddings(api_key=OPENAI_API_KEY)

text=input("Enter the Text")
response=llm.embed_query(text)

print(response)