import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
import cv2

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").eval()

def summarize_captions(captions):
    joined = " ".join(captions)
    prompt = (
        "Summarize the following visual descriptions from a video:\n\n"
        + joined
        + "\n\nSummary:"
    )
   
    print(prompt)
    return prompt

def generate_video_summary(video_path, frame_skip=150):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    visual_captions = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_skip == 0:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            inputs = processor(images=frame_rgb, return_tensors="pt")
            with torch.no_grad():
                output = model.generate(**inputs)
            caption = processor.decode(output[0], skip_special_tokens=True)
            visual_captions.append(caption)
            print(f"[Frame {frame_count}] {caption}")

        frame_count += 1

    cap.release()
    return summarize_captions(visual_captions)