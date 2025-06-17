import os
import pandas as pd
from googleapiclient.discovery import build
from dotenv import load_dotenv
import re

load_dotenv()

class YouTubeCommentFetcher:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("YOUTUBE_API_KEY")
        if not self.api_key:
            raise ValueError("API key not found. Set YOUTUBE_API_KEY in .env or pass as argument.")
        self.youtube = self._build_service()

    def _build_service(self):
        return build("youtube", "v3", developerKey=self.api_key)

    def fetch_comments(self, video_id: str) -> list:
        comments = []
        request = self.youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            textFormat="plainText"
        )

        while request:
            response = request.execute()
            for item in response.get("items", []):
                comment = item["snippet"]["topLevelComment"]["snippet"]
                comments.append({
                    "author": comment.get("authorDisplayName"),
                    "comment": comment.get("textDisplay"),
                    "likes": comment.get("likeCount"),
                    "published": comment.get("publishedAt")
                })

            request = self.youtube.commentThreads().list_next(request, response)

        return comments

    def save_to_csv(self, comments: list, filename: str = "data/comments.csv") -> None:
        if not comments:
            print("No comments to save.")
            return
        df = pd.DataFrame(comments)
        df.to_csv(filename, index=False)
        print(f"✅ Saved {len(df)} comments to {filename}")
        
    def get_video_title(self, video_id: str) -> str:
        request = self.youtube.videos().list(
            part="snippet",
            id=video_id
        )
        response = request.execute()
        items = response.get("items", [])
        if not items:
            return "untitled_video"
        title = items[0]["snippet"]["title"]
        return re.sub(r'[\\/*?:"<>|]', "_", title)

# Run as script
if __name__ == "__main__":
    video_id = input("🎥 Enter YouTube Video ID: ").strip()
    fetcher = YouTubeCommentFetcher()
    comments = fetcher.fetch_comments(video_id)
    fetcher.save_to_csv(comments)
