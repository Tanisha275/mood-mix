import pandas as pd
from mood_map import get_mood_features
from lastfm import get_track_info

df = pd.read_csv("dataset.csv")

def recommend_songs(mood, genre=None, limit=10):
    features = get_mood_features(mood)
    
    if features is None:
        print(f"Sorry, I don't recognize the mood '{mood}'")
        return []
    
    filtered = df.copy()
    if genre:
        filtered = filtered[filtered["track_genre"].str.lower() == genre.lower()]
    
    filtered["score"] = (
    abs(filtered["valence"] - features["valence"]) +
    abs(filtered["energy"] - features["energy"]) +
    abs(filtered["danceability"] - features["danceability"]) +
    (1 - filtered["popularity"] / 100) * 0.3  # popularity penalty
)
    
    filtered = filtered.sort_values(by=["score", "popularity"], ascending=[True, False])
    filtered = filtered.drop_duplicates(subset=["track_name", "artists"])
    result = filtered[["track_name", "artists", "popularity", "track_genre", "score"]].head(limit)
    
    return result

if __name__ == "__main__":
    mood = input("Enter your mood: ")
    genre = input("Enter a genre (or press Enter to skip): ")
    songs = recommend_songs(mood, genre=genre if genre else None)
    
    print(f"\nTop songs for '{mood}' mood:\n")
    for i, (_, row) in enumerate(songs.iterrows(), 1):
        # Fetch Last.fm data for each song
        info = get_track_info(row["track_name"], row["artists"].split(";")[0])
        
        print(f"{i}. {row['track_name']} — {row['artists']}")
        if info:
            print(f"   🎧 {int(row['popularity'])} popularity | {int(info['listeners']):,} Last.fm listeners")
            print(f"   🏷  {', '.join(info['tags'])}")
            print(f"   🔗 {info['url']}")
        print()