import streamlit as st
from streamlit_mic_recorder import speech_to_text

# --- Sidebar: The Control Center ---
with st.sidebar:
    st.header("Voice Controls")
    # This button sits in the sidebar, perfect for mobile thumbs
    voice_data = speech_to_text(
        language='en', 
        start_prompt="🎙️ Speak Setting", 
        stop_prompt="🛑 Stop"
    )

# --- Logic: Handle the voice input ---
# We initialize our simulation variables
if 'green_speed' not in st.session_state:
    st.session_state.green_speed = 10.0

if voice_data:
    st.sidebar.write(f"Recognized: {voice_data}")
    # Simple parser: look for numbers in the speech
    words = voice_data.lower().split()
    for word in words:
        # If the user says "set speed to 12", this catches "12"
        if word.replace('.','',1).isdigit():
            st.session_state.green_speed = float(word)
            st.sidebar.success(f"Updated to {st.session_state.green_speed}")

# --- Main App: The Simulation ---
st.title("PuttSim")
st.write(f"Current Green Speed: {st.session_state.green_speed}")

# 

# Your existing simulation code goes here
# calculations(st.session_state.green_speed)
