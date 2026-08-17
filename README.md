# 🎵 MelodyBot - Python Music Recommendation Chatbot

A simple, beginner-friendly command-line music recommender chatbot written in Python. It requires no external libraries or APIs and runs directly in any terminal.

---

## ✨ Features

- **Mood-Based Recommendations**: Recommends songs for moods like *Happy, Sad, Relaxed, Focus, Energetic, and Romantic*.
- **Genre-Based Filtering**: Search tracks across *Pop, Rock, Hip-Hop, Jazz, Lo-Fi, R&B, Classical, and Indie*.
- **Artist Search**: Look up songs by your favorite artists with case-insensitive partial matching.
- **Surprise Me / Random Pick**: Shuffles and delivers a fresh mix of 3–5 tracks.
- **Friendly Fallback Handling**: If an input or mood is unknown, MelodyBot politely guides the user with available options.
- **Zero External Dependencies**: Pure standard Python 3.

---

## 🚀 How to Launch the Web UI (Browser)

1. Run the Python server script:
   ```bash
   python server.py
   ```
   It will **automatically open** in your default web browser at `http://localhost:5000`!
2. Alternatively, you can directly open `index.html` in your browser.



---

## 💻 How to Run the CLI Version (Terminal)

If you prefer chatting directly in your terminal command-line:
```bash
python music_bot.py
```


---

## 💡 How to Use

When you start MelodyBot, you can choose one of the menu numbers or type natural keywords:

- Type `1` or `mood` to search by mood.
- Type `2` or `genre` to search by genre.
- Type `3` or `artist` to search by artist name.
- Type `4` or `surprise me` to get a random mix.
- Type `help` to see all available moods and genres.
- Type `exit` or `quit` to exit the chat.

---

## 🎼 Adding Your Own Songs

You can easily expand the song catalog by opening `music_bot.py` and adding a new dictionary entry to the `SONGS` list:

```python
{"title": "Bohemian Rhapsody", "artist": "Queen", "genre": "Rock", "mood": "energetic"},
```

---

## 🧪 Running Tests

To verify all recommendation logic and tests, run:

```bash
python test_music_bot.py
```
