# streamlit run app.py --server.maxUploadSize 400
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(url):
    video_id = url.split("=")[1]

    # Retrieve the transcript using YouTubeTranscriptApi
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)

    # Convert the list of dictionaries to a single string
    transcript_string = " ".join([item['text'] for item in transcript_list])
    return transcript_string


# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

st.title("Youtube Video Explainer")
# st.markdown("**Enter the the Video ID**", unsafe_allow_html=True)
st.header("Enter the the Youtube Video URL:")
url = st.text_input("")

prompt=""
# st.header("Enter the prompt if you want:")
# st.markdown("**Default prompt:** Make a note of whatever taught in this transcript elaborately and explain each of the concepts and terms discussed. Explain in a detailed manner. Expound and interpret the terms.", unsafe_allow_html=True)
# # video_id = st.text_area("Enter Below", height=200)
# prompt= st.text_area("Enter Below", height=200)

import os
load_dotenv()
# GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
GOOGLE_API_KEY=st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)
transcript_string=""
if url:
    transcript_string = get_transcript(url)

if transcript_string:
    try: 
        model = genai.GenerativeModel('gemini-1.5-pro-latest')
        if prompt:
            response = model.generate_content(f"{prompt} Transcript: {transcript_string}")
        else:
            response = model.generate_content(f"Make a note of whatever taught in this transcript elaborately and explain each of the concepts and terms discussed. Explain in a detailed manner. Expound and interpret the terms. Transcript: {transcript_string}")
        st.write(response.text)
        
    except Exception as e:
         st.write(f'{type(e).__name__}: {e}')


