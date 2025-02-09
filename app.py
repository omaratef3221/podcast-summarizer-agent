from flask import Flask, request, jsonify
from get_transcripts import get_podcast_data
from LLM_processing import llm_processor

app = Flask(__name__)

@app.route('/podcast_agent', methods=['GET'])
def podcast_agent():
    flag = request.args.get('flag')
    if flag:
        podcast_obj= get_podcast_data()
        llm_obj = llm_processor()


        search_results = podcast_obj.search()
        if search_results:
            all_text = podcast_obj.get_transcript(search_results[1].split('=')[1])
            summary = llm_obj.summarize_podcast(all_text)
            f = open("podcast_details.md", "a")
            f.write(summary.choices[0].message.content.replace('Output Format:', search_results[0]))
            f.close()
            return {"Response": 200}
        else:
            return {"error": "No valid podcast found"}
    else:
        return {"error": "Invalid flag"}

    

if __name__ == '__main__':
    app.run(debug=True)