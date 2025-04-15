import whisper
import os

model = whisper.load_model("medium")

def transcribe_audio(audio_path, return_segments=False):
    if not os.path.exists(audio_path):
        print("Error: Audio file not found.")
        return None

    result = model.transcribe(audio_path)

    if return_segments:
        return result['segments']
    else:
        return result['text']