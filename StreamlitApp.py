# Import Streamlit library to build interactive web applications
import streamlit as st  

# Import helper functions from QAWithPDF module
from QAWithPDF.data_ingestion import load_data  # Function to load uploaded PDF or text documents
from QAWithPDF.embedding import download_gemini_embedding  # Function to create embeddings & query engine
from QAWithPDF.model_api import load_model  # Function to load the Google Gemini LLM model

# Import dotenv to manage environment variables securely
from dotenv import load_dotenv
import os  # Provides access to environment variables and OS operations

# Load environment variables from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # Retrieve the Google API key from environment

# Define the main function to run the Streamlit app
def main():
    """
    Main function to run the Streamlit app for interactive QA on documents.
    """

    # ---------------- Page Configuration ----------------
    st.set_page_config(
        page_title="QA with Documents",  # Browser tab title
        layout="wide",  # Make the app full width
        page_icon="📝"  # Emoji icon for the app
    )

    # ---------------- Custom CSS for Styling ----------------
    st.markdown(
        """
        <style>
        /* Set app background to cream color and default text to black */
        .stApp {
            background-color: #fdf6e3; /* cream background */
            color: black; /* default text color black */
        }
        /* Customize file uploader appearance */
        div.stFileUploader {
            border: 2px dashed #4caf50; /* green dashed border */
            border-radius: 12px; /* rounded corners */
            padding: 12px; /* inner spacing */
            background-color: #f1f8e9; /* light cream/green background */
            color: black; /* text color inside uploader */
        }
        /* Customize button appearance */
        div.stButton > button {
            background-color: #4caf50; /* green button */
            color: black; /* button text color */
            border-radius: 10px; /* rounded corners */
            padding: 10px 20px; /* button padding */
            font-weight: bold; /* bold text */
            transition: 0.3s; /* smooth hover effect */
        }
        div.stButton > button:hover {
            background-color: black; /* dark background on hover */
            color: #ffffff; /* white text on hover */
        }
        /* Chat-style question boxes */
        .question-box {
            background-color: #fff9c4; /* soft yellow background */
            border-left: 5px solid #fbc02d; /* gold accent on the left */
            padding: 10px; /* spacing inside box */
            margin: 5px 0; /* spacing between boxes */
            border-radius: 8px; /* rounded corners */
            color: black; /* text color black */
        }
        /* Chat-style answer boxes */
        .answer-box {
            background-color: #bbdefb; /* soft blue background */
            border-left: 5px solid #1976d2; /* dark blue accent */
            padding: 10px; 
            margin: 5px 0 15px 0; /* spacing below answers */
            border-radius: 8px; 
            color: black; 
        }
        /* Adjust text size and color for input boxes */
        .stTextInput>div>input {
            font-size: 16px; 
            color: black; 
        }
        </style>
        """,
        unsafe_allow_html=True  # Allow HTML/CSS injection
    )

    # ---------------- Sidebar ----------------
    st.sidebar.title("📌 QA with Documents")  # Sidebar title
    st.sidebar.info(
        """
        1. Upload your PDF or text document.
        2. Ask questions dynamically.
        3. Each question will generate a response below in chat style.
        """
    )  # Instructions for users
    st.sidebar.write("⚠️ Ensure your Google API key is valid in `.env`.")  # Display API warning

    # ---------------- Main Page ----------------
    st.title("📄 QA with Documents")  # Main page title
    st.markdown(
        """
        <p style='font-size:18px; color:black;'>
        Ask multiple questions on your uploaded documents without re-uploading.<br>
        Powered by <b>Google Gemini LLM</b> and <b>Gemini Embeddings</b>.
        </p>
        """,
        unsafe_allow_html=True  # Allow HTML formatting
    )

    # ---------------- Session State Initialization ----------------
    # Initialize session variables to persist data between interactions
    if "document" not in st.session_state:
        st.session_state.document = None  # Store uploaded document
    if "query_engine" not in st.session_state:
        st.session_state.query_engine = None  # Store query engine for LLM
    if "questions" not in st.session_state:
        st.session_state.questions = []  # Store all questions dynamically
    if "responses" not in st.session_state:
        st.session_state.responses = []  # Store corresponding responses

    # ---------------- File Upload ----------------
    doc = st.file_uploader("📂 Upload your document", type=["pdf", "txt"])  # Upload PDF or text file

    # ---------------- Add New Question ----------------
    if st.button("➕ Add New Question"):  # Button to add a new question input
        st.session_state.questions.append("")  # Add empty string to questions list

    # ---------------- Dynamic Q&A ----------------
    for i in range(len(st.session_state.questions)):
        # Create text input for each question
        st.session_state.questions[i] = st.text_input(
            f"❓ Question {i+1}",  # Label for question
            value=st.session_state.questions[i],  # Pre-fill with existing value
            key=f"question_{i}"  # Unique key for each input
        )

        # Submit button for each question
        if st.button(f"Submit Question {i+1}", key=f"submit_{i}"):
            if doc is None:  # Check if document is uploaded
                st.warning("⚠️ Please upload a document first!")
            elif st.session_state.questions[i].strip() == "":  # Check if question is empty
                st.warning("⚠️ Please enter a question!")
            else:
                with st.spinner("Processing..."):  # Show spinner while processing
                    try:
                        # Load document only once
                        if st.session_state.document is None:
                            st.session_state.document = load_data(doc)

                        # Load model and create query engine only once
                        if st.session_state.query_engine is None:
                            model = load_model()
                            st.session_state.query_engine = download_gemini_embedding(
                                model, st.session_state.document, google_api_key=GOOGLE_API_KEY
                            )

                        # Query the engine with the current question
                        response = st.session_state.query_engine.query(st.session_state.questions[i])

                        # Store response in session state
                        if len(st.session_state.responses) <= i:
                            st.session_state.responses.append(response.response)
                        else:
                            st.session_state.responses[i] = response.response

                        # Display Q&A in styled boxes
                        st.markdown(f"<div class='question-box'>❓ {st.session_state.questions[i]}</div>", unsafe_allow_html=True)
                        st.markdown(f"<div class='answer-box'>💡 {st.session_state.responses[i]}</div>", unsafe_allow_html=True)

                    except Exception as e:  # Handle exceptions
                        st.error(f"❌ An error occurred: {str(e)}")

    # ---------------- Footer ----------------
    st.markdown("---")  # Horizontal line
    st.markdown("<p style='text-align:center; color:black;'>Made with ❤️ by <b>Yitayew Solomon</b></p>", unsafe_allow_html=True)

# ---------------- Run App ----------------
if __name__ == "__main__":
    main()  # Run the main function to launch the app
