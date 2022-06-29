import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

scope = "playlist-modify-public"
username = "bennisteinmueller"

token = SpotifyOAuth(scope=scope, username=username)
spotifyObject = spotipy.Spotify(auth_manager=token)

plname = input("Enter name")


# playlists = spotifyObject.user_playlists(username)
# trackids = playlists["items"][0]["id"]
# print(trackids)


tracks = spotifyObject.playlist_tracks(
    "37i9dQZEVXcDYET2LCFeAo",
    fields=None,
    limit=100,
    offset=0,
    market=None,
    additional_types=("track", "episode"),
)

trackids = []

for i in range(30):
    trackids.append(tracks["items"][i]["track"]["uri"])


spotifyObject.playlist_add_items("2tPmW96s1cZK1OLNAJIwEY", trackids, position=None)

# 2tPmW96s1cZK1OLNAJIwEY
