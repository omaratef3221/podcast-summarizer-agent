from dotenv import load_dotenv
load_dotenv()  

from flask import Flask, request, jsonify
from build_agent import graph
from mongo_functions import database_object
import datetime
import json
from langchain_core.messages import HumanMessage


app = Flask(__name__)

@app.route('/podcast_agent', methods=['GET'])
def podcast_agent():
    my_message = request.args.get('message')
    
    messages = [HumanMessage(content=my_message)]
    events = graph.invoke({'messages': messages})

    return jsonify({"messages": events["messages"][-1].content})


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(port=5001)