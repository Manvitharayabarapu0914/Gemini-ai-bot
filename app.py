import streamlit as st
from dotenv import load_dotenv
import os
from google import genai
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
st.set_page_config(
    page_title="gemini AI chatbot",
    layout="centered"
)
st.title("gemini AI chatbot")
st.write("Ask gemini anything !")
prompt= st.text_area("Enter your prompt here", placeholder="explain Ai in simple terms", height=100)
if st.button("generate response"):
    if prompt:
        with st.spinner("Gemini is thinking..."):
            response = client.models.generate_content(model="gemini-3.5-flash-lite",contents=prompt)
            st.success("Response generated successfully!")
            st.write(response.text)
    else:
        st.warning("please enter a prompt")