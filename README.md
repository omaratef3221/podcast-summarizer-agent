# 🎙️ Podcast Summarizer Agent

## 🚀 Overview
**Podcast Summarizer Agent** is an AI-powered application that automatically retrieves, transcribes, and summarizes the latest episodes of the *Super Data Science Podcast* from YouTube. It extracts key resources from each episode and stores them in a **MongoDB** database.

## ✨ Features
- 🔍 **Automated Retrieval**: Searches for the latest *Super Data Science Podcast* episodes on YouTube.
- 📝 **Transcription & Summarization**: Extracts captions and summarizes key points using an AI model.
- 🔗 **Resource Extraction**: Identifies and stores relevant links and references from the episode.
- 🗄️ **Storage in MongoDB**: Saves summaries, podcast titles, durations, and YouTube links in a NoSQL database.
- ⏳ **Scheduled Execution**: Can run automatically at set intervals or be triggered via API.

## 🛠️ Tech Stack
- 🐍 **Python** - Backend processing
- 🍃 **MongoDB** - NoSQL database for storing podcast summaries
- 🤖 **TogetherAPI** - AI model hosting (LLaMA for summarization)
- 🔎 **SeraAPI** - YouTube search functionality

## 📂 Project Structure
The application is structured within the `summarizer_container` directory:

```
summarizer_container/
│── 🔑 api_keys.py          # Reads API keys from environment variables
│── 🌐 app.py               # Flask REST API for running the app
│── 🐳 Dockerfile           # Configuration for containerization
│── 📜 requirements.txt     # Dependencies list
│── 🎥 get_transcripts.py   # Handles YouTube search and transcription retrieval
│── 🤖 LLM_processing.py    # Summarization and database insertion using LLaMA
│── ✍️ prompt_builder.py    # Defines prompts for AI summarization
```

## 🚀 Deployment & Execution
This app can be deployed on **Render** (free hosting) or run locally.  
### 🏠 Running Locally
1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Flask API:  
   ```bash
   flask run -h 0.0.0.0 -p 5001
   ```
3. Trigger the summarization process via API request:  
   ```bash
   curl --location 'http://localhost:5001/podcast_agent?flag=1'
   ```

### 🌍 Live Deployment
Currently, the application is deployed on **Render** at:  
🔗 **[Podcast Summarizer Agent](https://podcast-summarizer-agent.onrender.com/)**  

The API returns a **200 Success** response, and summaries are stored in **MongoDB**.

## 💰 Resource & Cost Breakdown
| Resource     | Cost               | Purpose                                         |
|-------------|--------------------|-------------------------------------------------|
| ☁️ **Render**  | Free               | Hosting the web application                     |
| 🤖 **TogetherAPI** | $0.88/1M tokens | Hosting the AI summarization model              |
| 🍃 **MongoDB** | Free (512MB tier)  | Storing summaries, titles, durations, and links |
| 🔍 **SeraAPI** | Free (100 searches/month) | Searching for podcasts on YouTube |

## 🔮 Future Enhancements (Work in Progress)
- 📚 **RAG Database with Pinecone**: Implementing a **retrieval-augmented generation (RAG)** system for querying all past podcast summaries.
- 📱 **Mobile App (Flutter)**: Developing a mobile app that sends weekly notifications about new episodes.

---
🎯 This project aims to streamline podcast knowledge extraction and make insightful content easily accessible.
