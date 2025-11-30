import warnings
import logging


import streamlit as st 

warnings.filterwarnings("ignore")
logging.getLogger("transformers").setLevel(logging.ERROR)


st.title("ChatUI")

prompt = st.chat_input('enter a message')

if 'messages' not in st.session_state:
     st.session_state.messages=[]


for message in st.session_state.messages:
     st.chat_message(message['role']).markdown(message['content'])

if prompt :
    st.chat_message('user').markdown(prompt)
    st.session_state.messages.append({'role':'user','content':prompt})


    response = "Hi I'm chatgpt"
    

    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({'role':'assistant','content':response})

 