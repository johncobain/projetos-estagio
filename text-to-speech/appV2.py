from gtts import gTTS
import streamlit as st

st.title("Text-to-Speech google")
st.divider()
prompt = st.text_input("Type your text")
lang = st.selectbox(
    "Language",
    ("en", "pt", "es"),
)

if prompt:
    tts = gTTS(prompt, lang=lang, slow=False)
    tts.save('output.wav')
    st.audio("output.wav", format="audio/wav")