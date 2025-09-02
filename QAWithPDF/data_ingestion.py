# Import SimpleDirectoryReader to read documents from a directory
from llama_index.core import SimpleDirectoryReader  

# Import sys to pass system exception details to the custom exception
import sys  

# Import the custom exception class from your exception module
from exception import customexception  

# Import logging for capturing process information
from logger import logging  


def load_data(data):
    """
    Load PDF documents from a specified directory.

    Parameters:
    - data (str): The path to the directory containing PDF files.

    Returns:
    - A list of loaded PDF documents. The specific type of documents may vary.
    """
    try:
        # Log the start of the data loading process
        logging.info("Data loading started...")
        
        # Initialize the document loader for the specified directory
        # Currently, the directory is hardcoded as "Data" instead of using 'data' parameter
        loader = SimpleDirectoryReader("Data")  
        
        # Load all documents from the directory into a list
        documents = loader.load_data()  
        
        # Log successful completion of data loading
        logging.info("Data loading completed...")
        
        # Return the loaded documents
        return documents  

    except Exception as e:
        # Log that an exception occurred during data loading
        logging.info("Exception occurred in loading data...")
        
        # Raise a custom exception with details about the original exception
        raise customexception(e, sys)
  