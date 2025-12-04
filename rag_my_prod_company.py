import os
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import Chroma

# OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
OPENAI_API_KEY = "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"


embeddings=OpenAIEmbeddings(api_key=OPENAI_API_KEY)
llm=ChatOpenAI(model="gpt-4o",api_key=OPENAI_API_KEY)

# Retriever
document=TextLoader("products-data.txt").load()
text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)

chunks=text_splitter.split_documents(document)
vector_store=Chroma.from_documents(chunks,embeddings)
retriever=vector_store.as_retriever()

# Generator
prompt_template=ChatPromptTemplate(
    [
        ("system","""You are an assistant for answering questions.
         Use the provided context to respond. If the answer isn't clear,
         acknowledge that you don't know.
         Limit your respobnse to three concise statements.
         {context}
        """),
        ("human","{input}")
    ]
)

qa_chain=create_stuff_documents_chain(llm,prompt_template)
rag_chain=create_retrieval_chain(retriever,qa_chain)

print("Chat with Document")
question=input("Your Question Please")

if question:
    response=rag_chain.invoke({"input":question})
    print(response['answer'])