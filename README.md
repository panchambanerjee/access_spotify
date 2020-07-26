# access_spotify

This project is for all the music obsessives out there. 

It will eventually evolve into a package that offers advanced functionality for utilizing the Spotify API. 

Currently, it queries Spotify for the specified artist (default = 'The Beatles' because who else?) and 
downloads all the album art, and all the album audio features and analysis for the artist. 

The album audio features and analysis are pickled as separate data-frames, which can then be read into 
pandas and analyzed, visualized etc. This will be made much more easy to utilize in future versions of the code. 

It is recommended that the user work in their own virtual environment.

Get your own Client_ID and Client_Secret from https://developer.spotify.com/dashboard/applications

## Current CLI usage:

### To clone the repository onto your local machine: 
* git clone https://github.com/panchambanerjee/access_spotify.git

### Install the dependencies:
* cd access_spotify/
* pip install -r requirements.txt

### Install the access-spotify package in developer mode:
* pip install -e ./

### See the help menu:
* access_script.py --help

### Query the Spotify API:
* access_script.py --artist_name 'Bob Dylan' --client_id 'your-client-id' --client_secret 'your-client-secret'

This saves all the album art (high resolution) and album track information (audio features and audio analysis) 
into pickled data-frames in the data/ folder. 

### This project would not have been possible without Spotipy: https://spotipy.readthedocs.io/en/2.13.0/
-- Go buy them a coffee and give their github repo a star! 
