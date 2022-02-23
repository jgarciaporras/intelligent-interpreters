import pydub
import os
from google.cloud import speech


def convert_wav_to_mp3(audio_clip_filename, destination_path):
    wav_file = audio_clip_filename + ".wav"
    sound = pydub.AudioSegment.from_wav(wav_file)
    filename = audio_clip_filename.split(".")[0]
    mp3_fillename = destination_path + filename + ".mp3"
    sound.export(mp3_fillename, format="mp3")
    print("File Converted Successfully")
    return


def speech_to_text(mp3_audio_file_name, client_service_key_location):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = client_service_key_location
    speech_client = speech.SpeechClient()
    media_file_name = 'audio_clips/converted/' + mp3_audio_file_name + '.mp3'
    
    with open (media_file_name, 'rb') as f:
        byte_data_wav = f.read()
    
    audio_mp3 = speech.RecognitionAudio(content=byte_data_wav)
    
    config_mp3 = speech.RecognitionConfig(
        sample_rate_hertz=48000,
        enable_automatic_punctuation=True,
        language_code='en-US'
    )

    # Transcribing the RecognitionAudio objects
    response_standard_mp3 = speech_client.recognize(
        config=config_mp3,
        audio=audio_mp3
    )

    transcription = str()
    for result in response_standard_mp3.results:
        transcription.append(result.alternatives[0].transcript)

    return transcription

