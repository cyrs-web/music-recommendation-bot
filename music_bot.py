import random
import sys

# Ensure UTF-8 output encoding for Windows terminals
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


# ==========================================
# 1. PREDEFINED SONG DATABASE
# ==========================================
# Stored as a list of dictionaries. Each song contains title, artist, genre, and mood.
SONGS = [
    # Happy / Energetic
    {"title": "Happy", "artist": "Pharrell Williams", "genre": "Pop", "mood": "happy"},
    {"title": "Can't Stop the Feeling!", "artist": "Justin Timberlake", "genre": "Pop", "mood": "happy"},
    {"title": "Don't Stop Me Now", "artist": "Queen", "genre": "Rock", "mood": "happy"},
    {"title": "Uptown Funk", "artist": "Mark Ronson ft. Bruno Mars", "genre": "Pop", "mood": "happy"},
    {"title": "Good as Hell", "artist": "Lizzo", "genre": "Hip-Hop", "mood": "happy"},
    {"title": "Walking on Sunshine", "artist": "Katrina and the Waves", "genre": "Pop", "mood": "happy"},
    {"title": "Levitating", "artist": "Dua Lipa", "genre": "Pop", "mood": "energetic"},
    {"title": "Eye of the Tiger", "artist": "Survivor", "genre": "Rock", "mood": "energetic"},
    {"title": "Stronger", "artist": "Kanye West", "genre": "Hip-Hop", "mood": "energetic"},
    {"title": "Till I Collapse", "artist": "Eminem", "genre": "Hip-Hop", "mood": "energetic"},
    {"title": "One More Time", "artist": "Daft Punk", "genre": "Electronic", "mood": "energetic"},

    # Sad / Melancholic
    {"title": "Someone Like You", "artist": "Adele", "genre": "Pop", "mood": "sad"},
    {"title": "Fix You", "artist": "Coldplay", "genre": "Rock", "mood": "sad"},
    {"title": "All Too Well", "artist": "Taylor Swift", "genre": "Pop", "mood": "sad"},
    {"title": "When the Party's Over", "artist": "Billie Eilish", "genre": "Pop", "mood": "sad"},
    {"title": "The Night We Met", "artist": "Lord Huron", "genre": "Indie", "mood": "sad"},
    {"title": "Skinny Love", "artist": "Bon Iver", "genre": "Indie", "mood": "sad"},
    {"title": "Tears in Heaven", "artist": "Eric Clapton", "genre": "Rock", "mood": "sad"},

    # Relaxed / Chill
    {"title": "Weightless", "artist": "Marconi Union", "genre": "Ambient", "mood": "relaxed"},
    {"title": "Sunflower", "artist": "Post Malone & Swae Lee", "genre": "Hip-Hop", "mood": "relaxed"},
    {"title": "Banana Pancakes", "artist": "Jack Johnson", "genre": "Indie", "mood": "relaxed"},
    {"title": "Put Your Records On", "artist": "Corinne Bailey Rae", "genre": "R&B", "mood": "relaxed"},
    {"title": "Beyond", "artist": "Leon Bridges", "genre": "R&B", "mood": "relaxed"},
    {"title": "Location", "artist": "Khalid", "genre": "R&B", "mood": "relaxed"},
    {"title": "So What", "artist": "Miles Davis", "genre": "Jazz", "mood": "relaxed"},
    {"title": "Take Five", "artist": "Dave Brubeck", "genre": "Jazz", "mood": "relaxed"},

    # Focus / Study
    {"title": "Coffee Breath", "artist": "Kina", "genre": "Lo-Fi", "mood": "focus"},
    {"title": "Affection", "artist": "Jinsang", "genre": "Lo-Fi", "mood": "focus"},
    {"title": "Clair de Lune", "artist": "Claude Debussy", "genre": "Classical", "mood": "focus"},
    {"title": "Gymnopédie No. 1", "artist": "Erik Satie", "genre": "Classical", "mood": "focus"},
    {"title": "Snowman", "artist": "Wun Two", "genre": "Lo-Fi", "mood": "focus"},
    {"title": "Nuvole Bianche", "artist": "Ludovico Einaudi", "genre": "Classical", "mood": "focus"},

    # Romantic
    {"title": "Perfect", "artist": "Ed Sheeran", "genre": "Pop", "mood": "romantic"},
    {"title": "Thinking Out Loud", "artist": "Ed Sheeran", "genre": "Pop", "mood": "romantic"},
    {"title": "Lover", "artist": "Taylor Swift", "genre": "Pop", "mood": "romantic"},
    {"title": "At Last", "artist": "Etta James", "genre": "R&B", "mood": "romantic"},
    {"title": "Fly Me to the Moon", "artist": "Frank Sinatra", "genre": "Jazz", "mood": "romantic"},
    {"title": "Until I Found You", "artist": "Stephen Sanchez", "genre": "Indie", "mood": "romantic"},
    {"title": "Make You Feel My Love", "artist": "Adele", "genre": "Pop", "mood": "romantic"},
]

