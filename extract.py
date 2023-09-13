from moviepy.editor import *


def extract_images(video_path, output_path, interval):
  video_clip = VideoFileClip(video_path)

  # Iterate through the frames and save them as images
  frame_number = 0
  for frame in video_clip.iter_frames(fps=1):
    frame_number += 1
    output_image_path = f'./frames/image_{frame_number:04d}.jpg'
    video_clip.save_frame(output_image_path, t=frame_number)

  # Close the video clip
  video_clip.close()

  print(f"Images extracted: {frame_number}")
