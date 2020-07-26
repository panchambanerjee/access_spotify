# access_spotify

This project is for all the music obsessives out there. 

It will eventually evolve into a package that offers advanced functionality for utilizing the Spotify API. 

Currently, it queries Spotify for the specified artist (default = 'The Beatles' because who else?) and 
downloads all the album art, and all the album audio features and analysis for the artist. 

The album audio features and analysis are pickled as separate data-frames, which can then be read into 
pandas and analyzed, visualized etc. This will be made much more easy to utilize in future versions of the code. 


It is recommended that the user work in their own virtual environment. 

Current CLI usage:

git clone https://github.com/panchambanerjee/access_spotify.git

cd access_spotify/

pip install -r requirements.txt

