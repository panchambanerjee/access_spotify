# access_spotify

This project is for all the music obsessives out there. 

It will eventually evolve into a package that offers advanced functionality for utilizing the Spotify API. 

Currently, the CLI interface queries Spotify for the specified artist (default = 'The Beatles' because who else?) and 
downloads all the album art, and all the album audio features and analysis for the artist. 

You can also import individual album data directly into a data-frame via a script or notebook. 

The album audio features and analysis are pickled as separate data-frames, which can then be read into 
pandas and analyzed, visualized etc. 

It is recommended that the user work in their own virtual environment.

Get your own Client_ID and Client_Secret from https://developer.spotify.com/dashboard/applications

For detailed information on the API and what audio features and audio analysis you can get via this script, please
refer to https://developer.spotify.com/documentation/web-api/reference/tracks/

## Installation and Usage

### Install the access-spotify package
* pip install access-spotify

### See the help menu
* access_script.py --help

### Query the Spotify API via CLI
* access_script.py --artist_name 'Led Zeppelin' --client_id 'your-client-id' --client_secret 'your-client-secret'

This saves all the album art (high resolution) and album track information (audio features and audio analysis) 
into pickled data-frames in the data/ folder. 

### Getting data for individual albums from the Spotify API
* See the example notebook on Github

### Also
* This is still very new, and I will continue to update the Documentation, functionality and add unit tests. 
Please let me know if you find any bugs or if you have any specific ideas for extending the functionality. 

### To-Do
* Documentation
* Unit tests
* Improve the argparse functionality
* Cool visualizations perhaps?
* Predictive Modeling? How sad will the next Radiohead album be? 

### This project would not have been possible without Spotipy --> https://spotipy.readthedocs.io/en/2.13.0/
-- Go buy them a coffee and give their github repo a star! 