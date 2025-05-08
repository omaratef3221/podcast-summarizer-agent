from flask import Flask, jsonify, request
from retreiver import retrieve_and_respond, llm


app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def summarize():
    data = request.get_json()
    question = data.get('message', '')
    response, metadata_list = retrieve_and_respond(question, llm)
    return jsonify({"response": response, "metadata": metadata_list})

if __name__ == '__main__':
    app.run()