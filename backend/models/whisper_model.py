import whisper
import os

model = whisper.load_model("medium")

def transcribe_audio(audio_path):
    if not os.path.exists(audio_path):
        print("Error: Audio file not found.")
        return None

    result = model.transcribe(audio_path)
    return result['text']