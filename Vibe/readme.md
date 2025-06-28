# 🎵 Vibe Music Recommendation Engine

A sleek, modern music player that generates personalized playlists based on your listening habits. This web app, powered by Python and Flask, focuses on artist discovery, creating dynamic recommendations from a curated local library of songs.

-----

## 📌 Core Features

  * **🎧 Interactive Music Player**: Play high-quality audio from a curated library, complete with a dynamic progress bar and full playback controls (Next, Previous, Play/Pause).
  * **🧠 Smart Artist-Centric AI**: The app learns which artists you like as you listen. Your personalized playlist is a mix of other songs by all the artists you've explored.
  * **✨ "Discovery Mix" Mode**: If you play a song by an artist with no other tracks in our library, the app generates a special "Discovery Mix" with one song from every other artist, helping you find new music.
  * **🧊 Glassmorphic UI**: A stunning, modern frontend built with CSS glassmorphism, featuring blur, transparency, and glowing interactive elements.
  * **🚀 Standalone & Robust**: Runs entirely without external APIs, using a local song library. This makes it fast, reliable, and easy to deploy.

-----

## 🧱 Tech Stack

| Layer | Technology Used |
| :-------- | :-------------------------------------------- |
| Frontend | HTML, CSS (Glassmorphism), JavaScript (ES6) |
| Backend | Python, Flask |
| Data | Pandas (for in-memory data management) |
| Audio | Cloud-hosted MP3s (e.g., Cloudinary) |
| Deployment| Render.com, Heroku, or any Python-hosting service |

-----

## 🎨 Glassmorphic Design

This app uses a clean **glassmorphism-inspired UI** to create a beautiful, modern feel:

  * Frosted-glass containers with blurred backgrounds.
  * Subtle glowing borders on interactive elements.
  * A clean, minimalist layout that focuses on the music.

Example CSS from `app/static/css/style.css`:

```css
.glass-card {
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  background: rgba(0, 0, 0, 0.2);
  border-radius: 24px;
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 2rem;
  color: white;
}
```

-----

## 📖 Project Structure

The project is organized for simplicity and scalability. The complex AI logic has been streamlined and now lives entirely on the frontend.

```
Vibe/
├── app/
│   ├── __init__.py           # Creates the Flask app
│   ├── routes.py             # Serves the main page and song data
│   ├── static/
│   │   ├── css/style.css     # All styles for the app
│   │   ├── js/main.js        # Core frontend logic and player controls
│   │   └── img/
│   │       ├── placeholder.png
│   │       └── favicon.ico
│   └── templates/
│       └── index.html        # The main (and only) HTML page
├── data/
│   └── song_library.csv      # The heart of the app! All track info is here.
├── requirements.txt
├── run.py                    # Entry point to run the Flask app
└── .gitignore
```

-----

## 🚀 Getting Started

### 1\. Clone the Repository

```bash
git clone https://github.com/mehtahrishi/Vibe.git
```

### 2\. Set Up Your Music Library

This is the most important step for personalization.

1.  Upload your MP3 song files to a cloud service like Cloudinary.
2.  Open `data/song_library.csv`.
3.  For each song, paste the public URL into the `cloudinary_url` column.

### 3\. Create a Virtual Environment & Install Dependencies

```bash
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt
```

### 4\. Run the App Locally

```bash
python run.py
```

Visit `http://127.0.0.1:5000` in your browser and enjoy your personalized music discovery engine\!

-----

## 💡 How Recommendations Work

The app uses a session-based, artist-centric recommendation model that runs entirely in your browser.

1.  **Load Library**: When the app starts, the entire `song_library.csv` is loaded into the browser's memory.
2.  **Track Interests**: When you click on a song, the JavaScript adds the song's artist to a temporary "interest list" for your current session.
3.  **Generate Playlist**: When you click "Get Recommendations," the JavaScript:
    a. Filters the main song library to find all songs by the artists in your interest list.
    b. Removes songs you've already played in this session.
    c. Displays the result as your personalized playlist.
4.  **Discovery Mix**: As a fallback, if you listen to an artist with only one song in our library, the app generates a "Discovery Mix" containing one random song from every other artist, ensuring you always have something new to explore.

This approach is fast, stateless, and requires no complex backend AI or databases, making it incredibly robust.

-----

## 🙋‍♂️ Contributing

Feel free to fork this repository, make it your own, and submit pull requests with new features or improvements. All ideas are welcome\!

-----

## 🚫 License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

-----

## 🚀 Author

Built by Hrishi Mehta with a passion for Python & Music ❤️