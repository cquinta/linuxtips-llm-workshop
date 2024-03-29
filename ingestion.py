import os
import pinecone
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv, find_dotenv
from pinecone import PodSpec
load_dotenv(find_dotenv(), override=True)

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_ENV = os.environ.get('PINECONE_ENV')

spec = PodSpec(environment=PINECONE_ENV)

embeddings = OpenAIEmbeddings()

loader = PyPDFLoader("docs/clt.pdf")
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(data)

pc=pinecone.Pinecone(api_key=os.environ.get('PINECONE_API_KEY'))

index_name = "linuxtips"
if index_name not in pc.list_indexes():
    pc.create_index(index_name, dimension=1536, spec=spec)

index = pc.Index(index_name)

docsearch = Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name=index_name)

# Test
# query = "o que são as férias?"
# docs = docsearch.similarity_search(query)
# print(docs[0])