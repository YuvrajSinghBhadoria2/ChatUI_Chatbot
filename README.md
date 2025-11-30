# PDF Chatbot

## Overview
This project is a PDF chatbot application built with Streamlit and powered by Groq's LLM API. It allows users to upload PDF documents and ask questions about their content using Retrieval-Augmented Generation (RAG) techniques.

## Features
- Interactive chat interface for querying PDF content
- PDF document processing and text extraction
- Vector storage for efficient document retrieval
- Integration with Groq's Llama 3.1 8B model
- Context-aware responses based on PDF content

## Technologies Used
- **Streamlit**: For the web interface
- **Groq API**: For LLM inference
- **LangChain**: For building LLM applications
- **ChromaDB**: For vector storage and retrieval
- **HuggingFace Embeddings**: For document embeddings
- **PyPDF**: For PDF text extraction

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd pdf_chatbot
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   Create a `.env` file in the root directory and add your Groq API key:
   ```env
   GROQ_API_KEY=your_api_key_here
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run groq_rag_chatbot.py
   ```

2. Upload a PDF document using the interface
3. Ask questions about the content of the PDF
4. Receive context-aware responses based on the document

## How It Works

1. **Document Processing**: The application loads and processes PDF documents, extracting text content.
2. **Text Splitting**: Documents are split into smaller chunks for efficient processing.
3. **Embedding**: Text chunks are converted to embeddings using HuggingFace models.
4. **Vector Storage**: Embeddings are stored in ChromaDB for fast retrieval.
5. **Query Processing**: User questions are processed and matched against stored document embeddings.
6. **Response Generation**: Relevant document chunks are retrieved and used as context for the LLM to generate answers.

## Files

- `groq_rag_chatbot.py`: Main application with RAG implementation
- `chatUI.py`: Simple chat interface
- `invokellm.py`: Basic LLM integration
- `requirements.txt`: Project dependencies

## Configuration

The application uses the following environment variables:
- `GROQ_API_KEY`: Your Groq API key for LLM access

## License

This project is licensed under the MIT License.
