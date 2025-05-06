# from dotenv import load_dotenv
# load_dotenv()  
from build_agent import graph
from mongo_functions import database_object
import datetime
import json
from langchain_core.messages import HumanMessage
import argparse


def generate(args):
    my_message = args.message
    messages = [HumanMessage(content=my_message)]
    events = graph.invoke({'messages': messages})
    return events
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--message', type=str, default= "Superdatascience and Lex Fridman")
    args = parser.parse_args()
    events = generate(args)
