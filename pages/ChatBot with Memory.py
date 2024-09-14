import streamlit as st

import os
from dotenv import load_dotenv
from llama_index.llms.gemini import Gemini
from llama_index.core.llms import ChatMessage

# Load the environment variables from the .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
llm = Gemini()


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "his_messages" not in st.session_state:
    st.session_state.his_messages = []

if "llm" not in st.session_state:
    st.session_state.llm = llm
 

st.title("Chatbot with Gemini")
st.chat_message("user").write("Hi there! How can I help you?")
user_prompt = st.chat_input("Say Something")


# Display chat messages from history on app rerun
for message in st.session_state.his_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#Tell me about Moon.

if user_prompt :


    st.chat_message("user").write(user_prompt)
    st.session_state.messages.append(ChatMessage(role= "user", content= user_prompt))
    st.session_state.his_messages.append({"role": "user", "content": user_prompt})
    # st.write(st.session_state.messages)

    assistant_message= st.chat_message("assistant")
    resp = st.session_state.llm.chat(st.session_state.messages)
    assistant_message.write(resp.message.content)

    st.session_state.messages.append(ChatMessage(role= "assistant", content= resp.message.content))
    st.session_state.his_messages.append({"role": "assistant", "content": resp.message.content})

    # resp = llm.stream_complete(user_prompt)
    # for r in resp:
        
    #     assistant_message.write(r.text)