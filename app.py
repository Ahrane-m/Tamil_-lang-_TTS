import streamlit as st
from gtts import gTTS

# Title of the app
st.title("Tamil Speech to Text Converter")

# Input text from the user
user_text = st.text_area("Enter text to convert to speech:", "")

# Slow speech option
slow = st.checkbox("Slow speech", False)

# Convert text to speech and play the audio
if st.button("Convert and Play"):
    if user_text:
        # Generate the audio using gTTS with Tamil language
        audio = gTTS(text=user_text, lang='ta', slow=slow)
        
        # Save the audio in MP3 format
        audio.save("speech.mp3")

        # Play the MP3 file
        st.audio("speech.mp3", format="audio/mp3")

        # Optionally, download the MP3 file
        with open("speech.mp3", "rb") as file:
            st.download_button("Download Audio", file, file_name="speech.mp3", mime="audio/mp3")
    else:
        st.warning("Please enter some text to convert.")

# Note for users
st.write("Note: The quality of speech may vary depending on the text. For best results, ensure the text is in Tamil.")
