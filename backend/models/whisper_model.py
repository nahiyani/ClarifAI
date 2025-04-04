# models/whisper_model.py
import whisper
import os

model = whisper.load_model("medium")  # Load once

def transcribe_audio(audio_path):
    """Transcribe the given audio file using Whisper."""
    if not os.path.exists(audio_path):
        print("Error: Audio file not found.")
        return None

    result = model.transcribe(audio_path)
    return result['text']