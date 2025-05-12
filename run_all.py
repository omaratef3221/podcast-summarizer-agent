# from dotenv import load_dotenv
# load_dotenv()  
from build_agent import graph
import datetime
import json
from langchain_core.messages import HumanMessage
import argparse
from create_rag_pinecone import insert_to_vector_db, get_latest_podcast
from langchain_core.runnables import RunnableConfig
config = RunnableConfig(recursion_limit=15)

def generate(args):
    my_message = args.message
    messages = [HumanMessage(content=my_message)]
    events = graph.invoke({'messages': messages}, config=config)
    return events
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--message', type=str, default= "Lex Fridman")
    args = parser.parse_args()
    events = generate(args)
    latest_podcast = get_latest_podcast()
    latest_podcast = list(latest_podcast)[0]
    insert_to_vector_db(latest_podcast)

