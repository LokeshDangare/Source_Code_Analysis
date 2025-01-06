import os
from dotenv import load_dotenv, find_dotenv
from src.helper import repo_ingestion, load_repo, text_splitter, load_embeddings
from langchain.vectorstores import Chroma

_ = load_dotenv(find_dotenv())
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

#Comment this 2 lines as I want to use it as User Interface while running web app.
 
#url = "https://github.com/LokeshDangare/Signature-Recognition-System"
#repo_ingestion(url)


documents = load_repo("repo/")
text_chunks = text_splitter(documents)
embeddings = load_embeddings()

#Storing vector in ChromaDB
vectordb = Chroma.from_documents(text_chunks, embedding=embeddings, persist_directory="./db")
vectordb.persist()