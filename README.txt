QA with Documents - README

Project Overview:
-----------------
This project allows users to perform Question Answering (QA) on uploaded documents using 
Google’s Gemini LLM and embeddings. It uses LlamaIndex to create a vector-based index 
for semantic search and Streamlit as the front-end interface.

Features:
---------
1. Upload PDF or text documents.
2. Ask natural language questions about the content.
3. Gemini embeddings generate vector representations for semantic search.
4. Streamlit interface for interactive question-answering.
5. Logs and custom exceptions for debugging and tracking.

Project Structure:
------------------
QAWithPDF/
    ├── __init__.py
    ├── data_ingestion.py       # Load documents from disk or uploaded files
    ├── embedding.py            # Generate embeddings and create query engine
    └── model_api.py            # Load Gemini LLM model

Experiments/
    └── experiment.ipynb        # Jupyter notebook for testing the system

StreamlitApp.py                 # Main Streamlit application

logger.py                        # Logging configuration
exception.py                     # Custom exception handling
setup.py                          # Python package setup file

.env                              # Environment file storing your Google API key

Requirements:
-------------
- Python 3.11+
- Streamlit
- llama-index
- google-generativeai
- python-dotenv
- tiktoken (latest version)
- Other dependencies in setup.py

Installation:
-------------
1. Clone this repository:
   git clone <repository_url>

2. Navigate to project folder:
   cd qasystem

3. Create a virtual environment (recommended):
   conda create -n venvQA python=3.11
   conda activate venvQA

4. Install required packages:
   pip install -r requirements.txt

5. Create a `.env` file in the project root:
   GOOGLE_API_KEY=your_actual_google_api_key_here

Running the Streamlit App:
--------------------------
1. Activate your virtual environment:
   conda activate venvQA

2. Run the app:
   streamlit run StreamlitApp.py

3. In the browser, upload a document and ask your question.

Notes:
------
- Ensure your Google API key is valid; otherwise, the Gemini model will not load.
- Keep `tiktoken` updated to avoid tokenizer errors with embeddings.
- Uploaded documents should be in PDF or text format.

Troubleshooting:
----------------
1. **API Key Error**:
   Ensure `.env` exists and GOOGLE_API_KEY is set correctly.
   
2. **Unknown encoding `cl100k_base`**:
   Upgrade `tiktoken` to the latest version:
   pip install --upgrade tiktoken

3. **Module not found**:
   Ensure all required packages are installed in the active environment.

Contact:
--------
For questions or issues, contact: yitayewsolomon3@gmail.com

