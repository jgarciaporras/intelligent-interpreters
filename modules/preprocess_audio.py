# This module contains functions that preprocesses the audio samples for input to the Neural Network, and saves the .npy file

import numpy as np
import librosa
from sklearn.preprocessing import StandardScaler

def preprocess_sample(file_name, destination_path):
    # load sample audio
    time_series_sample = []
    num_samples_sample = []
    audio_file = 'audio_clips/' + file_name + '.wav'
    data, samplerate = librosa.load(audio_file)
    time_series_sample.append(data)
    num_samples_sample.append(samplerate)

    # extract combined MFCC features 
    scaler = StandardScaler()
    
    mfcc_delta2_sample = []
    for i in range(0, len(time_series_sample)):
        mfcc_d = librosa.feature.mfcc(time_series_sample[i], sr=num_samples_sample[i])
        mfcc_delta = librosa.feature.delta(mfcc_d)
        mfcc_delta_delta = librosa.feature.delta(mfcc_d, order=2)
        combined_mfcc_delta = np.concatenate((mfcc_d, mfcc_delta, mfcc_delta_delta))
        combined_mfcc_delta_sc = scaler.fit_transform(combined_mfcc_delta)
        mfcc_delta2_sample.append(combined_mfcc_delta_sc)
    mfcc_delta2_sample = np.array(mfcc_delta2_sample)
    
    # saves features into npy file
    save_features = np.save(destination_path, mfcc_delta2_sample)
    
    # returns file with features of sample audio
    return save_features


