import streamlit as st
from get_transcripts import get_podcast_data
from LLM_processing import llm_processor
from mongo_functions import database_object
import datetime

st.title("Podcast Agent")

# Button to run the code
if st.button("Get latest Podcast"):
    db = database_object()
    llm_obj = llm_processor()
    cursor = db.get_latest_podcast()
    latest_record = list(cursor)[0]
    latest_id = latest_record["epidose_Id"]
    podcast_obj= get_podcast_data(episode_id= int(latest_id))
    search_results = podcast_obj.search()
    if search_results:
        all_text = podcast_obj.get_transcript_xml(search_results[1])
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
        st.title("Podcast Summary")

        st.write(f"**Title:** {record['title']}")
        st.write(f"**Episode ID:** {record['epidose_Id']}")
        st.write(f"**Length:** {record['length']}")
        st.write(f"**Database Record Date:** {record['database_record_date']}")
        st.write(f"**New Record:** {'✅ Yes' if record['is_new'] else '❌ No'}")
        st.write(f"**Message:** {record['message']}")

        # Display the summary as markdown
        st.markdown("### Summary")
        st.markdown(record["summary"])

        # Provide a clickable link
        st.markdown(f"[Listen to the episode]({record['link']})")
    else:
        latest_record["is_new"] = False
        latest_record["message"] = "This podcast is already existing in the database and SDS didn't release a new episode"
        latest_record.pop("_id")
        st.write(f"**Title:** {latest_record['title']}")
        st.write(f"**Episode ID:** {latest_record['epidose_Id']}")
        st.write(f"**Length:** {latest_record['length']}")
        st.write(f"**Database Record Date:** {latest_record['database_record_date']}")
        st.write(f"**New Record:** {'✅ Yes' if latest_record['is_new'] else '❌ No'}")
        st.write(f"**Message:** {latest_record['message']}")

        # Display the summary as markdown
        st.markdown("### Summary")
        st.markdown(latest_record["summary"])

        # Provide a clickable link
        st.markdown(f"[Listen to the episode]({latest_record['link']})")
    