# Import Streamlit to build interactive web apps
import streamlit as st  

# Import helper functions to load documents, embeddings, and LLM model
from QAWithPDF.data_ingestion import load_data  
from QAWithPDF.embedding import download_gemini_embedding  
from QAWithPDF.model_api import load_model  

from dotenv import load_dotenv
import os

load_dotenv()  # load environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # get the actual key

def main():
    """
    Main function to run the Streamlit app for QA with documents.
    """
    # Set the page configuration (title of the app)
    st.set_page_config(page_title="QA with Documents")  
    
    # File uploader widget for the user to upload a document
    doc = st.file_uploader("Upload your document")  
    
    # Header for the app section
    st.header("QA with Documents (Information Retrieval)")  
    
    # Text input widget for the user to enter a question
    user_question = st.text_input("Ask your question")  
    
    # Button to submit the question and process the document
    if st.button("Submit & Process"):
        # Show a spinner while processing
        with st.spinner("Processing..."):
            # Load the uploaded document using the data ingestion function
            document = load_data(doc)  
            
            # Load the Gemini LLM model
            model = load_model()  
            
            # Generate embeddings and create a query engine from the documents
            query_engine = download_gemini_embedding(model, document, google_api_key=GOOGLE_API_KEY)  
            
            # Query the engine with the user's question
            response = query_engine.query(user_question)  
            
            # Display the response from the model on the Streamlit app
            st.write(response.response)  


# Run the main function when this script is executed
if __name__ == "__main__":
    main()  