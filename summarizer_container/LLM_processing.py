from prompt_builder import build_prompt
from api_keys import togetherapi_key, mongodb_uri
from together import Together
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

client = Together(api_key=togetherapi_key)  

class llm_processor:
    def __init__(self, model_name = "meta-llama/Llama-3.3-70B-Instruct-Turbo"):
        self.model_name = model_name

    def summarize_podcast(self, podcast_text):
        prompt = build_prompt({"text": podcast_text})
        response = client.chat.completions.create(
                model = self.model_name,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                temperature=0.7,
                top_p=0.9,
                top_k=100,
            )
        return response
    
    def insert_to_mongodb(self, data):
        try:
            client = MongoClient(mongodb_uri , server_api=ServerApi('1'))
            mydatabase = client.podcast_agent_results
            mycollection = mydatabase.podcast_summaries
            mycollection.insert_one(data) 
        except Exception as e:
            print(e, flush=True)

