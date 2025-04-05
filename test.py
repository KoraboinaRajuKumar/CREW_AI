import os
import streamlit as st
from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit page config
#st.set_page_config(page_title="Content Reseracher &  Writer", page_icon="📰", layout="wide")

# Title and description
st.title("🤖 Content Researcher & Writer")
st.markdown("Generate blog posts about any topic using AI agents.")

with st.sidebar:
    st.header("Content setting")

    st.text_area(
        "Enter your topic",
        height=100,
        placeholder="enter your topic name"
    )

    st.markdown("LLM Settings")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)

    # Add some spacing
    st.markdown("---")

    generate_button = st.button("Generate Content", type="primary",use_container_width=True)

    with st.expander("ℹ️ How to use"):
        st.markdown("""
        1. Enter your desired content topic
        2. Play with the temperature
        3. Click 'Generate Content' to start
        4. Wait for the AI to generate your article
        5. Download the result as a markdown file
        """)

