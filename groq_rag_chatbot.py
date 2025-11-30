import warnings
import logging
import streamlit as st
import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_classic.chains.retrieval import create_retrieval_chain


load_dotenv()

warnings.filterwarnings("ignore")
logging.getLogger("transformers").setLevel(logging.ERROR)

st.title("ChatUI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])


# ---------- VECTORSTORE ----------
@st.cache_resource
def get_vectorstore():
    pdf_file = "15_Coverless_Steganography_for_Face_Recognition_Based_on_Diffusion_Model.pdf"
    loaders = PyPDFLoader(pdf_file)
    docs = loaders.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma.from_documents(chunks, embedding)

    return db


prompt_input = st.chat_input("Enter a message")

if prompt_input:
    st.chat_message("user").markdown(prompt_input)
    st.session_state.messages.append({"role": "user", "content": prompt_input})

    # ---------- PROMPT ----------
    prompt = ChatPromptTemplate.from_template("""
Use the following context to answer the question.

Context:
{context}

Question: {input}

Answer:
""")

    # ---------- LLM ----------
    groq_model = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=os.environ["GROQ_API_KEY"]
    )

    try:
        vectorstore = get_vectorstore()

        # ---------- STUFF DOCUMENT CHAIN ----------
        stuff_chain = create_stuff_documents_chain(
            groq_model,
            prompt
        )

        # ---------- RETRIEVER ----------
        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

        # ---------- MAIN RETRIEVAL CHAIN ----------
        chain = create_retrieval_chain(
            retriever=retriever,
            combine_docs_chain=stuff_chain,
        )

        # ---------- RUN QUERY ----------
        result = chain.invoke({
            "input": prompt_input
        })

        response = (
        result.get("output_text")
        or result.get("answer")
        or result.get("result")
        )

        st.chat_message("assistant").markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

    except Exception as e:
        st.error(f"Error: {e}")
