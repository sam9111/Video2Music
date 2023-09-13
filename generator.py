from extract import extract_images
from describe import describe_images
from musicprompt import generate_music_prompt
from musicgen import generate_music
import os


def main(video):
  # Specify the path to the video file
  video_path = "./video/" + video

  # Specify the output directory to save the extracted frames
  if not os.path.exists("frames"):
    os.mkdir("frames")
  else:
    os.system("rm -rf frames")
    os.mkdir("frames")

  output_directory = "frames"

  # Call the function to extract frames from the video
  extract_images(video_path, output_directory, 2)

  descriptions = describe_images()
  music_prompt = generate_music_prompt(descriptions)
  # music_prompt = "Reggae/Ska instrumentation, moderate-tempo BPM (around 100-120), with a relaxed, beachy vibe."
  generate_music(music_prompt)

  return music_prompt
