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


tools = [search, transcribe, get_today_date, send_email]

