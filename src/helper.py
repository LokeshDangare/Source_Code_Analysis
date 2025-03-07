import os
from git import Repo
from langchain.text_splitter import Language
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings


#Clone any github repositories

def repo_ingestion(repo_url):
    os.makedirs("repo", exist_ok=True)
    repo_path = "repo/"
    Repo.clone_from(repo_url, to_path=repo_path)


# Loading repositories as documents
def load_repo(repo_path):
    loader = GenericLoader.from_filesystem(
        repo_path,
        glob="**/*",
        suffixes=[".py"],
        parser=LanguageParser(language=Language.PYTHON, parser_threshold=500)
    )

    documents = loader.load()

    return documents


# Creating text chunks

def text_splitter(documents):
    documents_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON,
        chunk_size=2000,
        chunk_overlap=200
    )

    text_chunks = documents_splitter.split_documents(documents)
    return text_chunks


# Loading embeddings model
def load_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={'device': 'cpu'})
    return embeddings 