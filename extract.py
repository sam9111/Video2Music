from moviepy.editor import *
from PIL import Image
import numpy as np


def extract_images(video_path):

  video_clip = VideoFileClip(video_path)
  output_images = []

  for t in np.arange(0, video_clip.duration, 2):
    frame = video_clip.get_frame(t)
    image = Image.fromarray(frame)
    output_images.append(image)

  video_clip.close()

  print(f"Images extracted: {len(output_images)}")

  return output_images
