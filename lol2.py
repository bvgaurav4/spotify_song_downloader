from moviepy.editor import AudioFileClip

def convert_mp4_to_mp3(mp4_file_path, mp3_file_path):
    video = AudioFileClip(mp4_file_path)
    
    video.write_audiofile(mp3_file_path)

    print("Conversion complete.")

convert_mp4_to_mp3('C:\g\pproject\spotify_song_downloader\songs\Feel Good Inc.mp4', 'C:\g\pproject\spotify_song_downloader\songs\Feel Good Inc.mp3')
