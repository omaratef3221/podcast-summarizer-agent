from prompt_builder import build_prompt
from api_keys import togetherapi_key
from together import Together
import os

client = Together(api_key=togetherapi_key)  

class llm_processor:
    def __init__(self, model_name = "Qwen/Qwen2.5-72B-Instruct-Turbo"):
        self.model_name = model_name

    def summarize_podcast(self, podcast_text):
        prompt = build_prompt({"text": podcast_text})
        response = client.chat.completions.create(
                model = self.model_name,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                temperature=0.7,
                top_p=0.9,
                top_k=100,
            )
        return response
    

