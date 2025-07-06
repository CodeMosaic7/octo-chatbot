import streamlit as st
from speaking_bot.setup import conversation_chain as conversation
from speaking_bot.voice_utils import speech_to_text, text_to_speech

st.set_page_config(page_title="Personal Chatbot", layout="centered")
st.title("🗣️ Personal Ollama")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


mode = st.radio("Choose Input Mode", ("Text", "Voice"))


if mode == "Text":
    user_input = st.text_input("Type your message:")
    if st.button("Send") and user_input:
        # Get response from conversation chain
        response = conversation.predict(input=user_input)
        st.session_state.chat_history.append((user_input, response))
        text_to_speech(response)

elif mode == "Voice":
    if st.button("🎙️ Speak"):
        user_input = speech_to_text()
        if user_input:  
            st.write(f"You said: {user_input}")
        
            response = conversation.predict(input=user_input)
            st.session_state.chat_history.append((user_input, response))
            text_to_speech(response)

# Display chat history
st.markdown("### Conversation")
for user_msg, bot_msg in st.session_state.chat_history:
    st.markdown(f"**You**: {user_msg}")
    st.markdown(f"**Bot**: {bot_msg}")