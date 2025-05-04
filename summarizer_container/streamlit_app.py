from dotenv import load_dotenv
load_dotenv()  

import streamlit as st
from langchain_core.messages import HumanMessage
from build_agent import graph

st.set_page_config(page_title="Podcast Agent", page_icon="🎙️")
st.markdown("## 🎧 Podcast Agent")
st.markdown("This assistant summarizes podcast transcripts and answers related queries.")

text = st.text_input("📝 Enter your message:", placeholder="Paste your podcast transcript or question here")

if st.button("🚀 Submit"):
    if not text.strip():
        st.warning("Please enter a message before submitting.")
    else:
        with st.spinner("Analyzing your message and fetching insights..."):
            messages = [HumanMessage(content=text)]
            events = graph.invoke({'messages': messages})

        st.success("✅ Response generated and sent by email!")

        with st.expander("📤 Agent Response", expanded=True):
            st.markdown(events["messages"][-1].content, unsafe_allow_html=True)
            st.markdown(events["messages"][-2].content, unsafe_allow_html=True)

        st.info("Tip: You can submit another message or paste a different podcast transcript to explore more.")
