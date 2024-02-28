from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load Gemini pro model and get response
model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response

# Initializing Stream App
st.set_page_config(page_title="Q&A Demo")
st.text("Made by: Prashant Kumar")
st.text("IIT Patna")
st.header("Gemini LLM Application")
st.subheader("Chat Bot")

# Initialize session state for chat history if it doesn't exist
if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input Text:",key="input")
# submit=st.button("Ask the question")

if st.button("Ask the question") and input:
    response=get_gemini_response(input)
    # Add user query and response to session chat history
    st.session_state['chat_history'].append(("You",input))
    st.subheader("Response")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))

st.subheader("Chat history")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")