import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cover_creator
import base64


scope = "playlist-modify-public"
username = "bennisteinmueller"

discover_weekly_ID = "37i9dQZEVXcDYET2LCFeAo"
discover_weekly_archive_ID = "1jAXcKJmLvHxk9OpMofCEI"

token = SpotifyOAuth(scope=scope, username=username)
spotifyObject = spotipy.Spotify(auth_manager=token)

tracks = spotifyObject.playlist_items(
    discover_weekly_ID,
    fields=None,
    limit=100,
    offset=0,
    market=None,
    additional_types=("track", "episode"),
)

trackids = []

length = len(tracks["items"])

for i in range(length):
    trackids.append(tracks["items"][i]["track"]["uri"])

spotifyObject.playlist_add_items(discover_weekly_archive_ID, trackids, position=None)

print("Added new songs to your Discover Weekly Archive")

#Create Cover and updating cover image

#scope = "ugc-image-upload"
#token = SpotifyOAuth(scope=scope, username=username)
#spotifyObject = spotipy.Spotify(auth_manager=token)
#
#
#cover_creator.create_cover()
#encoded = base64.b64encode(open("cover.jpeg", "rb").read())
#spotifyObject.playlist_upload_cover_image("1jAXcKJmLvHxk9OpMofCEI", encoded)
#print("Cover updated")


