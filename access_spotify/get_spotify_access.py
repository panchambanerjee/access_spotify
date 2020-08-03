#!/usr/bin/env python

"""
This script uses the user's Client ID and Client Secret to get access to the Spotify ID
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# API Credentials

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from .spotify_credentials import CLIENT_SECRET, CLIENT_ID


def get_spotify_credentials(client_id, client_secret):
    """Takes in API credentials to start querying the Spotify API

    :param client_id: Spotify Client ID
    :type client_id: str
    :param client_secret: Spotify Client Secret
    :type client_secret: str
    :returns: sp: Spotify object
    :rtype: object

    """

    client_id = client_id
    client_secret = client_secret

    client_credentials_manager = SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    return sp


if __name__ == "__main__":
    sp = get_spotify_credentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
