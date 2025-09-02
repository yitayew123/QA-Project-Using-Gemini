# Import VectorStoreIndex to create a vector-based index for semantic search
from llama_index.core import VectorStoreIndex  

# Import ServiceContext to configure the LLM, embedding model, and chunking (deprecated in new versions)
from llama_index.core import ServiceContext  

# Import StorageContext and load_index_from_storage for saving and loading index data
from llama_index.core import StorageContext, load_index_from_storage  

# Import GeminiEmbedding to create vector embeddings using Google's Gemini model
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


def download_gemini_embedding(model, document):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Parameters:
    - model: The LLM model object (e.g., Gemini)
    - document: A list of document objects to be embedded

    Returns:
    - query_engine: A query engine built from the VectorStoreIndex for similarity queries
    """
    try:
        # Log the start of embedding creation (message can be customized)
        logging.info("Initializing Gemini Embedding model...")
        
        # Initialize the Gemini embedding model
        gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")
        
        # Configure ServiceContext (deprecated; used for setting LLM, embedding model, chunking)
        service_context = ServiceContext.from_defaults(
            llm=model,
            embed_model=gemini_embed_model,
            chunk_size=800,         # Maximum chunk size for splitting documents
            chunk_overlap=20        # Overlap between chunks for better context
        )
        
        # Log progress
        logging.info("Creating vector index from documents...")
        
        # Build a vector store index from the documents using the service context
        index = VectorStoreIndex.from_documents(document, service_context=service_context)
        
        # Persist the index to disk so it can be reloaded without rebuilding
        index.storage_context.persist()
        
        # Log progress
        logging.info("Converting index to a query engine...")
        
        # Create a query engine for interacting with the index (for semantic queries)
        query_engine = index.as_query_engine()
        
        # Return the query engine to allow querying the documents
        return query_engine

    except Exception as e:
        # Raise a custom exception with detailed info if anything goes wrong
        raise customexception(e, sys)
