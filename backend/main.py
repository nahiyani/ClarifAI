from utils.youtube_downloader import download_audio, download_video
from models.whisper_model import transcribe_audio
from models.yolo_model import detect_objects_in_video
from summarizer import summarize_text 

def process_youtube_video(url):
    print("🎧 Downloading audio...")
    audio_file = download_audio(url)

    print("📝 Transcribing audio with Whisper...")
    transcript = transcribe_audio(audio_file)

    print("\n===== 🎤 WHISPER TRANSCRIPT =====\n")
    print(transcript if transcript else "❌ Failed to generate transcript.")

    if transcript:
        print("\n📄 Summarizing transcript with BART...")
        summary = summarize_text(transcript)
        print("\n===== ✂️ SUMMARY =====\n")
        print(summary)

    print("\n🎥 Downloading video for YOLO object detection...")
    video_file = download_video(url)

    print("🧠 Running object detection with YOLO...")
    detections = detect_objects_in_video(video_file)

    print("\n===== 🕵️ YOLO OBJECT DETECTIONS =====\n")
    if detections:
        for frame_num, objects in detections[:10]:
            print(f"Frame {frame_num}: {', '.join(objects) if objects else 'No objects detected'}")
    else:
        print("❌ No objects detected or detection failed.")

if __name__ == "__main__":
    video_url = input("📺 Paste the YouTube video URL: ")
    process_youtube_video(video_url)