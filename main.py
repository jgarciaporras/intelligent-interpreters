from flask import Flask
from flask import request
from flask import render_template
import os
import sys
sys.path.append('modules')
from filename_generator import *


app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        f = request.files['audio_data']
        filename = "audio_clips/" + generate_random_filename()
        with open(filename, 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')

        return render_template('index.html', request="POST")
    else:
        return render_template("index.html")

@app.route('/test_output', methods=['POST', 'GET'])
def test_output():
    return render_template('index.html', language = "English", gender = "Male")


if __name__ == "__main__":
    app.run(debug=True)