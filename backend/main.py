from utils.youtube_downloader import download_audio, download_video
from models.whisper_model import transcribe_audio
from models.blip_model import generate_video_summary
from summarizer import summarize_text

def format_timestamp(seconds):
    minutes, secs = divmod(int(seconds), 60)
    return f"{minutes}:{secs:02d}"

def process_youtube_video(url):
    print("🎧 Downloading audio...")
    audio_file = download_audio(url)

    print("📝 Transcribing audio with Whisper...")
    transcript_segments = transcribe_audio(audio_file, return_segments=True)

    print("\n===== 🎤 WHISPER TRANSCRIPT =====\n")
    full_transcript = ""
    if transcript_segments:
        for segment in transcript_segments:
            start = segment['start']
            end = segment['end']
            text = segment['text'].strip()

            start_str = format_timestamp(start)
            end_str = format_timestamp(end)

            print(f"[{start_str} - {end_str}]: {text}")
            full_transcript += f"{text} "
    else:
        print("❌ Failed to generate transcript.")

    if full_transcript:
        print("\n📄 Summarizing transcript with BART...")
        summary = summarize_text(full_transcript)
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