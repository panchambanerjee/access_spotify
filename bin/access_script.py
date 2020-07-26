#!/usr/bin/env python

"""
Access script
"""

from access_spotify import run_all

import argparse

parser = argparse.ArgumentParser(description='Get artist name for API access')
parser.add_argument(
    '--artist', '-a',
    default='The Beatles',
    help='Artist to download all album art and info for'
)
parser.add_argument(
    '--client_id', '-id',
    required=True,
    help='Client ID for API'
)
parser.add_argument(
    '--client_secret', '-s',
    required=True,
    help='Client Secret for API'
)

my_namespace = parser.parse_args()
artist_name = my_namespace.artist
CLIENT_ID = my_namespace.client_id
CLIENT_SECRET = my_namespace.client_secret


if __name__ == "__main__":
    run_all.run_all(artist_name=artist_name, client_id=CLIENT_ID, client_secret=CLIENT_SECRET)


