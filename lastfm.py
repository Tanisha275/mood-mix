import requests
from config import CLIENT_ID

def get_track_info(track_name, artist):
    url = "http://ws.audioscrobbler.com/2.0/"
    params = {
        "method": "track.getInfo",
        "api_key": CLIENT_ID,
        "artist": artist,
        "track": track_name,
        "format": "json"
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if "track" in data:
        track = data["track"]
        return {
            "url": track.get("url", "N/A"),
            "listeners": track.get("listeners", "N/A"),
            "tags": [t["name"] for t in track.get("toptags", {}).get("tag", [])][:3]
        }
    return None

# Test it
if __name__ == "__main__":
    info = get_track_info("Lush Life", "Zara Larsson")
    print(info)