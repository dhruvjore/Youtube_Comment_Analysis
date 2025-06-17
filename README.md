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

```
Youtube_Comments_Analysis/
├── data/                 # Saved CSV files
├── src/                  # Core logic
│   └── fetch_comments.py
├── streamlit_app/        # Streamlit frontend
│   └── app.py
├── .env                  # (not committed) contains YOUTUBE_API_KEY
├── requirements.txt
└── README.md
```

---

## 🧪 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/dhruvjore/Youtube_Comment_Analysis.git
cd Youtube_Comment_Analysis
```

### 2. Set up virtual environment and install dependencies
```bash
python -m venv venv
.\venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### 3. Add your `.env` file
Create a file named `.env` in the root with your API key:
```
YOUTUBE_API_KEY=your_key_here
```

### 4. Run the Streamlit app
```bash
streamlit run streamlit_app/app.py
```

---

## 🧠 Coming Soon

- Sentiment & emotion analysis
- Feedback clustering
- Toxicity detection
- Exportable PDF reports

---

## 📌 Requirements

- Python 3.8+
- YouTube Data API v3 Key
- Internet connection (for API calls)

---

## 🧑‍💻 Author

**Dhruv Jore**  
*Data Scientist | ML Engineer | Creator Insights Enthusiast*  
📧 dhruvjore@gmail.com
