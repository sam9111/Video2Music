from flask import Flask, render_template, request, send_file, redirect
from generator import main
app = Flask(__name__)


@app.route('/audio')
def serve_audio():
    # Provide the path to your audio file here
    audio_file = './public/musicgen_out.wav'
    return send_file(audio_file, mimetype='audio/mpeg')


@app.route('/', methods=['GET', 'POST'])
def upload_video():
    if request.method == 'POST':
        # Check if the POST request has a file part
        if 'video_file' not in request.files:
            return 'No file part in the request'

        file = request.files['video_file']

        # Check if the file is selected
        if file.filename == '':
            return 'No file selected'

        # Save the uploaded video file
        file.save("./video/"+file.filename)

        # Call the main function to generate music

        music_prompt = main(file.filename)

        return render_template('output.html', music_prompt=music_prompt)

    return render_template('upload.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