# Unique lists of available categories for easy lookup and display
ALL_MOODS = sorted(list({song["mood"].lower() for song in SONGS}))
ALL_GENRES = sorted(list({song["genre"].lower() for song in SONGS}))
ALL_ARTISTS = sorted(list({song["artist"] for song in SONGS}))


# ==========================================
# 2. RECOMMENDATION HELPER FUNCTIONS
# ==========================================

def get_recommendations_by_mood(mood_query, count=4):
    """Filter songs matching the given mood."""
    mood_query = mood_query.strip().lower()
    matches = [song for song in SONGS if song["mood"].lower() == mood_query]
    # Sample up to 'count' random songs from the matches
    return random.sample(matches, min(len(matches), count)) if matches else []


def get_recommendations_by_genre(genre_query, count=4):
    """Filter songs matching the given genre (case-insensitive substring/exact)."""
    genre_query = genre_query.strip().lower()
    matches = [song for song in SONGS if genre_query in song["genre"].lower()]
    return random.sample(matches, min(len(matches), count)) if matches else []


def get_recommendations_by_artist(artist_query, count=4):
    """Filter songs matching the given artist (case-insensitive partial match)."""
    artist_query = artist_query.strip().lower()
    matches = [song for song in SONGS if artist_query in song["artist"].lower()]
    return random.sample(matches, min(len(matches), count)) if matches else []


def get_random_recommendations(count=4):
    """Return a random selection of songs."""
    return random.sample(SONGS, min(len(SONGS), count))


def format_song_list(song_list):
    """Format a list of song dictionaries into a clean, numbered string."""
    if not song_list:
        return "No songs found."
    
    formatted_output = []
    for index, song in enumerate(song_list, start=1):
        formatted_output.append(
            f"  {index}. 🎵 \"{song['title']}\" by {song['artist']} [{song['genre']} | Mood: {song['mood'].capitalize()}]"
        )
    return "\n".join(formatted_output)


# ==========================================
# 3. INTERACTIVE CHATBOT INTERFACE
# ==========================================

def print_banner():
    """Print the welcome banner for the bot."""
    print("=" * 60)
    print("        🎶 Welcome to MelodyBot - Music Recommender 🎶")
    print("=" * 60)
    print("Hello! I am your personal music assistant.")
    print("Tell me your current mood, a favorite genre, or an artist,")
    print("and I will recommend 3-5 great tracks for you!\n")


def display_options():
    """Show available moods, genres, and sample artists."""
    print("\n--- Available Options ---")
    print(f"🎭 Moods   : {', '.join(mood.capitalize() for mood in ALL_MOODS)}")
    print(f"🎸 Genres  : {', '.join(genre.capitalize() for genre in ALL_GENRES)}")
    print("💡 Commands: 'mood', 'genre', 'artist', 'random', 'help', 'exit'")
    print("-------------------------\n")


def handle_mood_flow():
    """Interactive flow to recommend songs by mood."""
    print(f"\nAvailable moods: {', '.join(m.capitalize() for m in ALL_MOODS)}")
    user_mood = input("What's your mood right now? > ").strip()
    
    if not user_mood:
        print("You didn't enter a mood! Let's try again.\n")
        return

    results = get_recommendations_by_mood(user_mood)
    if results:
        print(f"\n🎧 Here are some {user_mood.capitalize()} tracks for you:")
        print(format_song_list(results))
        print("\nEnjoy the tunes! ✨\n")
    else:
        print(f"\n🤔 I don't have songs categorized under '{user_mood}' yet.")
        print(f"Try one of these moods: {', '.join(m.capitalize() for m in ALL_MOODS)}")
        print("Or type 'random' to discover something unexpected!\n")


def handle_genre_flow():
    """Interactive flow to recommend songs by genre."""
    print(f"\nAvailable genres: {', '.join(g.capitalize() for g in ALL_GENRES)}")
    user_genre = input("What genre would you like to listen to? > ").strip()
    
    if not user_genre:
        print("You didn't enter a genre! Let's try again.\n")
        return

    results = get_recommendations_by_genre(user_genre)
    if results:
        print(f"\n🎸 Here are some top {user_genre.capitalize()} recommendations:")
        print(format_song_list(results))
        print("\nTurn up the volume! 🔊\n")
    else:
        print(f"\n🤔 I couldn't find any songs in the '{user_genre}' genre.")
        print(f"Available genres include: {', '.join(g.capitalize() for g in ALL_GENRES)}\n")


