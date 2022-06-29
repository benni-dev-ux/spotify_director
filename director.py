import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

scope = "playlist-modify-public"
username = "bennisteinmueller"

discover_weekly_ID = "37i9dQZEVXcDYET2LCFeAo"
discover_weekly_archive_ID = "2tPmW96s1cZK1OLNAJIwEY"

token = SpotifyOAuth(scope=scope, username=username)
spotifyObject = spotipy.Spotify(auth_manager=token)


tracks = spotifyObject.playlist_tracks(
    discover_weekly_ID,
    fields=None,
    limit=100,
    offset=0,
    market=None,
    additional_types=("track", "episode"),
)

trackids = []

for i in range(30):
    trackids.append(tracks["items"][i]["track"]["uri"])


spotifyObject.playlist_add_items(discover_weekly_archive_ID, trackids, position=None)
