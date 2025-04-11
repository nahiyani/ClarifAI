from utils.youtube_downloader import download_audio, download_video
from models.whisper_model import transcribe_audio
from models.blip_model import generate_video_summary
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

    print("\n🎥 Downloading video for BLIP analysis...")
    video_file = download_video(url)

    print("🧠 Running BLIP image captioning on video frames...")
    visual_summary = generate_video_summary(video_file)

    print("\n===== 🏷️ BLIP VISUAL SUMMARY =====\n")
    if visual_summary:
        print(visual_summary)
    else:
        print("❌ No captions generated or BLIP failed.")

if __name__ == "__main__":
    video_url = input("📺 Paste the YouTube video URL: ")
    process_youtube_video(video_url)