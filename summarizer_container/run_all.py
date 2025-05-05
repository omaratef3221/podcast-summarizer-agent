from dotenv import load_dotenv
load_dotenv()  
from build_agent import graph
from mongo_functions import database_object
import datetime
import json
from langchain_core.messages import HumanMessage

my_message = "Superdatascience and Lex Fridman"
    
messages = [HumanMessage(content=my_message)]
events = graph.invoke({'messages': messages})
