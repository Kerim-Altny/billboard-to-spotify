# 🎵 Billboard to Spotify Converter

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Spotify](https://img.shields.io/badge/Spotify-1ED760?style=for-the-badge&logo=spotify&logoColor=white)

A powerful web application that travels back in time to fetch Billboard music charts and automatically converts them into a listenable Spotify Playlist.

> **Project Status:** MVP (Minimum Viable Product) - Active Development

## 📖 Overview

This project was originally inspired by a Python scripting concept from a Udemy course. I took the core idea and **re-architected it into a full-stack Web Application** using Flask.

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