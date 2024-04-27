
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import PIL




load_dotenv()
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-pro-latest')

def get_gemini_conversation(prompt, uploaded_file):
    if uploaded_file is not None:
        response = model.generate_content([prompt, uploaded_file])
    else:
        response = model.generate_content(prompt)
    return response


def main():
    st.title("Chatbot with Gemini")
    user_prompt = st.text_area("You:", height=200)
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    img=None
    if uploaded_file is not None:
        img = PIL.Image.open(uploaded_file)
    if st.button('Submit'):
        if user_prompt:
            response = get_gemini_conversation(user_prompt, img)
            st.write(response.text)
        else:
            st.write("No prompt found!")

        
if __name__ == "__main__":
    main()
