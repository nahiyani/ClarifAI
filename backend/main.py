# main.py
from utils.youtube_downloader import download_audio, download_video
from models.whisper_model import transcribe_audio
from models.yolo_model import detect_objects_in_video

def process_youtube_video(url):
    print("Downloading audio...")
    audio_file = download_audio(url)

    print("Transcribing...")
    transcript = transcribe_audio(audio_file)

    print("\nTranscript:\n", transcript[:1000], "...")  # Limit output

    print("\nDownloading video for object detection...")
    video_file = download_video(url)

    print("Running object detection...")
    detections = detect_objects_in_video(video_file)

    print("\nDetections (sample):")
    for frame, objects in detections[:5]:  # Show just first few
        print(f"Frame {frame}: {objects}")

if __name__ == "__main__":
    video_url = input("Paste the YouTube video URL: ")
    process_youtube_video(video_url)