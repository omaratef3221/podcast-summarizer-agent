import datetime
import markdown2
from youtube_transcript_api import YouTubeTranscriptApi
from serpapi import GoogleSearch
from langchain_community.tools import GmailSendMessage
from langchain_community.agent_toolkits import GmailToolkit 
import markdown2
from langchain_community.tools.gmail.utils import build_resource_service, get_gmail_credentials
from google.oauth2.credentials import Credentials
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

creds = Credentials(
    token=os.getenv("GOOGLE_TOKEN"),
    refresh_token=os.getenv("GOOGLE_REFRESH_TOKEN"),
    token_uri=os.getenv("token_uri"),
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    scopes=["https://mail.google.com/"]
)


api_resource = build_resource_service(credentials=creds)
toolkit = GmailToolkit(api_resource=api_resource)


def search(search_query: str, custom_tbs = "cdr:1,cd_min:4/6/2025,cd_max:4/21/2025,sbd:1"):
    """
    Search about a specific podcast
    args:
    search_query: string,
    custom_tbs: Time-Based Search filters in Google search URLs
    """
    params = {
        "engine": "google",
        "q": search_query,
        "api_key": os.environ["serpapi_key"],
        "num": 5,
        "tbs": custom_tbs,
        "tbm": "vid"
        }

    query = GoogleSearch(params)
    results = query.get_dict()

    return {"messages": results}

def transcribe(youtube_id: str) -> str:
    """
    transrcibe a Youtube video
    args:
    youtube_id: id of a youtube video, if 
    """
    transcriptions = YouTubeTranscriptApi.get_transcript(youtube_id)
    all_text = [x["text"] for x in transcriptions]
    all_text = ' '.join(all_text)
    return all_text

def get_today_date() -> str:
    """
    function to get today date and current time
    """
    import datetime
    return str(datetime.datetime.now())


def send_email(message: str, email_subject: str) -> None:
    """
    function sends an email with the results (if any)
    args: 
    - message (str): email message
    - email_subject (str): the subject of the email
    """
    markdown_text = message
    html_content = markdown2.markdown(markdown_text)
    tool = GmailSendMessage(api_resource=api_resource)
    tool.run({
        "to": "omaratef3221@gmail.com",
        "subject": f"Podcast summary as of: {str(datetime.datetime.now())}",
        "message": html_content,
        "is_html": True
    })
    return None

def send_email(message: str, subject: str) -> None:
    """
    function sends an email with the results (if any)
    args:
    - message (str): email message
    - email_subject (str): the subject of the email
    """
    markdown_text = message
    html_content = markdown2.markdown(markdown_text)
    tool = GmailSendMessage(api_resource=api_resource)
    tool.run({
        "to": "omaratef3221@gmail.com",
        "subject": subject,
        "message": html_content,
        "is_html": True
    })
    return None

def insert_to_mongodb(
    episode_id: str,
    podcast_title: str,
    podcast_description: str,
    podcast_url: str,
    podcast_summary: str,
    length: str = None,
    is_new: bool = True
):
    """
    Insert a structured podcast summary into MongoDB.

    Args:
        episode_id (str): Unique ID of the episode (e.g., YouTube video ID or custom index)
        podcast_title (str): Full title of the podcast or video
        podcast_description (str): Description or caption of the episode
        podcast_url (str): Direct URL to the episode (e.g., YouTube link)
        podcast_summary (str): Markdown-formatted summary of the episode
        length (str, optional): Duration of the episode in HH:MM or MM:SS format
        is_new (bool, optional): Flag to mark the record as newly generated (default: True)

    Example inserted document:
        {
            "episode_id": "856",
            "podcast_title": "The Fastest-Growing Jobs Are AI Jobs",
            "podcast_description": "Interview with Jon Krohn...",
            "podcast_url": "https://www.youtube.com/watch?v=J5CDDV0QdlA",
            "podcast_summary": "### Summary\n- Bullet point 1\n- Bullet point 2",
            "length": "9:49",
            "database_record_date": "2025-02-13T00:11:29.374+00:00",
            "is_new": true,
            "message": "Podcast summary successfully generated and stored in Mongo Database"
        }
    """
    try:
        client = MongoClient(os.getenv("mongodb_uri"), server_api=ServerApi("1"))
        db = client.podcast_agent_results
        collection = db.podcast_summaries

        record = {
            "episode_id": episode_id,
            "podcast_title": podcast_title,
            "podcast_description": podcast_description,
            "podcast_url": podcast_url,
            "podcast_summary": podcast_summary,
            "length": length,
            "database_record_date": datetime.datetime.now().isoformat(),
            "is_new": is_new,
            "message": "Podcast summary successfully generated and stored in Mongo Database"
        }

        collection.insert_one(record)

    except Exception as e:
        print(f"[MongoDB Insert Error] {e}", flush=True)

tools = [search, transcribe, get_today_date, send_email, insert_to_mongodb]

