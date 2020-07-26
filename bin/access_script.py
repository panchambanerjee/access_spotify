#!/usr/bin/env python

"""
Access script
"""

from access_spotify import run_all
from spotify_credentials import CLIENT_ID, CLIENT_SECRET

import argparse

parser = argparse.ArgumentParser(description='Get artist name for API access')
parser.add_argument(
    '--artist', '-a',
    default='The Beatles',
    help='Artist to download all album art and info for'
)

my_namespace = parser.parse_args()
artist_name = my_namespace.artist


if __name__ == "__main__":
    run_all.run_all(artist_name=artist_name, client_id=CLIENT_ID, client_secret=CLIENT_SECRET)


