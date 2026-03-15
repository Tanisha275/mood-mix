#spoify's audio features range from 0.0 to 1.0
# valence = happiness, energy = intensity, danceability = rhythm
mood_map = {
    "happy": {"valence": 0.8, "energy":0.7, "danceability": 0.7},
    "sad":  {"valence": 0.2, "energy":0.3, "danceability": 0.3},
    "energetic": {"valence": 0.6, "energy":0.9, "danceability": 0.8},
    "calm": {"valence": 0.5, "energy":0.2, "danceability": 0.3},
    "angry": {"valence": 0.1, "energy":0.9, "danceability": 0.5},
    "nostalgic": {"valence": 0.4, "energy":0.3, "danceability": 0.4},
    "romantic": {"valence": 0.7, "energy":0.4, "danceability": 0.5},   
}
def get_mood_features(mood):
    mood = mood.lower().strip()
    if mood in mood_map:
        return mood_map[mood]
    else:
        return None
