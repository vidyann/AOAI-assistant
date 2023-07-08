from moviepy.editor import *

# Set up the file paths
input_file = "./data/Microsoft Community Champs.mp4"
output_file = "./data/Microsoft Community Champs.wav"

# Load the video file
video = VideoFileClip(input_file)

# Extract the audio from the video file
audio = video.audio

# Save the audio to an MP3 file
audio.write_audiofile(output_file)



