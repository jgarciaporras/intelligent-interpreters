# This module contains functions that loads the Neural Network model and predicts audio samples for gender and language

import numpy as np
from tensorflow.keras.models import load_model


# loads model from the model directory
def audio_model(model_directory):
    model = load_model(model_directory, compile = True)
    
    return model


def predict_sample(file_name, model):
    # load features for sample audio
    sample_audio = np.load(file_name)

    # get model prediction
    predictions = model.predict(sample_audio)
    classes = np.argmax(predictions, axis = 1)

    # dictionary for prediction labels
    Dict = {0: 'Language: German, Gender: Female',
            1: 'Language: German, Gender: Male',
            2: 'Language: English, Gender: Female',
            3: 'Language: English, Gender: Male',
            4: 'Language: Spanish, Gender: Female',
            5: 'Language: Spanish, Gender: Male',
           }

    return (Dict[classes[0]])

