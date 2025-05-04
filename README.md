# 🎙️ Podcast Summarizer Agent

## 🚀 Overview
**Podcast Summarizer Agent** is an AI-powered application that automatically retrieves, transcribes, and summarizes podcast episodes. It uses a combination of LangChain, TogetherAI, and MongoDB to create an intelligent summarization pipeline.

## ✨ Features
- 🔍 **Automated Retrieval**: Searches for podcast episodes using SerpAPI
- 📝 **Transcription & Summarization**: Extracts captions using YouTube Transcript API and summarizes content using TogetherAI
- 🗄️ **MongoDB Integration**: Stores summaries and metadata in a NoSQL database
- 🤖 **LangChain Integration**: Uses LangChain for building the agent workflow
- 🌐 **Dual Interface**: Available both as a Flask API and Streamlit web application

## 🛠️ Tech Stack
- 🐍 **Python** - Backend processing
- 🤖 **LangChain** - Agent workflow and orchestration
- 🍃 **MongoDB** - NoSQL database for storing summaries
- 🔥 **TogetherAI** - AI model for summarization
- 🔍 **SerpAPI** - YouTube search functionality
- 🎥 **YouTube Transcript API** - Caption extraction
- 🌐 **Flask** - REST API interface
- 📊 **Streamlit** - Web interface

## 📂 Project Structure
```
summarizer_container/
│── app.py               # Flask REST API implementation
│── build_agent.py       # LangChain agent configuration
│── get_transcripts_tools.py  # YouTube search and transcript retrieval
│── prompt.py           # Prompt templates and configurations
│── streamlit_app.py    # Streamlit web interface
│── mongo_functions.py  # MongoDB operations
│── env_variables.py    # Environment variable management
│── requirements.txt    # Python dependencies
│── Dockerfile         # Container configuration
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- MongoDB instance
- API keys for:
  - TogetherAI
  - SerpAPI
  - MongoDB

### Installation
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables in `.env` file

### Running the Application

#### Flask API
```bash
python app.py
```
The API will be available at `http://localhost:5001`

#### Streamlit Interface
```bash
streamlit run streamlit_app.py
```

### Docker Deployment
```bash
docker build -t podcast-summarizer .
docker run -p 5001:5001 podcast-summarizer
```

## 🔗 API Endpoints

### `/podcast_agent`
- **Method**: GET
- **Query Parameters**: 
  - `message`: The input message for the agent
- **Response**: JSON containing the agent's response

### `/healthcheck`
- **Method**: GET
- **Response**: JSON with application status

## 💰 Resource & Cost Breakdown
| Resource     | Cost               | Purpose                                         |
|-------------|--------------------|-------------------------------------------------|
| 🤖 **TogetherAI** | Pay-per-use | AI model for summarization |
| 🍃 **MongoDB** | Free tier available | Database storage |
| 🔍 **SerpAPI** | Pay-per-use | YouTube search functionality |

## 🔮 Future Enhancements
- Enhanced error handling and retry mechanisms
- Improved prompt engineering for better summaries
- Additional podcast sources beyond YouTube
- Caching layer for frequently accessed summaries

---
🎯 This project aims to make podcast content more accessible through AI-powered summarization.
