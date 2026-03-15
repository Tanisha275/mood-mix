from flask import Flask, render_template, request, jsonify
import requests
from config import YOUTUBE_API_KEY
from recommender import recommend_songs
from mood_parser import parse_mood
from lastfm import get_track_info

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    user_input = data.get("mood", "")
    genre = data.get("genre", "")

    # Parse free-form input or use direct mood
    detected_mood = parse_mood(user_input)

    # Get recommendations
    songs_df = recommend_songs(detected_mood, genre=genre if genre else None)

    # Enrich with Last.fm
    songs = []
    for _, row in songs_df.iterrows():
        artist_clean = row["artists"].split(";")[0]
        info = get_track_info(row["track_name"], artist_clean)
        songs.append({
            "title": row["track_name"],
            "artist": artist_clean,
            "popularity": int(row["popularity"]),
            "genre": row["track_genre"],
            "listeners": int(info["listeners"]) if info else 0,
            "tags": info["tags"] if info else [],
            "url": info["url"] if info else "#"
        })

    return jsonify({
        "mood": detected_mood,
        "songs": songs
    })
@app.route("/youtube", methods=["POST"])
def youtube_search():
    data = request.json
    query = f"{data['title']} {data['artist']} official audio"
    
    response = requests.get(
        "https://www.googleapis.com/youtube/v3/search",
        params={
            "part": "id",
            "q": query,
            "key": YOUTUBE_API_KEY,
            "maxResults": 10,
            "type": "video",
            "videoEmbeddable": "true"
        }
    )
    
    result = response.json()
    if not result.get("items"):
        return jsonify({"video_id": None})

    # Get video IDs and check embeddable status server-side
    video_ids = ",".join([item["id"]["videoId"] for item in result["items"]])
    
    check = requests.get(
        "https://www.googleapis.com/youtube/v3/videos",
        params={
            "part": "status,contentDetails",
            "id": video_ids,
            "key": YOUTUBE_API_KEY
        }
    )
    
    for item in check.json().get("items", []):
        if item["status"].get("embeddable") and not item["contentDetails"].get("regionRestriction"):
            return jsonify({"video_id": item["id"]})
    
    # Fallback — return first result anyway
    return jsonify({"video_id": result["items"][0]["id"]["videoId"]})

if __name__ == "__main__":
    app.run(debug=True)