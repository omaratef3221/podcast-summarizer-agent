import streamlit as st
# from dotenv import load_dotenv
from retreiver import retrieve_and_respond, llm
import toml
config = toml.load(".streamlit/secrets.toml")
import os
# load_dotenv()

os.environ["OPENAI_API_KEY"] = config["openai"]["api_key"]
os.environ["PINECONE_API_KEY"] = config["pinecone"]["api_key"]
os.environ["mongodb_uri"] = config["mongodb"]["uri"]


st.set_page_config(page_title="🎧 Podcast Chatbot", page_icon="🎙️")
st.title("🎧 Podcast Chatbot")
st.caption("Ask questions based on summarized AI podcast episodes.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! Ask me anything about recent AI podcasts."}
    ]

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask a question...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        response_container = st.empty()
        response_container.markdown("_Generating answer..._")

        response, metadata_list = retrieve_and_respond(user_input, llm)
        response_container.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Sidebar: metadata
    if metadata_list:
        st.sidebar.markdown("### 🔍 Retrieved Podcast Info")
        for i, meta in enumerate(metadata_list, 1):
            st.sidebar.markdown(f"**{i}. {meta.get('podcast_title', 'Untitled')}**")
            st.sidebar.markdown(f"- 📅 Date: {meta.get('database_record_date', 'N/A')}")
            st.sidebar.markdown("---")

