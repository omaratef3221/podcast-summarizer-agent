from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain.docstore.document import Document
import os

client = MongoClient(os.getenv("mongodb_uri"), server_api=ServerApi("1"))
db = client.podcast_agent_results
collection = db.podcast_summaries

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index_name = "podcast-summaries"
namespace = "summaries"  # Can also use per-channel or per-user

spec = ServerlessSpec(cloud="aws", region="us-east-1")

if index_name not in [i.name for i in pc.list_indexes()]:
    pc.create_index(name=index_name, dimension=3072, metric="cosine", spec=spec)

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")


def get_latest_podcast():
    mydatabase = client.podcast_agent_results
    mycollection = mydatabase.podcast_summaries
    latest_podcast = mycollection.find().sort([("database_record_date", -1)]).limit(1)
    return latest_podcast

def insert_to_vector_db(podcast: dict):
    if not podcast:
        print("No podcast found.")
        return

    metadata = {
        k: v for k, v in podcast.items()
        if k not in {"_id", "podcast_summary", "podcast_transcript"}
    }

    doc = Document(
        page_content=podcast["podcast_summary"],
        metadata=metadata
    )

    vector_store = PineconeVectorStore.from_documents(
        documents=[doc],
        index_name=index_name,
        embedding=embeddings,
        namespace=namespace
    )
    print("Podcast summary inserted into Pinecone.")
