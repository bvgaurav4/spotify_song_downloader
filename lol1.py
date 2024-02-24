import os

# Specify the directory path
folder_path = 'C:\g\pproject\spotify_song_downloader\songs\mp4'  # Replace '/path/to/your/folder' with the actual directory path

# Iterate through all the filenames in the folder
for filename in os.listdir(folder_path):
    # Check if the current item is a file (not a subdirectory)
    if os.path.isfile(os.path.join(folder_path, filename)):
        # Split the filename into its base name and extension
        base_name, extension = os.path.splitext(filename)
        
        # Print only the base name
        print(base_name)