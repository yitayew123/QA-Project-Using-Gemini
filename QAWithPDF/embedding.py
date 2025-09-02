# Import VectorStoreIndex to create a vector-based index for semantic search
from llama_index.core import VectorStoreIndex  
from llama_index.core import Settings  # Global settings to replace ServiceContext
from llama_index.embeddings.gemini import GeminiEmbedding  

# Import helper functions to load documents and models
from QAWithPDF.data_ingestion import load_data  
from QAWithPDF.model_api import load_model  

# Import sys to pass system exception info to custom exception
import sys  

# Import custom exception class for controlled error handling
from exception import customexception  

# Import logging for tracking process flow
from logger import logging  


def download_gemini_embedding(model, document, google_api_key):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Parameters:
    - model: The Gemini LLM model object
    - document: A list of document objects to be embedded
    - google_api_key: API key for Gemini model

    Returns:
    - query_engine: A query engine built from the VectorStoreIndex for similarity queries
    """
    try:
        # Log the start of embedding creation
        logging.info("Initializing Gemini Embedding model...")
        
        # Initialize the Gemini embedding model
        gemini_embed_model = GeminiEmbedding(
            model_name="models/embedding-001",
            api_key=google_api_key
        )
        
        # Configure global Settings (replaces deprecated ServiceContext)
        Settings.llm = model                       # Set the LLM
        Settings.embed_model = gemini_embed_model  # Set the embedding model
        Settings.chunk_size = 800                  # Configure chunk size
        Settings.chunk_overlap = 20                # Configure chunk overlap
        
        # Log progress
        logging.info("Creating vector index from documents...")
        
        # Build a vector store index from the documents
        index = VectorStoreIndex.from_documents(document, service_context=None)  # No ServiceContext needed
        
        # Persist the index to disk so it can be reloaded later
        index.storage_context.persist()
        
        # Log progress
        logging.info("Converting index to a query engine...")
        
        # Create a query engine for interacting with the index
        query_engine = index.as_query_engine()
        
        # Return the query engine
        return query_engine

    except Exception as e:
        # Raise a custom exception with detailed info if anything goes wrong
        raise customexception(e, sys)
