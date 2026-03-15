# 🎵 Mood Mix

I used to make Spotify playlists for my friend whenever she was feeling down — something to cheer her up, or at least keep her company when she needed it. Mood Mix is that idea, expanded.

It's a mood-based song recommendation web app with a simple, welcoming UI designed to feel less like a tool and more like a friend who just gets what you need to hear right now.

## What it does
- Pick a mood from the vinyl disk UI or just type how you're feeling in your own words
- Get 10 song recommendations matched by audio features across a dataset of 114,000 songs
- See real-time listener data pulled live from Last.fm
- Play songs directly inside the app via an embedded YouTube player

## The build
This started as a Spotify API project — until Spotify decided new developer accounts couldn't access basic search without a Premium subscription. So I pivoted: built a local recommendation engine using pandas on a 114k song dataset, integrated Last.fm for live data, and added YouTube for playback.

The UI went through its own journey too — started in Streamlit, hit its limitations fast when I wanted real interactivity, and rebuilt the whole thing properly with Flask, HTML, CSS and JavaScript.

## Tech Stack
- **Backend:** Python, Flask, pandas
- **APIs:** Last.fm, YouTube Data API v3
- **Dataset:** Spotify Tracks Dataset (114k songs)
- **Frontend:** HTML, CSS, JavaScript

## Run it locally
1. Clone the repo
2. Create a virtual environment: `python3 -m venv .venv`
3. Activate it: `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file using `.env.example` as a template
6. Run: `python3 app.py`
7. Open `http://127.0.0.1:5000`

## Notes
You'll need your own API keys for Last.fm and YouTube Data API v3 — both are free. See `.env.example` for the required variables.