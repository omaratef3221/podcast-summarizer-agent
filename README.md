# 🎙️ Podcast Summarizer Agent

## 🚀 Overview
**Podcast Summarizer Agent** is an AI-powered application that automatically retrieves, transcribes, and summarizes podcast episodes. It uses a combination of LangChain, TogetherAI, and MongoDB to create an intelligent summarization pipeline.

## 🏗️ Architecture
The application uses LangGraph to create a sophisticated agent workflow. Here's how the components interact:

![Agent Workflow](Podcast%20Agent.drawio.png)

### Core Components
1. **Input Handler**
   - Receives and processes user queries
   - Initializes the conversation state
   - Routes requests to appropriate components

2. **Agent Node**
   - Powered by TogetherAI
   - Processes input using advanced language models
   - Makes intelligent decisions about next actions
   - Maintains conversation context

3. **Tool Node**
   - YouTube Search: Finds relevant podcast episodes
   - Transcript Retrieval: Extracts captions from videos
   - Summary Generation: Creates concise episode summaries
   - Database Operations: Manages data persistence

4. **Conditional Routing**
   - Determines workflow progression
   - Handles error cases and retries
   - Manages conversation flow

## ✨ Key Features
- 🔍 **Smart Search**: Automated podcast discovery using SerpAPI
- 📝 **AI-Powered Processing**: 
  - Automatic transcription via YouTube Transcript API
  - Intelligent summarization using TogetherAI
- 🗄️ **Data Management**: 
  - MongoDB integration for persistent storage
  - Efficient metadata management
- 🤖 **Advanced Workflow**: 
  - LangChain-powered agent system
  - Dynamic tool selection
  - Error recovery mechanisms
- 🌐 **Dual Interface**: 
  - Agent works as a cron job on railway.com
  - User-friendly web interface (Streamlit)

## 🛠️ Technology Stack
| Component | Technology | Purpose |
|-----------|------------|----------|
| Backend | Python 3.8+ | Core processing |
| AI Framework | LangChain | Agent orchestration |
| Database | MongoDB | Data storage |
| AI Models | TogetherAI | Content summarization |
| Search | SerpAPI | YouTube search |
| Transcription | YouTube Transcript API | Caption extraction |
| API | Flask | REST interface |
| UI | Streamlit | Web interface |

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
- Python 3.8 or higher
- MongoDB instance
- Required API Keys:
  - TogetherAI
  - SerpAPI
  - MongoDB

### Installation
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure environment variables in `.env` file:
   ```
   TOGETHER_API_KEY=your_key_here
   SERPAPI_API_KEY=your_key_here
   MONGODB_URI=your_connection_string
   ```

### Running the Application

#### Option 1: Flask API
```bash
python app.py
```
Access the API at `http://localhost:5001`

#### Option 2: Streamlit Interface
```bash
streamlit run streamlit_app.py
```

#### Option 3: Docker Deployment
```bash
docker build -t podcast-summarizer .
docker run -p 5001:5001 podcast-summarizer
```

## 🔗 API Documentation

### `/podcast_agent`
- **Method**: GET
- **Purpose**: Process podcast-related queries
- **Parameters**: 
  - `message`: User input message
- **Response**: JSON with agent's response

### `/healthcheck`
- **Method**: GET
- **Purpose**: Verify application status
- **Response**: JSON with system status

## 💰 Resource Costs
| Service | Cost Model | Usage |
|---------|------------|--------|
| TogetherAI | Pay-per-use | AI model calls |
| MongoDB | Free tier available | Data storage |
| SerpAPI | Pay-per-use | Search operations |

## 🔮 Roadmap
- [ ] Enhanced error handling
- [ ] Improved summary quality
- [ ] Additional podcast sources
- [ ] Caching system
- [ ] Performance optimizations

---
🎯 **Mission**: Making podcast content more accessible through AI-powered summarization.
