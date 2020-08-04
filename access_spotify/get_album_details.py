"""
This script gets the details for all of the specified artist's albums

"""

import os.path
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def get_album_details(sp, artist_name):
    """Gets details for all of the albums for the specified artist

    :param sp: Spotify object
    :type sp: object
    :param artist_name: Artist to query for
    :type artist_name: str
    :returns: album_names: List of album names
        album_name_dict: Dictionary mapping album names to album uri values
        album_img_url_dict: Dictionary mapping album names to album cover urls
    :rtype: (list, dict, dict)

    """

    result = sp.search(artist_name)  # search query

    # Extract Artist's uri
    artist_uri = result["tracks"]["items"][0]["artists"][0]["uri"]

    # Pull all of the artist's albums
    sp_albums = sp.artist_albums(artist_uri, album_type="album")
    # CHECK THAT ALL THE ALBUMS ARE BEING DOWNLOADED -- MIGHT BE A BUG
    # Store artist's albums' names' and uris in separate lists
    album_names = []
    album_uris = []
    album_img_urls = []
    for i in range(len(sp_albums["items"])):
        album_names.append(sp_albums["items"][i]["name"])
        album_uris.append(sp_albums["items"][i]["uri"])
        album_img_urls.append(sp_albums["items"][i]["images"][0]["url"])

    album_name_dict = dict(zip(album_names, album_uris))
    album_img_url_dict = dict(zip(album_names, album_img_urls))

    return album_names, album_name_dict, album_img_url_dict

