import spotipy
from spotipy.oauth2 import SpotifyOAuth


import tkinter as tk
from tkinter import ttk
import sv_ttk


class SpotifyDirectorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Spotify Discover Weekly Archiver")
        master.resizable(False, False)

        sv_ttk.use_light_theme()  # Set light theme

        self.label = ttk.Label(
            master, text="Spotify Discover Weekly Archiver", font="Helvetica 16 bold "
        )

        self.text = ttk.Label(
            master,
            text="Adds all songs from Discover Weekly to your Discover Weekly Archive",
            font="Helvetica 10 ",
        )

        self.close_button = ttk.Button(master, text="Close", command=master.quit)
        self.add_button = ttk.Button(
            master, text="Add Songs", command=self.add_songs_to_archive
        )
        self.add_button.focus()

        self.label.grid(columnspan=2, row=0, sticky=tk.W, padx=30, pady=15)
        self.text.grid(columnspan=2, row=1, sticky=tk.W, padx=30, pady=10)
        self.close_button.grid(row=2, column=0, padx=30, pady=20, sticky=tk.EW)
        self.add_button.grid(row=2, column=1, padx=30, pady=20, sticky=tk.EW)

    def add_songs_to_archive(self):
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

        spotifyObject.playlist_add_items(
            discover_weekly_archive_ID, trackids, position=None
        )

        print("Added new songs to your Discover Weekly Archive")


root = tk.Tk()


SD_GUI = SpotifyDirectorGUI(root)
root.mainloop()


# Create Cover and updating cover image

# scope = "ugc-image-upload"
# token = SpotifyOAuth(scope=scope, username=username)
# spotifyObject = spotipy.Spotify(auth_manager=token)
#
#
# cover_creator.create_cover()
# encoded = base64.b64encode(open("cover.jpeg", "rb").read())
# spotifyObject.playlist_upload_cover_image("1jAXcKJmLvHxk9OpMofCEI", encoded)
# print("Cover updated")
