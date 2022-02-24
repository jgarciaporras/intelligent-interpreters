from flask import Flask
from flask import request
from flask import render_template
import os
import sys
sys.path.append('modules')
import filename_generator
import speech_to_text
import load_model_and_predict
import preprocess_audio

app = Flask(__name__, template_folder='templates')

# Load the NN model for prediction
model_directory = 'model/model1/'
model = load_model_and_predict.audio_model(model_directory)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        f = request.files['audio_data']
        # Generate filename and store on server
        filename = filename_generator.generate_filename()
        file_path = "audio_clips/" + filename + '.wav'
        with open(file_path, 'wb') as audio:
            f.save(audio)
        print('file Uploaded successfully')

        # Convert .wav file to mp3
        wav_file_path = 'audio_clips/'
        mp3_destination_path = 'audio_clips/converted/'
        mp3_filename = speech_to_text.convert_wav_to_mp3(filename, wav_file_path, mp3_destination_path)

        # Preprocess audio
        audio_features = preprocess_audio.preprocess_sample(filename)
        print("Processed Audio Successfully")

        features_file = 'audio_clips/processed/' + filename + '.npy'
        prediction = load_model_and_predict.predict_sample(features_file, model)
        print(prediction)
        return render_template('index.html', request="POST")
    else:
        return render_template("index.html")

@app.route('/test_output', methods=['POST', 'GET'])
def test_output():
    return render_template('index.html', language = "English", gender = "Male")


if __name__ == "__main__":
    app.run(debug=True)