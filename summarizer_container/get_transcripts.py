from youtube_transcript_api import YouTubeTranscriptApi
from serpapi import GoogleSearch
from api_keys import serpapi_key

class get_podcast_data:
    def __init__(self, search_query = "Super Data Science: ML & AI Podcast with Jon Krohn latest", num_results=1):
        self.search_query = search_query
        self.num_results = num_results
        
    def search(self):
        params = {
        "engine": "youtube",
        "search_query": self.search_query,
        "api_key": serpapi_key,
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        for result in results["video_results"]:
            if result["title"][0:2].isnumeric() and len(result["length"]) >= 5:
                title = result["title"]
                link =result["link"]
                length = result["length"]
                break
        if len(title) == 0:
            return None
        return title, link, length
    
    def get_transcript(self, youtube_id):
        transcriptions = YouTubeTranscriptApi.get_transcript(youtube_id, proxies={"https": "http://localhost:5001"})
        all_text = [x["text"] for x in transcriptions]
        all_text = ' '.join(all_text)
        return all_text

