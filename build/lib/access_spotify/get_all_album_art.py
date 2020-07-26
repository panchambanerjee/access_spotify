"""
This script downloads all the album art (high resolution) for an artist from Spotify
"""

from tqdm import tqdm
import urllib.request
from PIL import Image


def get_all_album_art(album_names, album_img_url_dict, album_cover_path):
    """Downloads and saves highest resolution album artwork for all albums

    :param album_names: List of the album names
    :type album_names: list
    :param album_img_url_dict: Dictionary mapping album names to album cover urls
    :type album_img_url_dict: dict
    :param album_cover_path: Path to save album images to
    :type album_cover_path: str
    :returns: None

    """

    for album_name in tqdm(album_names):
        print(f"Downloading album cover for {album_name}")

        # Get album cover
        url = album_img_url_dict[album_name]
        image = Image.open(urllib.request.urlopen(url))

        image.save(f"{album_cover_path}/{album_name}_art.png")

