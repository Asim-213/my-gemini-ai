import streamlit as st
import google.generativeai as genai


st.title("Welcome TO A13 AI")



genai.configure(api_key="AIzaSyAh2EeL3Tep1WHk0Ah-vaUoBGDJzVkk2lo")

text = st.text_input("Enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Enter"):
    response = chat.send_message(text)
    st.write(response.text)
