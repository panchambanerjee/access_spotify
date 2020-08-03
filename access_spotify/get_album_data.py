"""
This script downloads all the album data (audio features and audio analysis) for an artist from Spotify
"""

import os.path
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tqdm import tqdm
import pandas as pd


def get_album_audio_features(sp, album_name, album_name_dict, album_info_path):
    """Get audio features data for all albums for the given artists and pickle the data-frames

    :param sp: Spotify object
    :type sp: object
    :param album_name: List of album names
    :type album_name: list
    :param album_name_dict: Dictionary mapping album names to album uri values
    :type album_name_dict: dict
    :param album_info_path: Path to save pickle files to
    :type album_info_path: str
    :returns: df_audio_features: Data-frame of audio features for album
    :rtype: data-frame
    """

    print(f"Creating and pickling audio features data-frame for {album_name}")

    # Get album tracks

    album_uri = album_name_dict[album_name]
    tracks = sp.album_tracks(album_uri)

    album_data = pd.json_normalize(tracks["items"])
    album_data = album_data[["duration_ms", "name", "track_number", "uri"]]

    # Get audio features for each track and build a data frame

    df_audio_features = pd.DataFrame()

    for name, uri in tqdm(
        list(zip(album_data["name"].tolist(), album_data["uri"].tolist()))
    ):
        track_audio_features = pd.json_normalize(sp.audio_features(uri))
        track_audio_features["name"] = name
        df_audio_features = pd.concat(
            [df_audio_features, track_audio_features], axis=0
        )

    df_audio_features.set_index("name", inplace=True)
    df_audio_features.reset_index(inplace=True)

    df_audio_features.to_pickle(
        f"{album_info_path}/{album_name}_audio_features.pkl"
    )

    return df_audio_features


def get_album_audio_analysis(sp, album_name, album_name_dict, album_info_path):
    """Get audio analysis data for all albums for the given artists and pickle the data-frames

    :param sp: Spotify object
    :type sp: object
    :param album_name: List of album names
    :type album_name: list
    :param album_name_dict: Dictionary mapping album names to album uri values
    :type album_name_dict: dict
    :param album_info_path: Path to save pickle files to
    :type album_info_path: str
    :returns: df_audio_analysis: Data-frame for audio analysis of album
    :rtype: data-frame

    """

    # Get album tracks

    album_uri = album_name_dict[album_name]
    tracks = sp.album_tracks(album_uri)

    album_data = pd.json_normalize(tracks["items"])
    album_data = album_data[["duration_ms", "name", "track_number", "uri"]]

    # Get audio analysis for each track and build a data frame

    print(f"Creating and pickling audio analysis data-frame for {album_name}")

    df_audio_analysis = pd.DataFrame()

    for name, uri in tqdm(
        list(zip(album_data["name"].tolist(), album_data["uri"].tolist()))
    ):
        track_audio_analysis = pd.json_normalize(sp.audio_analysis(uri))
        track_audio_analysis["name"] = name
        df_audio_analysis = pd.concat(
            [df_audio_analysis, track_audio_analysis], axis=0
        )

    df_audio_analysis.set_index("name", inplace=True)
    df_audio_analysis.reset_index(inplace=True)

    df_audio_analysis.to_pickle(
        f"{album_info_path}/{album_name}_audio_analysis.pkl"
    )

    return df_audio_analysis
