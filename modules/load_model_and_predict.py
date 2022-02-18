#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from tensorflow.keras.models import load_model


def audio_model(model_folder):
    # loads model from the model folder
    model = load_model(model_folder, compile = True)
    
    return model


def predict_sample(file_name):
    # load features for sample audio
    sample_audio = np.load(file_name+'.npy')

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

