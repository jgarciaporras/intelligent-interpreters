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
import transcribe
import translate


app = Flask(__name__, template_folder='templates')

# Load the NN model for prediction
model_directory = 'model/model1/'
model = load_model_and_predict.audio_model(model_directory)

filename = filename_generator.generate_filename()
features_file = 'audio_clips/processed/' + filename + '.npy'
    


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        f = request.files['audio_data']
        # Generate filename and store on server
        
        file_path = "audio_clips/" + filename + '.wav'
        with open(file_path, 'wb') as audio:
            f.save(audio)
        print('file Uploaded successfully')

        # Convert .wav file to mp3
        wav_file_path = 'audio_clips/'
        mp3_destination_path = 'audio_clips/converted/'
        mp3_filename = speech_to_text.convert_wav_to_mp3(filename, wav_file_path, mp3_destination_path)

        # Preprocess audio
        audio_features = preprocess_audio.preprocess_sample(filename, features_file)
        print("Processed Audio Successfully")
        
        return render_template('index.html', request="POST")
    else:
        return render_template("index.html")

    
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == "POST":
        if request.form.get('predictaction') == 'Predict':
            
            prediction = load_model_and_predict.predict_sample(os.path.join(app.root_path, features_file), model)
            
            #language of transcription
            language = transcribe.get_audio_language(prediction)
            
            #transcribe audio
            transcription = transcribe.transcribe("audio_clips/" + filename + '.wav', language)    
            
            
            #translation language
            source = translate.get_source_language(language)
            
            target = 'en'
            
            #translate audio
            google_translate = translate.translate(transcription, source, target)
            translation = google_translate.text
            
    return render_template('index.html', prediction=prediction, transcription=transcription, translation=translation)


if __name__ == "__main__":
    app.run(debug=True)