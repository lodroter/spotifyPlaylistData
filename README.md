# Spotify playlist data

Python code for getting playlist data from any Spotify playlist. 

## Setup 

First you need to copy link to any spotify playlist like this 

https://open.spotify.com/playlist/5erJSy4v4m2LmTxsgwi8dy?si=149fa7ec74654ec5

For playlist id we need only this part of the link 

5erJSy4v4m2LmTxsgwi8dy

For credentials you need to create a Spotify app in spotify dashboard 

https://developer.spotify.com/dashboard

In settings of this app you can find ClientID and ClientSecret which you need to copy into the code. 

Once you've changed these 3 things you can run the code and the csv file will be created. 

## Possible data you can get

- **ID**: Unique Spotify identifier for the track.
- **Title**: The name of the track.
- **Artists**: List of artists involved in the track.
- **Album**: Information about the album the track belongs to.
- **Release date**: The release date of the album.
- **Duration**: Track length in milliseconds.
- **Explicit flag**: Whether the track is marked as explicit.
- **Popularity**: A measure of the track's popularity (0-100).
- **Preview URL**: URL to a short preview of the track.
- **External URL**: Direct URL to the track on Spotify.
