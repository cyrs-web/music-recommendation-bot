/**
 * MelodyBot - Client Logic & Recommendation Engine
 */

// ==========================================
// 1. SONG DATABASE (In-Memory)
// ==========================================
const SONGS = [
    // Happy / Energetic
    { title: "Happy", artist: "Pharrell Williams", genre: "Pop", mood: "happy" },
    { title: "Can't Stop the Feeling!", artist: "Justin Timberlake", genre: "Pop", mood: "happy" },
    { title: "Don't Stop Me Now", artist: "Queen", genre: "Rock", mood: "happy" },
    { title: "Uptown Funk", artist: "Mark Ronson ft. Bruno Mars", genre: "Pop", mood: "happy" },
    { title: "Good as Hell", artist: "Lizzo", genre: "Hip-Hop", mood: "happy" },
    { title: "Walking on Sunshine", artist: "Katrina and the Waves", genre: "Pop", mood: "happy" },
    { title: "Levitating", artist: "Dua Lipa", genre: "Pop", mood: "energetic" },
    { title: "Eye of the Tiger", artist: "Survivor", genre: "Rock", mood: "energetic" },
    { title: "Stronger", artist: "Kanye West", genre: "Hip-Hop", mood: "energetic" },
    { title: "Till I Collapse", artist: "Eminem", genre: "Hip-Hop", mood: "energetic" },
    { title: "One More Time", artist: "Daft Punk", genre: "Electronic", mood: "energetic" },

    // Sad / Melancholic
    { title: "Someone Like You", artist: "Adele", genre: "Pop", mood: "sad" },
    { title: "Fix You", artist: "Coldplay", genre: "Rock", mood: "sad" },
    { title: "All Too Well", artist: "Taylor Swift", genre: "Pop", mood: "sad" },
    { title: "When the Party's Over", artist: "Billie Eilish", genre: "Pop", mood: "sad" },
    { title: "The Night We Met", artist: "Lord Huron", genre: "Indie", mood: "sad" },
    { title: "Skinny Love", artist: "Bon Iver", genre: "Indie", mood: "sad" },
    { title: "Tears in Heaven", artist: "Eric Clapton", genre: "Rock", mood: "sad" },

    // Relaxed / Chill
    { title: "Weightless", artist: "Marconi Union", genre: "Ambient", mood: "relaxed" },
    { title: "Sunflower", artist: "Post Malone & Swae Lee", genre: "Hip-Hop", mood: "relaxed" },
    { title: "Banana Pancakes", artist: "Jack Johnson", genre: "Indie", mood: "relaxed" },
    { title: "Put Your Records On", artist: "Corinne Bailey Rae", genre: "R&B", mood: "relaxed" },
    { title: "Beyond", artist: "Leon Bridges", genre: "R&B", mood: "relaxed" },
    { title: "Location", artist: "Khalid", genre: "R&B", mood: "relaxed" },
    { title: "So What", artist: "Miles Davis", genre: "Jazz", mood: "relaxed" },
    { title: "Take Five", artist: "Dave Brubeck", genre: "Jazz", mood: "relaxed" },

    // Focus / Study
    { title: "Coffee Breath", artist: "Kina", genre: "Lo-Fi", mood: "focus" },
    { title: "Affection", artist: "Jinsang", genre: "Lo-Fi", mood: "focus" },
    { title: "Clair de Lune", artist: "Claude Debussy", genre: "Classical", mood: "focus" },
    { title: "Gymnopédie No. 1", artist: "Erik Satie", genre: "Classical", mood: "focus" },
    { title: "Snowman", artist: "Wun Two", genre: "Lo-Fi", mood: "focus" },
    { title: "Nuvole Bianche", artist: "Ludovico Einaudi", genre: "Classical", mood: "focus" },

    // Romantic
    { title: "Perfect", artist: "Ed Sheeran", genre: "Pop", mood: "romantic" },
    { title: "Thinking Out Loud", artist: "Ed Sheeran", genre: "Pop", mood: "romantic" },
    { title: "Lover", artist: "Taylor Swift", genre: "Pop", mood: "romantic" },
    { title: "At Last", artist: "Etta James", genre: "R&B", mood: "romantic" },
    { title: "Fly Me to the Moon", artist: "Frank Sinatra", genre: "Jazz", mood: "romantic" },
    { title: "Until I Found You", artist: "Stephen Sanchez", genre: "Indie", mood: "romantic" },
    { title: "Make You Feel My Love", artist: "Adele", genre: "Pop", mood: "romantic" },
];

const ALL_MOODS = [...new Set(SONGS.map(s => s.mood.toLowerCase()))].sort();
const ALL_GENRES = [...new Set(SONGS.map(s => s.genre.toLowerCase()))].sort();
const ALL_ARTISTS = [...new Set(SONGS.map(s => s.artist))].sort();

