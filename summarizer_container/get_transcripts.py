from youtube_transcript_api import YouTubeTranscriptApi
from serpapi import GoogleSearch
from api_keys import serpapi_key
import requests
import re
import xml.etree.ElementTree as ET


class get_podcast_data:
    def __init__(self, search_query = "Super Data Science: ML & AI Podcast with Jon Krohn podcast", episode_id = None, num_results=1):
        if episode_id:
            self.episode_id = episode_id 
            self.search_query = search_query+ " Episode " + str(episode_id+1)
        else:  
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
            if "SDS" in result["title"]:
                if int(result["title"].split(":")[0].split("SDS ")[1]) == self.episode_id:
                    continue
                elif int(result["title"].split(":")[0].split("SDS ")[1]) >= self.episode_id:
                    title = result["title"]
                    link =result["link"]
                    length = result["length"]
                    break
            else:
                try:
                    if int(result["title"].split(":")[0]) == self.episode_id:
                        continue
                    elif int(result["title"].split(":")[0]) >= self.episode_id:
                        title = result["title"]
                        link =result["link"]
                        length = result["length"]
                        break
                except:
                    pass
                title = ''
                continue
        if len(title) == 0:
            return None
        return title, link, length
    
    def get_transcript_xml(self, youtube_link):
        response = requests.get(youtube_link)

        if response.status_code != 200:
            print(f"Failed to fetch the page: {response.status_code}")
            return None

        match = re.search(r'(https://www\.youtube\.com/api/timedtext[^"]+)', response.text)

        if not match:
            print("No subtitle URL found")
            return None
        subtitle_url = match.group(1).replace(r"\u0026", "&")
        response = requests.get(subtitle_url)
        if response.status_code != 200:
            print(f"Failed to fetch subtitles: {response.status_code}")
            return None

        root = ET.fromstring(response.text)
        transcript = " ".join(text_element.text for text_element in root.findall("text") if text_element.text)

        return transcript
