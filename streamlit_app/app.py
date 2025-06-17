import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import re
from src.fetch_comments import YouTubeCommentFetcher
import os

# Set Streamlit page config
st.set_page_config(page_title="YouTube Comment Fetcher", layout="centered")

# Title
st.title("🎬 YouTube Comment Fetcher")

# Description
st.markdown("Paste a YouTube video link below to fetch the comments.")

# Input field
youtube_url = st.text_input("📥 Enter YouTube video URL:")

# Function to extract video ID
def extract_video_id(url: str) -> str:
    match = re.search(r"(?:v=|be/)([a-zA-Z0-9_-]{11})", url)
    return match.group(1) if match else None

if youtube_url:
    video_id = extract_video_id(youtube_url)
    
    if video_id:
        st.success(f"✅ Video ID detected: `{video_id}`")

        if st.button("Fetch Comments"):
            try:
                fetcher = YouTubeCommentFetcher()
                title = fetcher.get_video_title(video_id)
                comments = fetcher.fetch_comments(video_id)

                # Create safe filename
                safe_title = re.sub(r'[\\/*?:"<>|]', "_", title)
                filename = f"data/{safe_title}_comments.csv"

                fetcher.save_to_csv(comments, filename=filename)
                
                st.success(f"✅ Saved {len(comments)} comments to `{filename}`")
                st.dataframe(comments)

            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
    else:
        st.warning("⚠️ Could not extract a valid video ID. Please check the link format.")
