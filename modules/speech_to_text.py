# This module contains functions for converting the input wav file to mp3, as well as includes functions for integration with Google's Speech to Text API for
# transcribing audio to text

import pydub
import os
from google.cloud import speech


# Convertes a .wav file to .mp3
# This is done because it reduces the file size and also performance with Google Cloud Speech to Text API is much faster
def convert_wav_to_mp3(audio_clip_filename, wav_file_path, destination_path):
    wav_file = wav_file_path + audio_clip_filename + ".wav"
    sound = pydub.AudioSegment.from_wav(wav_file)
    #filename = audio_clip_filename.split(".")[0]
    mp3_filename = destination_path + audio_clip_filename + ".mp3"
    sound.export(mp3_filename, format="mp3")
    print("File Converted Successfully")
    return mp3_filename


# Passes an MP3 file to Google Cloud Speech to Text API and receives the transcription
def speech_to_text(mp3_audio_file_name, client_service_key_location, language):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = client_service_key_location
    speech_client = speech.SpeechClient()
    media_file_name = 'audio_clips/converted/' + mp3_audio_file_name + '.mp3'
    
    with open (media_file_name, 'rb') as f:
        byte_data_wav = f.read()
    
    audio_mp3 = speech.RecognitionAudio(content=byte_data_wav)
    
    config_mp3 = speech.RecognitionConfig(
        sample_rate_hertz=48000,
        enable_automatic_punctuation=True,
        language_code= language #'en-US'
    )

    # Transcribing the RecognitionAudio objects
    response_standard_mp3 = speech_client.recognize(
        config=config_mp3,
        audio=audio_mp3
    )

    transcription = str()
    for result in response_standard_mp3.results:
        transcription.append(result.alternatives[0].transcript)
        #confidence = result.alternatives[0].confidence

    return transcription #, confidence
