import os  # 'os' kütüphanesini import et (Ortam Değişkenleri için)
from flask import Flask, render_template, request, redirect, session, url_for
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup
from functools import wraps
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)


app.secret_key = os.environ.get("SECRET_KEY")
CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.environ.get("REDIRECT_URI")
# --------------------------------

SCOPE = "playlist-modify-private"

# Spotipy OAuth
sp_oauth = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,

)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token_info = session.get('token_info', None)
        if not token_info:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    """Ana sayfa - Tarih formunu veya giriş sayfasını gösterir."""
    token_info = session.get('token_info', None)
    if not token_info:
     
        return render_template('login.html')
    
    return render_template('index.html')


@app.route('/login')
def login():
    """Kullanıcıyı Spotify giriş sayfasına yönlendirir."""
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)


@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)


    session['token_info'] = token_info

    return redirect(url_for('index'))


@app.route('/create_playlist', methods=['POST'])
@login_required
def create_playlist():
    """Formdan gelen tarih ile Billboard listesini çeker ve Spotify listesi oluşturur."""


    token_info = session.get('token_info', None)
    if not token_info:
        return redirect(url_for('login'))

    if sp_oauth.is_token_expired(token_info):
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
        session['token_info'] = token_info


    sp = spotipy.Spotify(auth=token_info['access_token'])
    user_id = sp.current_user()["id"]


    date = request.form['date']

    chart_type = request.form.get('chart_type', 'global')

    if chart_type == 'turkce':
        billboard_url = f"https://www.billboard.com/charts/turkey-songs-hotw/{date}"
        playlist_name = f"{date} Turkey Songs"
    elif chart_type == 'hiphop':
        billboard_url = f"https://www.billboard.com/charts/r-b-hip-hop-songs/{date}"
        playlist_name = f"{date} R&B/Hip-Hop"
    elif chart_type == 'pop':
        billboard_url = f"https://www.billboard.com/charts/pop-songs/{date}"
        playlist_name = f"{date} Pop Songs"
    else:  # 'global'
        billboard_url = f"https://www.billboard.com/charts/hot-100/{date}"
        playlist_name = f"{date} Billboard 100"
    # ...

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"}


    response = requests.get(url=billboard_url, headers=header)

    soup = BeautifulSoup(response.text, 'html.parser')
    song_names_spans = soup.select("li ul li h3")
    song_names = [song.getText().strip() for song in song_names_spans]


    song_uris = []
    year = date.split("-")[0]
    songs_not_found = []

    for song in song_names:
        result = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            songs_not_found.append(song)

   
    if song_uris:

        playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
        sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


        return render_template('success.html', playlist_url=playlist['external_urls']['spotify'], date=date)
    else:

        if not song_names:
            return "Bu tarih için Billboard listesi bulunamadı. Lütfen farklı bir tarih deneyin."
        return "Listeden hiçbir şarkı Spotify'da bulunamadı."



if __name__ == '__main__':
    app.run(debug=True, port=5000)
