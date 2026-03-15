import anthropic
from config import ANTHROPIC_API_KEY

client = anthropic.Anthropic(api_key = ANTHROPIC_API_KEY)

def parse_mood(user_input):
    user_input = user_input.lower()
    
    mood_keywords = {
        "happy": ["happy", "joy", "excited", "great", "wonderful", "cheerful", "good", "fantastic", "elated"],
        "sad": ["sad", "down", "depressed", "unhappy", "melancholic", "gloomy", "miserable", "heartbroken"],
        "energetic": ["energetic", "pumped", "hyped", "motivated", "active", "fired up", "ready", "electric", "dance", "party", "dancing", "wild", "crazy", "hype"],
        "calm": ["calm", "relaxed", "peaceful", "chill", "serene", "quiet", "tranquil", "easy"],
        "angry": ["angry", "furious", "mad", "frustrated", "annoyed", "rage", "irritated", "livid"],
        "nostalgic": ["nostalgic", "memories", "throwback", "old times", "reminiscing", "miss", "past"],
        "romantic": ["romantic", "love", "affectionate", "crush", "dreamy", "intimate", "passionate"]
    }
    
    # Count keyword matches per mood
    scores = {mood: 0 for mood in mood_keywords}
    for mood, keywords in mood_keywords.items():
        for keyword in keywords:
            if keyword in user_input:
                scores[mood] += 1
    
    # Return mood with highest score, default to calm if nothing matches
    best_mood = max(scores, key=lambda x: scores[x])
    if scores[best_mood] == 0:
        return "calm"
    return best_mood

# Test it
if __name__ == "__main__":
    test_inputs = [
        "I'm feeling really down and melancholic today",
        "I want to dance and party all night",
        "feeling peaceful and relaxed"
    ]
    for inp in test_inputs:
        print(f"'{inp}' → {parse_mood(inp)}")