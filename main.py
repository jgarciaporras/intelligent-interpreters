from flask import Flask
from flask import request
from flask import render_template
import os
import sys
sys.path.append('modules')
from filename_generator import *
import speech_to_text

app = Flask(__name__, template_folder='templates')

# Load the NN model for prediction
model_directory = 'model/model1/'
model = audio_model(model_directory)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        f = request.files['audio_data']
        # Generate filename and store on server
        filename = generate_filename()
        file_path = "audio_clips/" + filename + '.wav'
        with open(file_path, 'wb') as audio:
            f.save(audio)
        print('file Uploaded successfully')

        # Convert .wav file to mp3
        wav_file_path = 'audio_clips/'
        mp3_destination_path = 'audio_clips/converted/'
        speech_to_text.convert_wav_to_mp3(filename, wav_file_path, mp3_destination_path)


        return render_template('index.html', request="POST")
    else:
        return render_template("index.html")

@app.route('/test_output', methods=['POST', 'GET'])
def test_output():
    return render_template('index.html', language = "English", gender = "Male")


if __name__ == "__main__":
    app.run(debug=True)