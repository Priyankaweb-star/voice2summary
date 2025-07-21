from src.voice_to_text import transcribe_audio
from src.text_to_pdf import text_to_pdf
from src.summarizer import summarize_transcript
import os

audio_file = "audio_input/meeting1.mp3"
transcript_file = "transcripts/meeting1.txt"
pdf_file = "pdfs/meeting1.pdf"
summary_file = "summaries/meeting1_summary.txt"

# Step 1: Audio to Transcript
if os.path.exists(audio_file):
    transcribe_audio(audio_file, transcript_file)

    # Step 2: Transcript to PDF
    if os.path.exists(transcript_file):
        text_to_pdf(transcript_file, pdf_file)

        # Step 3: Summary
        summarize_transcript(transcript_file, summary_file)
else:
    print("❌ Audio file not found!")
