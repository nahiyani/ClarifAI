from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.youtube_downloader import download_audio, download_video
from models.whisper_model import transcribe_audio
from models.blip_model import generate_video_summary
from summarizer import summarize_text
import os

app = Flask(__name__)
CORS(app)

def format_timestamp(seconds):
    minutes, secs = divmod(int(seconds), 60)
    return f"{minutes}:{secs:02d}"

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'url' not in request.json:
        return jsonify({'error': 'No URL provided'}), 400

    video_url = request.json['url']
    try:
        print(f"➡️  [transcribe] Received request for URL: {video_url}")
        audio_file_path = download_audio(video_url)
        print("✅ Audio downloaded.")

        transcription = transcribe_audio(audio_file_path)
        print("✅ Transcription complete.")
        print("\n===== WHISPER TRANSCRIPTION START =====\n")
        print(transcription)
        print("\n===== WHISPER TRANSCRIPTION END =====\n")

        if os.path.exists(audio_file_path):
            os.remove(audio_file_path)
            print("🧹 Temp audio file removed.")

        return jsonify({'transcription': transcription.strip()}), 200

    except Exception as e:
        print(f"❌ Error in /transcribe: {str(e)}")
        return jsonify({'error': f'An error occurred during transcription: {str(e)}'}), 500

@app.route('/process_full', methods=['POST'])
def process_full():
    if 'url' not in request.json:
        return jsonify({'error': 'No URL provided'}), 400

    url = request.json['url']
    response_data = {}

    try:
        print(f"➡️  [process_full] Starting full processing for URL: {url}")

        print("🎧 Downloading audio...")
        audio_file = download_audio(url)
        print("✅ Audio downloaded.")

        print("📝 Transcribing audio with Whisper...")
        transcript_segments = transcribe_audio(audio_file, return_segments=True)
        print("✅ Transcription complete.")

        formatted_segments = []
        full_transcript = ""
        timestamped_transcript = ""

        print("\n===== 🎤 WHISPER TRANSCRIPT =====\n")
        for idx, seg in enumerate(transcript_segments):
            start = seg['start']
            end = seg['end']
            text = seg['text'].strip()

            start_str = format_timestamp(start)
            end_str = format_timestamp(end)

            segment_text = f"[{start_str} - {end_str}]: {text}"
            print(segment_text)

            formatted_segments.append({
                'start': start_str,
                'end': end_str,
                'text': text
            })
            
            if idx == 0:
                full_transcript = text
            else:
                full_transcript += f" {text}"
                
            timestamped_transcript += segment_text + "\n"

        response_data['transcript_segments'] = formatted_segments
        response_data['timestamped_transcript'] = timestamped_transcript.strip()

        print("\n📄 Summarizing transcript with BART...")
        summary = summarize_text(full_transcript.strip())
        print("\n===== ✂️ SUMMARY =====\n")
        print(summary)
        response_data['summary'] = summary.strip()

        print("\n🎥 Downloading video for BLIP analysis...")
        video_file = download_video(url)
        print("✅ Video downloaded.")

        print("🧠 Running BLIP image captioning on video frames...")
        visual_summary = generate_video_summary(video_file)
        print("\n===== 🏷️ BLIP VISUAL SUMMARY =====\n")
        if visual_summary:
            print(visual_summary)
        else:
            print("❌ No captions generated or BLIP failed.")
        response_data['visual_summary'] = visual_summary.strip() if visual_summary else ""

        print("✅ Full processing complete.")
        return jsonify(response_data), 200

    except Exception as e:
        print(f"❌ Error in /process_full: {str(e)}")
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    print("🚀 Starting Flask server on http://localhost:5000")
    app.run(debug=True)