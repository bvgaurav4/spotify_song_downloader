from pytube import YouTube
from youtubesearchpython import VideosSearch

# Define your search query
# query = "I Was Made For Lovin' You"
def downloading(query):
    # Perform the search
    videos_search = VideosSearch(query, limit = 5)  # Limiting to 5 search results

    # Extract video URLs from search results
    video_urls = [video['link'] for video in videos_search.result()['result']]

    # Print the search results
    for i, url in enumerate(video_urls, start=1):
        print(f"{i}. {url}")

    # Let's download the first video from the search results
    if video_urls:
        # Get the first video URL from the search results
        video_url = video_urls[0]
        
        # Initialize YouTube object with the video URL
        yt = YouTube(video_url)
        
        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()
        
        # Download the video to the current working directory
        stream.download()
        
        print("Download complete.")
    else:
        print("No videos found for the given query.")
downloading("dandlions")
