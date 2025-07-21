import whisper
import os

def transcribe_audio(audio_path, output_txt_path):
    model = whisper.load_model("large") 

    print(f"Transcribing: {audio_path} ...")
    result = model.transcribe(audio_path)

    transcript = result["text"]

    # Save to output file
    with open(output_txt_path, "w", encoding="utf-8") as f:
        f.write(transcript)

    print(f"Transcript saved to: {output_txt_path}")
    return transcript
