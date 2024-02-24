import requests
import base64


from pytube import YouTube
from youtubesearchpython import VideosSearch

from moviepy.editor import AudioFileClip

def convert_mp4_to_mp3(mp4_file_path, mp3_file_path):
    try:
        video = AudioFileClip(mp4_file_path)
    except:
        print(mp3_file_path,mp4_file_path)
        return  
    video.write_audiofile(mp3_file_path)

    print("Conversion complete.")
path="C:\g\pproject\spotify_song_downloader\songs"
def downloading(query):
    videos_search = VideosSearch(query, limit = 5 )  

    video_urls = [video['link'] for video in videos_search.result()['result']]

    
    for i, url in enumerate(video_urls, start=1):
        print(f"{i}. {url}")

    
    if video_urls:
        video_url = video_urls[0]
        
        yt = YouTube(video_url)
        
        try:
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path="C:\g\pproject\spotify_song_downloader\songs\mp4")
        except:
            print("An error occurred while downloading the video.")
            return     
        
        print("Download complete.")
    else:
        print("No videos found for the given query.")

client_id = 'e48f621015e34b3a9aeefa6780e48b46'
client_secret = 'f634e1809a77452c8af8191543e35b17'

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

lol=list()
with open('songs.txt', 'r') as file:
    spotify_link = file.read()
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
    artist_name = track_response.json()['artists'][0]['name']

    print(track_name + " " + artist_name)
    downloading(track_name+" "+artist_name)

import os

# Specify the directory path
folder_path = 'C:\g\pproject\spotify_song_downloader\songs\mp4'  # Replace '/path/to/your/folder' with the actual directory path

# Iterate through all the filenames in the folder
for filename in os.listdir(folder_path):
    # Check if the current item is a file (not a subdirectory)
    if os.path.isfile(os.path.join(folder_path, filename)):
        base_name, extension = os.path.splitext(filename)
        print(filename)
        convert_mp4_to_mp3(f"C:\g\pproject\spotify_song_downloader\songs\mp4\{filename}", f"C:\g\pproject\spotify_song_downloader\songs\mp3\{base_name}.mp3")

print("All files have been downloaded and  converted.")
