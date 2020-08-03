#!/usr/bin/env python

"""
The main script that runs the code, gets the Spotify API access, downloads the album art and data
"""

import os
import os.path
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from .get_spotify_access import get_spotify_credentials
from .get_album_details import get_album_details
from .get_album_art import get_album_art
from .get_album_data import get_album_audio_analysis, get_album_audio_features

from tqdm import tqdm


def run_all(artist_name, client_id, client_secret):
    """
    Runs all the methods to download all the album art and info for the specified artist

    :param artist_name: Name of artist
    :type artist_name: str
    :param client_id: Client ID for Spotify API Access
    :type client_id: str
    :param client_secret: Client Secret for Spotify API Access
    :type client_secret: str
    :returns: None
    """

    parent_dir = "./data"
    artist_dir = f"{artist_name}"
    base_path = os.path.join(parent_dir, artist_dir)

    # Define save-path for album art

    album_cover_dir = "Album_Art/"
    album_cover_path = os.path.join(base_path, album_cover_dir)
    try:
        os.makedirs(album_cover_path)
    except FileExistsError:
        pass

    # Define save-path for album analysis audio frames

    album_info_dir = "Album_Info/"
    album_info_path = os.path.join(base_path, album_info_dir)
    try:
        os.makedirs(album_info_path)
    except FileExistsError:
        pass

    sp = get_spotify_credentials(client_id=client_id, client_secret=client_secret)

    album_names, album_name_uri_dict, album_img_url_dict = get_album_details(sp=sp, artist_name=artist_name)

    for album_name in tqdm(album_names):

        get_album_art(album_name=album_name, album_img_url_dict=album_img_url_dict,
                      album_cover_path=album_cover_path)

    for album_name in tqdm(album_names):

        get_album_audio_features(sp=sp, album_name=album_name, album_name_dict=album_name_uri_dict,
                                 album_info_path=album_info_path)

        get_album_audio_analysis(sp=sp, album_name=album_name, album_name_dict=album_name_uri_dict,
                                 album_info_path=album_info_path)
