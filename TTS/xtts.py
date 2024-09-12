from TTS.api import TTS
import streamlit as st
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

st.title("Text-to-Speech basic test")
st.divider()
prompt = st.text_input("Type your text")

reference_audios = ['./samples/bolsonaro_sample_1.wav', './samples/bolsonaro_sample_2.wav', './samples/bolsonaro_sample_3.wav', './samples/bolsonaro_sample_4.wav']
if prompt:
    # generate speech by cloning a voice using default settings
    tts.tts_to_file(text=prompt,
                    file_path="output.wav",
                    speaker_wav=reference_audios,
                    language="pt",
                    split_sentences=True)
    st.audio("output.wav", format="audio/wav")