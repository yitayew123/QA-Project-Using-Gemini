# Import os to work with environment variables and file paths
import os  

# Import load_dotenv to load environment variables from a .env file
from dotenv import load_dotenv  

# Import sys to pass exception info to the custom exception class
import sys  

# Import Gemini LLM class from llama_index for text generation
from llama_index.llms.gemini import Gemini  

# Import Markdown and display for nicely formatted outputs in Jupyter notebooks
from IPython.display import Markdown, display  

# Import Google Generative AI SDK to interact with Gemini models
import google.generativeai as genai  

# Import custom exception class for controlled error handling
from exception import customexception  

# Import logging to track process flow
from logger import logging  


# Load environment variables from a .env file
load_dotenv()  

# Retrieve the Google API key from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  

# Configure the Google Generative AI client with the API key
genai.configure(api_key=GOOGLE_API_KEY)  


def load_model():
    """
    Loads a Gemini-Pro model for natural language processing.

    Returns:
    - model (Gemini): An instance of the Gemini class initialized with the 'gemini-pro' model.
    """
    try:
        # Initialize the Gemini LLM with the 'gemini-pro' model and API key
        model = Gemini(models='gemini-pro', api_key=GOOGLE_API_KEY)
        
        # Return the initialized model
        return model

    except Exception as e:
        # Raise a custom exception with details if initialization fails
        raise customexception(e, sys)  
