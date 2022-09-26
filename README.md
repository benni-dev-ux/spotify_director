# Spotify Director

Using the Spotify API via ![spotipy](https://github.com/plamere/spotipy) to copy songs from the automatically generated 'Discover Weekly' playlist to an archive.

[Application Screensot](doc/screen2_.png)

## Setup Guide

1. Register for a developer Account at

    <https://developer.spotify.com/>

2. Retrieve your client ID and secret from there and set it as envirenment variables in  your pipenv

    set SPOTIPY_CLIENT_ID=****YOUR CLIENT ID****

    set SPOTIPY_CLIENT_SECRET = ****YOUR CLIENT SECRET****

2. Set the redirect uri to localhost

    set SPOTIPY_REDIRECT_URI=****<http://127.0.0.1:8080/>****

## Work in Progress

Automatic upload of auto-generated cover images with date of last update.
