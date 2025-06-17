# 🎬 YouTube Comment Analyzer

This tool fetches all comments from any public YouTube video, saves them with the video's title as the filename, and provides a simple Streamlit interface to use it — ideal for YouTubers or content creators who want to understand their audience better.

---

## 🚀 Features

- ✅ Fetches **all top-level comments** from any YouTube video
- ✅ Saves comments as CSV named after the video title
- ✅ Easy-to-use **Streamlit interface**
- ✅ Modular class-based backend
- 📦 Ready for further enhancements (sentiment, emotion, clustering, etc.)

---

## 📁 Project Structure
Youtube_Comments_Analysis/
├── data/ # Saved CSV files
├── src/ # Core logic
│ └── fetch_comments.py
├── streamlit_app/ # Streamlit frontend
│ └── app.py
├── .env # (not committed) contains YOUTUBE_API_KEY
├── requirements.txt
└── README.md

