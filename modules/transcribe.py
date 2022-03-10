# This module includes functions for integrating Google's Speech Recognition API

import speech_recognition as sr


def get_audio_language(audio_pred):
     
    Dict = {'Language: German, Gender: Female':'de-DE',
          'Language: German, Gender: Male':'de-DE',
          'Language: English, Gender: Female':'en-US',
          'Language: English, Gender: Male':'en-US',
          'Language: Spanish, Gender: Female':'es-ES',
          'Language: Spanish, Gender: Male':'es-ES',
         }
    
    return (Dict[audio_pred])



def transcribe(audio_path, language):

    # use the audio file as the audio source
    r = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = r.record(source)  # read the entire audio file
        
    transcript = r.recognize_google(audio, language=language)

    return transcript
    
