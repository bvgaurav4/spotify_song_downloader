import requests
import base64


from pytube import YouTube
from youtubesearchpython import VideosSearch

# Replace these with your actual credentials
client_id = 'e48f621015e34b3a9aeefa6780e48b46'
client_secret = 'f634e1809a77452c8af8191543e35b17'

# Get an access token
auth_response = requests.post(
    'https://accounts.spotify.com/api/token',
    headers={
        'Authorization': 'Basic ' + base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode()
    },
    data={
        'grant_type': 'client_credentials'
    }
)
access_token = auth_response.json()['access_token']

# Extract the track ID from the Spotify link
lol=list()
with open('songs.txt', 'r') as file:
    spotify_link = file.read()
    print(spotify_link)
    lol = spotify_link.split('\n')
for i in lol:
    track_id = i.split('/')[-1]
    track_response = requests.get(
        f'https://api.spotify.com/v1/tracks/{track_id}',
        headers={
            'Authorization': 'Bearer ' + access_token
        }
    )
    track_name = track_response.json()['name']

    print(track_name)