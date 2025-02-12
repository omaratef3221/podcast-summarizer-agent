from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from api_keys import mongodb_uri

class database_object:
    def __init__(self):
        self.client = MongoClient(mongodb_uri , server_api=ServerApi('1'))

    def get_latest_podcast(self):
        mydatabase = self.client.podcast_agent_results
        mycollection = mydatabase.podcast_summaries
        latest_podcast = mycollection.find().sort([("epidose_Id", -1)]).limit(1)
        return latest_podcast
    
    def insert_to_mongodb(self, data):
        try:
            mydatabase = self.client.podcast_agent_results
            mycollection = mydatabase.podcast_summaries
            mycollection.insert_one(data) 
        except Exception as e:
            print(e, flush=True)
