import warnings
import logging
import streamlit as st 

import os 
from dotenv import load_dotenv , find_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq





load_dotenv()

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


    groq_sys_prompt  = ChatPromptTemplate.from_template(
         template= """
                    You are a very good AI assistant , you always provide provide precise and concise answer as per user prompt .

                    """
    )
    model = "llama-3.1-8b-instant"
    groq_model = ChatGroq(model=model,api_key=os.environ.get("GROQ_API_KEY"))
    chat = groq_sys_prompt | groq_model | StrOutputParser()

    response = chat.invoke({"user_prompt":prompt})

    

    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({'role':'assistant','content':response})

 