// ==========================================
// 2. DOM ELEMENTS
// ==========================================
const chatViewport = document.getElementById("chat-viewport");
const chatMessages = document.getElementById("chat-messages");
const chatForm = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");
const surpriseBtn = document.getElementById("surprise-btn");
const clearChatBtn = document.getElementById("clear-chat-btn");
const chipsScroll = document.getElementById("chips-scroll");

// ==========================================
// 3. RECOMMENDATION ENGINE
// ==========================================

function shuffleArray(array) {
    const arr = [...array];
    for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
}

function getMoodRecommendations(moodQuery, count = 4) {
    const q = moodQuery.trim().toLowerCase();
    const matches = SONGS.filter(s => s.mood.toLowerCase() === q);
    return shuffleArray(matches).slice(0, count);
}

function getGenreRecommendations(genreQuery, count = 4) {
    const q = genreQuery.trim().toLowerCase();
    const matches = SONGS.filter(s => s.genre.toLowerCase().includes(q));
    return shuffleArray(matches).slice(0, count);
}

function getArtistRecommendations(artistQuery, count = 4) {
    const q = artistQuery.trim().toLowerCase();
    const matches = SONGS.filter(s => s.artist.toLowerCase().includes(q));
    return shuffleArray(matches).slice(0, count);
}

function getRandomRecommendations(count = 4) {
    return shuffleArray(SONGS).slice(0, count);
}

// ==========================================
// 4. CHAT RENDERING HELPERS
// ==========================================

function scrollToBottom() {
    chatViewport.scrollTop = chatViewport.scrollHeight;
}

