from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

OPENAI_API_KEY ="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"

llm=OpenAIEmbeddings(api_key=OPENAI_API_KEY)

document=TextLoader("job_listings.txt").load()

text_splitter=RecursiveCharacterTextSplitter(chunk_size=200,chunk_overlap=10)

chunks=text_splitter.split_documents(document)

db=Chroma.from_documents(chunks,llm)

retriever=db.as_retriever()

text=input("I have openings for you. What Role you are looking for?")

docs=retriever.invoke(text)

for doc in docs:
    print(doc.page_content)

