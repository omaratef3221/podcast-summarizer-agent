from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore 
from langchain_openai import OpenAIEmbeddings
from langchain.docstore.document import Document


client = MongoClient(os.getenv("mongodb_uri"), server_api=ServerApi("1"))

def get_latest_podcast():
    mydatabase = client.podcast_agent_results
    mycollection = mydatabase.podcast_summaries
    latest_podcast = mycollection.find().sort([("database_record_date", -1)]).limit(1)
    return latest_podcast

def insert_rag(latest_podcast):
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-large",
    )

    api_key = os.getenv("PINECONE_API_KEY")
    pc = Pinecone(api_key=api_key)
    spec = ServerlessSpec(cloud="aws", region="us-east-1")

    namespace = str(latest_podcast["podcast_title"])
    index_name = "podcast-summaries"

    exclude_keys = ["_id", "database_record_date", "podcast_summary"]
    metadata = {k: latest_podcast[k] for k in set(list(latest_podcast.keys())) - set(exclude_keys)}

    doc =  [Document(page_content=latest_podcast["podcast_summary"] , metadata=metadata)]

    docsearch = PineconeVectorStore.from_documents(
        documents=doc,
        index_name=index_name,
        embedding=embeddings,
        namespace=namespace
    )