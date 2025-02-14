from flask import Flask, request, jsonify
from get_transcripts import get_podcast_data
from LLM_processing import llm_processor
from mongo_functions import database_object
import datetime
import json

app = Flask(__name__)

@app.route('/podcast_agent', methods=['GET'])
def podcast_agent():
    flag = request.args.get('flag')
    if flag:
        db = database_object()
        llm_obj = llm_processor()
        cursor = db.get_latest_podcast()
        latest_record = list(cursor)[0]
        latest_id = latest_record["epidose_Id"]
        podcast_obj= get_podcast_data(episode_id= int(latest_id))
        search_results = podcast_obj.search()
        if search_results:
            all_text = podcast_obj.get_transcript(search_results[1].split("=")[1])
            summary = llm_obj.summarize_podcast(all_text)
            
            record = {
                "epidose_Id": search_results[0].split(":")[0],
                "title": search_results[0],
                "link": search_results[1],
                "length": search_results[2],
                "summary": summary.choices[0].message.content.replace('Output Format:', search_results[0]),
                "database_record_date": datetime.datetime.now(),
                "is_new": True,
                "message": "Podcast summary successfully generated and stored in Mongo Database"
            }
            db.insert_to_mongodb(record)
            record.pop("_id")
            record["database_record_date"]= str(record["database_record_date"])
            return record
        else:
            latest_record["is_new"] = False
            latest_record["message"] = "This podcast is already existing in the database and SDS didn't release a new episode"
            latest_record.pop("_id")
            return latest_record
    else:
        return {"error": "Invalid flag"}

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run()