from flask import Flask, request, jsonify, render_template, send_file
from generator import main
from moviepy.editor import *

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 64 * 1024 * 1024
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'flv', 'wmv'}


def allowed_file(filename):
  return '.' in filename and \
         filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/upload', methods=['POST', 'GET'])
def upload_video():

  if 'file' not in request.files:
    return jsonify({'error': 'No file part'}), 400

  file = request.files['file']

  if file.filename == '':
    return jsonify({'error': 'No selected file'}), 400

  if not allowed_file(file.filename):
    return jsonify({'error': 'Invalid file type'}), 400

  input_video = "./static/video.mp4"
  output_audio = "./static/audio.wav"

  file.save(input_video)

  descriptions, music_prompt = main()

  video = VideoFileClip(input_video)
  audio = AudioFileClip(output_audio)
  final_clip = video.set_audio(audio)
  final_clip.write_videofile("./static/combined_video.mp4", codec="libx264")

  video.close()
  audio.close()

  return render_template('output.html',
                         descriptions=descriptions,
                         music_prompt=music_prompt)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
