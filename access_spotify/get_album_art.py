"""
This script downloads all the album art (high resolution) for an artist from Spotify
"""

import os.path
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import urllib.request
from PIL import Image


def get_album_art(album_name, album_img_url_dict, album_cover_path):
    """Downloads and saves highest resolution album artwork for the specified album

    :param album_name: Album name
    :type album_name: str
    :param album_img_url_dict: Dictionary mapping album names to album cover urls
    :type album_img_url_dict: dict
    :param album_cover_path: Path to save album images to
    :type album_cover_path: str
    :returns: Album cover
    :rtype: image file

    """

    print(f"Downloading album cover for {album_name}")

    # Get album cover
    url = album_img_url_dict[album_name]
    image = Image.open(urllib.request.urlopen(url))

    image.save(f"{album_cover_path}/{album_name}_art.png")

    return image

