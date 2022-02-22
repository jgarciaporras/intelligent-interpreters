import pydub


def convert_wav_to_mp3(audio_clip_filename, destination_path):
    wav_file = audio_clip_filename + ".wav"
    sound = pydub.AudioSegment.from_wav(wav_file)
    filename = audio_clip_filename.split(".")[0]
    mp3_fillename = destination_path + filename + ".mp3"
    sound.export(mp3_fillename, format="mp3")
    print("File Converted Successfully")
    return