function formatCurrentTime() {
    const now = new Date();
    return now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

function appendUserMessage(text) {
    const row = document.createElement("div");
    row.className = "message-row user";
    row.innerHTML = `
        <div class="msg-avatar">👤</div>
        <div class="msg-content">
            <div class="msg-bubble">${escapeHTML(text)}</div>
            <span class="msg-timestamp">${formatCurrentTime()}</span>
        </div>
    `;
    chatMessages.appendChild(row);
    scrollToBottom();
}

function showTypingIndicator() {
    const row = document.createElement("div");
    row.className = "message-row bot typing-row";
    row.id = "typing-indicator";
    row.innerHTML = `
        <div class="msg-avatar">🤖</div>
        <div class="msg-content">
            <div class="msg-bubble">
                <div class="typing-dots">
                    <span class="typing-dot"></span>
                    <span class="typing-dot"></span>
                    <span class="typing-dot"></span>
                </div>
            </div>
        </div>
    `;
    chatMessages.appendChild(row);
    scrollToBottom();
}

function removeTypingIndicator() {
    const indicator = document.getElementById("typing-indicator");
    if (indicator) indicator.remove();
}

function appendBotResponse(headline, songList = [], footerMsg = "") {
    removeTypingIndicator();

    const row = document.createElement("div");
    row.className = "message-row bot";

    let songsHTML = "";
    if (songList && songList.length > 0) {
        songsHTML = `
            <div class="song-cards-container">
                ${songList.map((song, idx) => `
                    <div class="song-card">
                        <div class="song-info">
                            <span class="song-index">0${idx + 1}</span>
                            <div class="song-details">
                                <span class="song-title">${escapeHTML(song.title)}</span>
                                <span class="song-artist">${escapeHTML(song.artist)}</span>
                                <div class="song-tags">
                                    <span class="tag-pill tag-genre">${escapeHTML(song.genre)}</span>
                                    <span class="tag-pill tag-mood">${escapeHTML(song.mood)}</span>
                                </div>
                            </div>
                        </div>
                        <div class="waveform-bars">
                            <span class="wave-bar"></span>
                            <span class="wave-bar"></span>
                            <span class="wave-bar"></span>
                            <span class="wave-bar"></span>
                        </div>
                        <div class="song-actions">
                            <a href="https://open.spotify.com/search/${encodeURIComponent(song.title + ' ' + song.artist)}" target="_blank" rel="noopener noreferrer" class="action-link" title="Listen on Spotify">
                                🟢
                            </a>
                            <a href="https://www.youtube.com/results?search_query=${encodeURIComponent(song.title + ' ' + song.artist)}" target="_blank" rel="noopener noreferrer" class="action-link" title="Watch on YouTube">
                                ▶️
                            </a>
                        </div>
                    </div>
                `).join("")}
            </div>
        `;
    }

    row.innerHTML = `
        <div class="msg-avatar">🤖</div>
        <div class="msg-content">
            <div class="msg-bubble">
                <p>${headline}</p>
                ${songsHTML}
                ${footerMsg ? `<p style="margin-top: 10px; font-size: 0.88rem; color: #94a3b8;">${footerMsg}</p>` : ""}
            </div>
            <span class="msg-timestamp">${formatCurrentTime()}</span>
        </div>
    `;

    chatMessages.appendChild(row);
    scrollToBottom();
}

function escapeHTML(str) {
    const p = document.createElement("p");
    p.appendChild(document.createTextNode(str));
    return p.innerHTML;
}

// ==========================================
// 5. INTENT PROCESSING
// ==========================================

function processUserInput(rawInput) {
    const input = rawInput.trim();
    if (!input) return;

    appendUserMessage(input);
    userInput.value = "";
    showTypingIndicator();

    setTimeout(() => {
        const query = input.toLowerCase();

        // 1. Check for Help / Menu
        if (query === "help" || query === "options" || query === "menu" || query === "show all") {
            const moodList = ALL_MOODS.map(m => `<b>${capitalize(m)}</b>`).join(", ");
            const genreList = ALL_GENRES.map(g => `<b>${capitalize(g)}</b>`).join(", ");
            appendBotResponse(
                `Here are all the genres and moods in my catalog:<br><br>` +
                `🎭 <strong>Moods:</strong> ${moodList}<br>` +
                `🎸 <strong>Genres:</strong> ${genreList}<br><br>` +
                `You can also search for artists like <em>Queen, Adele, Taylor Swift, Ed Sheeran, Daft Punk, etc.</em>!`
            );
            return;
        }

        // 2. Check for Surprise / Random
        if (query.includes("surprise") || query.includes("random") || query === "shuffle" || query === "mix") {
            const songs = getRandomRecommendations(4);
            appendBotResponse("🎲 Here is a hand-picked surprise mix just for you:", songs, "Hope you discover a new favorite! ✨");
            return;
        }

        // 3. Check for direct mood match
        for (const mood of ALL_MOODS) {
            if (query.includes(mood)) {
                const songs = getMoodRecommendations(mood, 4);
                appendBotResponse(`🎧 Found great <strong>${capitalize(mood)}</strong> vibes for you:`, songs, "Turn up the volume! 🔊");
                return;
            }
        }

        // 4. Check for direct genre match
        for (const genre of ALL_GENRES) {
            if (query.includes(genre)) {
                const songs = getGenreRecommendations(genre, 4);
                appendBotResponse(`🎸 Here are some top <strong>${capitalize(genre)}</strong> tracks:`, songs, "Enjoy the groove! ✨");
                return;
            }
        }

        // 5. Check for artist match
        for (const artist of ALL_ARTISTS) {
            if (query.includes(artist.toLowerCase()) || artist.toLowerCase().includes(query)) {
                const songs = getArtistRecommendations(artist, 4);
                if (songs.length > 0) {
                    appendBotResponse(`🎤 Recommended tracks by <strong>${artist}</strong>:`, songs, "Great choice of artist! ⭐");
                    return;
                }
            }
        }

        // 6. Generic partial artist check
        const artistMatches = getArtistRecommendations(query, 4);
        if (artistMatches.length > 0) {
            appendBotResponse(`🎤 Found tracks matching "<strong>${escapeHTML(input)}</strong>":`, artistMatches, "Enjoy the music! 🎶");
            return;
        }

        // 7. Unknown Fallback
        appendBotResponse(
            `🤔 I couldn't find any songs matching "<strong>${escapeHTML(input)}</strong>".<br><br>` +
            `Try asking for a mood (<em>Happy, Chill, Relaxed, Focus</em>), a genre (<em>Pop, Rock, Lo-Fi, Jazz</em>), or click <strong>Surprise Me</strong>!`
        );

    }, 350);
}

function capitalize(s) {
    return s.charAt(0).toUpperCase() + s.slice(1);
}

// ==========================================
// 6. EVENT LISTENERS
// ==========================================

chatForm.addEventListener("submit", (e) => {
    e.preventDefault();
    processUserInput(userInput.value);
});

// Quick Chips click handler
document.addEventListener("click", (e) => {
    const chip = e.target.closest(".chip");
    if (!chip) return;

    if (chip.classList.contains("intro-chip")) {
        const query = chip.getAttribute("data-query");
        processUserInput(query);
        return;
    }

    const type = chip.getAttribute("data-type");
    const val = chip.getAttribute("data-value");

    if (type === "mood" || type === "genre") {
        processUserInput(val);
    } else if (type === "action") {
        if (val === "random") {
            processUserInput("surprise me");
        } else if (val === "help") {
            processUserInput("help");
        }
    }
});

// Top bar Surprise Me button
surpriseBtn.addEventListener("click", () => {
    processUserInput("surprise me");
});

// Clear Chat button
clearChatBtn.addEventListener("click", () => {
    chatMessages.innerHTML = `
        <div class="message-row bot">
            <div class="msg-avatar">🤖</div>
            <div class="msg-content">
                <div class="msg-bubble">
                    <p><strong>Chat reset! 🎶</strong> What vibe or genre are you in the mood for?</p>
                </div>
                <span class="msg-timestamp">Just now</span>
            </div>
        </div>
    `;
});