def handle_artist_flow():
    """Interactive flow to recommend songs by artist."""
    user_artist = input("\nWhich artist are you looking for? > ").strip()
    
    if not user_artist:
        print("You didn't enter an artist name! Let's try again.\n")
        return

    results = get_recommendations_by_artist(user_artist)
    if results:
        print(f"\n🎤 Here are songs by or featuring '{user_artist}':")
        print(format_song_list(results))
        print("\nGreat choice of artist! ⭐\n")
    else:
        print(f"\n🤔 I couldn't find any songs by '{user_artist}' in my catalog.")
        print("Sample artists in my catalog include: Adele, Queen, Ed Sheeran, Taylor Swift, Billie Eilish, Daft Punk, Miles Davis.")
        print("Feel free to try another artist or search by mood/genre!\n")


def handle_random_flow():
    """Recommend a random selection of songs."""
    results = get_random_recommendations(count=4)
    print("\n🎲 Here is a hand-picked surprise mix for you:")
    print(format_song_list(results))
    print("\nHope you find a new favorite! 🚀\n")


def parse_freeform_input(user_input):
    """
    Attempt to smartly identify if user input directly matches
    a mood, genre, artist, or command.
    """
    cleaned = user_input.strip().lower()

    # Direct command matching
    if cleaned in ["1", "mood", "by mood"]:
        return "mood", None
    if cleaned in ["2", "genre", "by genre"]:
        return "genre", None
    if cleaned in ["3", "artist", "by artist"]:
        return "artist", None
    if cleaned in ["4", "random", "surprise", "surprise me", "shuffle"]:
        return "random", None
    if cleaned in ["help", "options", "menu"]:
        return "help", None
    if cleaned in ["exit", "quit", "bye", "goodbye", "q"]:
        return "exit", None

    # Check if user typed a specific mood directly (e.g., "happy" or "i feel sad")
    for mood in ALL_MOODS:
        if mood in cleaned:
            return "direct_mood", mood

    # Check if user typed a specific genre directly (e.g., "rock" or "play jazz")
    for genre in ALL_GENRES:
        if genre in cleaned:
            return "direct_genre", genre

    # Check if user typed an artist directly
    for artist in ALL_ARTISTS:
        if artist.lower() in cleaned:
            return "direct_artist", artist

    return "unknown", user_input


def main():
    """Main chatbot interaction loop."""
    print_banner()

    while True:
        print("How would you like music recommendations today?")
        print("  [1] By Mood (happy, sad, relaxed, focus, energetic, romantic)")
        print("  [2] By Genre (pop, rock, jazz, hip-hop, lo-fi, r&b, etc.)")
        print("  [3] By Artist (search your favorite singer or band)")
        print("  [4] Surprise Me (random mix)")
        print("  (Type 'exit' to quit or 'help' to see all categories)")
        
        user_choice = input("\nEnter your choice or type what you want > ").strip()
        if not user_choice:
            continue

        action, param = parse_freeform_input(user_choice)

        if action == "exit":
            print("\n👋 Thanks for hanging out with MelodyBot! Have a musical day! 🎵\n")
            break

        elif action == "help":
            display_options()

        elif action == "mood":
            handle_mood_flow()

        elif action == "genre":
            handle_genre_flow()

        elif action == "artist":
            handle_artist_flow()

        elif action == "random":
            handle_random_flow()

        elif action == "direct_mood":
            results = get_recommendations_by_mood(param)
            print(f"\n🎧 Recognized mood '{param.capitalize()}'! Here are your recommendations:")
            print(format_song_list(results))
            print("\nEnjoy! ✨\n")

        elif action == "direct_genre":
            results = get_recommendations_by_genre(param)
            print(f"\n🎸 Recognized genre '{param.capitalize()}'! Here are your recommendations:")
            print(format_song_list(results))
            print("\nEnjoy! 🔊\n")

        elif action == "direct_artist":
            results = get_recommendations_by_artist(param)
            print(f"\n🎤 Recognized artist '{param}'! Here are your recommendations:")
            print(format_song_list(results))
            print("\nEnjoy! ⭐\n")

        else:
            print(f"\n🤔 I'm not sure how to match '{user_choice}'.")
            print("You can pick a number [1-4], type a mood (e.g. 'happy', 'chill'), a genre (e.g. 'rock', 'lo-fi'),")
            print("or type 'help' to see all supported options.\n")


if __name__ == "__main__":
    main()
