import requests
import csv
import json
import base64

# Spotify API credentials
client_id = ''
client_secret = ''

# Encode credentials
credentials = f"{client_id}:{client_secret}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()

# Get access token
token_url = "https://accounts.spotify.com/api/token"
token_data = {
    "grant_type": "client_credentials"
}
token_headers = {
    "Authorization": f"Basic {encoded_credentials}"
}

response = requests.post(token_url, data=token_data, headers=token_headers)
token_response_data = response.json()
access_token = token_response_data.get('access_token')

if not access_token:
    print("Failed to retrieve access token")
    print(token_response_data)
    exit()

# Get playlist items
playlist_id = '5erJSy4v4m2LmTxsgwi8dy'#playlist_id = '5M4CVbcaiIivlDemL2D4ly'
playlist_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
playlist_headers = {
    "Authorization": f"Bearer {access_token}"
}

params = {
    "limit": 100,
    "offset": 0
}

all_tracks = []

while True:
    response = requests.get(playlist_url, headers=playlist_headers, params=params)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve playlist data: {response.status_code}")
        print(response.text)
        break

    playlist_data = response.json()

    # Print the raw response data for debugging (optional)
    # print(json.dumps(playlist_data, indent=4))

    # Check for 'items' key or any relevant key in the response
    if 'items' not in playlist_data:
        print("Key 'items' not found in the response")
        print(playlist_data)
        break

    # Add current batch of tracks to the list
    all_tracks.extend(playlist_data['items'])

    # Check if there are more tracks to fetch
    if playlist_data['next'] is None:
        break

    # Move to the next page
    params['offset'] += params['limit']


# Extract necessary information
track_info = []
for item in all_tracks:
    if 'track' in item:
        track = item['track']
        if 'artists' in track and 'name' in track:
            track_info.append({
                "title": track.get("name"),  # Track title
                "artist": [artist['name'] for artist in track.get("artists", [])],  # List of artist names
                "album": track.get("album", {}).get("name"),  # Album name
                "release_date": track.get("album", {}).get("release_date"),
                "popularity": track.get("popularity"),  # Track popularity
                "preview_url": track.get("preview_url"),  # Link to track snippet
                "external_url": track.get("external_urls", {}).get("spotify")  # Spotify URL
            
            })
        else:
            print(f"Track data is missing expected keys: {track}")
    else:
        print(f"Item data is missing 'track' key: {item}")

# Save data to CSV
csv_file = 'spotify_playlist.csv'
csv_columns = ['title','artist','album','release_date','popularity','preview_url','external_url',]

with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in track_info:
        writer.writerow(data)

print(f"Data saved to {csv_file}")
