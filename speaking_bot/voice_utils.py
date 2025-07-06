import speech_recognition as sr
import pyttsx3
import streamlit as st
import tempfile
import os

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()

def speech_to_text():
    """
    Convert speech to text using speech recognition
    """
    recognizer = sr.Recognizer()
    
    try:
        # Use microphone as audio source
        with sr.Microphone() as source:
            st.info("🎤 Listening... Please speak now!")
            
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source, duration=1)
            
            # Listen for audio with timeout
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
            
            st.info("🔄 Processing your speech...")
            
            # Convert speech to text using Google's speech recognition
            text = recognizer.recognize_google(audio)
            
            st.success("✅ Speech recognized successfully!")
            return text
            
    except sr.UnknownValueError:
        st.error("❌ Could not understand the audio. Please try again.")
        return None
    except sr.RequestError as e:
        st.error(f"❌ Error with speech recognition service: {e}")
        return None
    except sr.WaitTimeoutError:
        st.error("❌ No speech detected. Please try again.")
        return None
    except Exception as e:
        st.error(f"❌ An error occurred: {e}")
        return None

def text_to_speech(text):
    """
    Convert text to speech using pyttsx3
    """
    try:
        # Set speech rate (optional)
        tts_engine.setProperty('rate', 150)
        
        # Set voice (optional - you can choose male/female voice)
        voices = tts_engine.getProperty('voices')
        if voices:
            tts_engine.setProperty('voice', voices[0].id)  # Use first available voice
        
        # Convert text to speech
        tts_engine.say(text)
        tts_engine.runAndWait()
        
    except Exception as e:
        st.error(f"❌ Error in text-to-speech: {e}")

def speech_to_text_from_file(audio_file):
    """
    Convert uploaded audio file to text
    """
    recognizer = sr.Recognizer()
    
    try:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            tmp_file.write(audio_file.read())
            tmp_file_path = tmp_file.name
        
        # Process the audio file
        with sr.AudioFile(tmp_file_path) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
        
        # Clean up temporary file
        os.unlink(tmp_file_path)
        
        return text
        
    except sr.UnknownValueError:
        st.error("❌ Could not understand the audio file.")
        return None
    except sr.RequestError as e:
        st.error(f"❌ Error with speech recognition service: {e}")
        return None
    except Exception as e:
        st.error(f"❌ An error occurred: {e}")
        return None