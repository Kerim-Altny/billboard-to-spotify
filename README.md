

````markdown
# 🎵 Billboard to Spotify Converter

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Spotify](https://img.shields.io/badge/Spotify-1ED760?style=for-the-badge&logo=spotify&logoColor=white)

A powerful web application that travels back in time to fetch Billboard music charts and automatically converts them into a listenable Spotify Playlist.

> **Project Status:** MVP (Minimum Viable Product) - Active Development

## 📖 Overview

This project was inspired by a concept from a coding course. I took the core idea and **re-architected it into a full-stack Web Application** using Flask.

Instead of a simple CLI script, this tool offers a user-friendly interface where users can select specific dates and chart categories. It leverages AI tools for rapid frontend prototyping, allowing me to focus on **Backend Logic, API Integration, and OAuth 2.0 flows**.

## ✨ Features

* **📅 Time Travel:** Fetches song data from any specific date in history.
* **📊 Multiple Chart Support:**
    * Billboard Hot 100 (Global)
    * Turkey Songs
    * Pop Songs
    * R&B / Hip-Hop
* **🔐 Secure OAuth 2.0:** Integrates safely with Spotify API using user authentication (no password storage).
* **🤖 Smart Matching:** Automatically searches and matches Billboard songs with Spotify's database.
* **⚡ Session Management:** Uses Flask Sessions to handle tokens, so you don't need to login repeatedly.

## 🛠 Tech Stack

* **Backend:** Python 3.x, Flask
* **Scraping:** BeautifulSoup4 (bs4)
* **API:** Spotipy (Spotify Web API Wrapper)
* **Frontend:** HTML5, CSS3 (Prototyped with AI assistance)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/Kerim-Altny/billboard-to-spotify.git](https://github.com/Kerim-Altny/billboard-to-spotify.git)
cd billboard-to-spotify
````

### 2\. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3\. Spotify Configuration

To run this app, you need a Spotify Developer Account.

1.  Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2.  Create an app and get your **Client ID** and **Client Secret**.
3.  Click "Edit Settings" and add this **Redirect URI**:
    `http://127.0.0.1:5000/callback`

### 4\. Environment Variables

Create a `.env` file in the root directory and add your keys:

```ini
SPOTIPY_CLIENT_ID="your_client_id_here"
SPOTIPY_CLIENT_SECRET="your_client_secret_here"
SECRET_KEY="random_secret_key_for_flask"
REDIRECT_URI="[http://127.0.0.1:5000/callback](http://127.0.0.1:5000/callback)"
```

### 5\. Run the App

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## ⚠️ Known Issues & Limitations

  * **Song Mismatch:** Sometimes the exact song version on Billboard (e.g., specific remixes) isn't the top result on Spotify. In these cases, the algorithm skips the song to avoid adding incorrect tracks.
  * **Region Locks:** Some songs might be available on Billboard but locked in your Spotify region.

## 🗺 Roadmap

  * [ ] Add support for YouTube Music.
  * [ ] Improve UI/UX with a loading animation during the scraping process.
  * [ ] Optimize scraping speed with asynchronous requests.
  * [ ] Dockerize the application for easier deployment.

## 🤝 Contributing

Contributions are welcome\! Please feel free to submit a Pull Request.

-----

*Developed by Kerim Altınay*

```
```
