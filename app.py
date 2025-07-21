# app.py

import streamlit as st
import os
from src.voice_to_text import transcribe_audio
from src.text_to_pdf import text_to_pdf
from src.summarizer import summarize_transcript

# --- Setup ---
st.set_page_config(page_title="Voice2Summary", page_icon="🎙️", layout="centered")

AUDIO_DIR = "audio_input"
TRANSCRIPT_DIR = "transcripts"
PDF_DIR = "pdfs"
SUMMARY_DIR = "summaries"

for folder in [AUDIO_DIR, TRANSCRIPT_DIR, PDF_DIR, SUMMARY_DIR]:
    os.makedirs(folder, exist_ok=True)

# --- Modern Gradient Header ---
st.markdown("""
    <div style="padding:25px; border-radius:15px; 
        background: linear-gradient(to right, #4facfe, #00f2fe); 
        color:white; text-align:center;">
        <h1 style="margin-bottom:5px;">🎙️ Voice2Summary Pro</h1>
        <p style="font-size:16px;">Convert Voice → PDF → Summary with AI</p>
    </div>
    <br>
""", unsafe_allow_html=True)

# --- Upload Section ---
st.markdown("### 📂 Upload your Audio File")
uploaded_file = st.file_uploader("", type=["mp3", "wav", "m4a"])

if uploaded_file:
    audio_filename = uploaded_file.name
    audio_path = os.path.join(AUDIO_DIR, audio_filename)
    with open(audio_path, "wb") as f:
        f.write(uploaded_file.read())

    base = os.path.splitext(audio_filename)[0]
    transcript_path = os.path.join(TRANSCRIPT_DIR, base + ".txt")
    pdf_path = os.path.join(PDF_DIR, base + ".pdf")
    summary_path = os.path.join(SUMMARY_DIR, base + "_summary.txt")

    with st.spinner("🧠 Transcribing audio..."):
        transcript = transcribe_audio(audio_path, transcript_path)

    with st.spinner("📄 Creating transcript PDF..."):
        text_to_pdf(transcript_path, pdf_path)

    with st.spinner("📝 Summarizing content..."):
        summary = summarize_transcript(transcript_path, summary_path)

    st.success("✅ All tasks completed successfully!")

    # --- Tab View ---
    tab1, tab2 = st.tabs(["📄 Transcript", "🧠 Summary"])

    with tab1:
        st.text_area("Full Transcript", transcript, height=300)
        st.download_button("⬇️ Download Transcript PDF", open(pdf_path, "rb").read(),
                           file_name=os.path.basename(pdf_path), mime="application/pdf")

    with tab2:
        st.markdown("""
            <div style="background-color:#f1f3f4; padding:20px; 
            border-radius:12px; font-size:16px; line-height:1.6;">
        """, unsafe_allow_html=True)
        st.markdown(summary)
        st.markdown("</div>", unsafe_allow_html=True)
        st.download_button("⬇️ Download Summary", open(summary_path, "rb").read(),
                           file_name=os.path.basename(summary_path), mime="text/plain")

    # --- Audio Preview (Optional) ---
    st.markdown("---")
    st.audio(audio_path)

else:
    st.info("🪄 Upload an audio file above to begin...")

# --- Footer ---
st.markdown("""
    <hr>
    <div style='text-align:center; font-size:14px;'>
        Made with ❤️ by <b>Priyanka</b> | <a href="https://github.com/Priyankaweb-star" target="_blank">GitHub ↗</a>
    </div>
""", unsafe_allow_html=True)
