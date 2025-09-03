# Import Streamlit library to build interactive web applications
import streamlit as st  

# Import helper functions from your QAWithPDF module
from QAWithPDF.data_ingestion import load_data  # Loads uploaded PDF or text documents
from QAWithPDF.embedding import download_gemini_embedding  # Creates embeddings & query engine
from QAWithPDF.model_api import load_model  # Loads the Google Gemini LLM model

# Import dotenv to manage environment variables securely
from dotenv import load_dotenv
import os  # Provides access to environment variables and OS operations

# Load environment variables from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # Retrieve the actual Google API key

# Define the main function to run the Streamlit app
def main():
    """
    Main function to run the Streamlit app for interactive QA on documents.
    """

    # ---------------- Page Configuration ----------------
    # Set Streamlit page title, layout, and icon for browser tab and window
    st.set_page_config(
        page_title="📄 QA with Documents",
        layout="wide",  # Make the page full width
        page_icon="📝"  # Emoji icon for the page
    )

    # ---------------- Sidebar Configuration ----------------
    # Add a title in the sidebar
    st.sidebar.title("📌 QA with Documents")
    # Add instructions and information in the sidebar
    st.sidebar.info(
        """
        1. Upload your PDF or text document.
        2. Ask questions on the document dynamically.
        3. Each question will generate a response below.
        """
    )
    # Add a warning about API key validity
    st.sidebar.write("⚠️ Make sure your Google API key is valid in the `.env` file.")

    # ---------------- Main Page Header ----------------
    # Main title of the app
    st.title("📄 QA with Documents")
    # Short description below the title
    st.markdown(
        """
        Ask multiple questions on your uploaded documents without re-uploading. 
        Powered by **Google Gemini LLM** and **Gemini Embeddings**.
        """
    )

    # ---------------- Session State Initialization ----------------
    # Initialize session state variables to store document, model, questions, and responses
    if "document" not in st.session_state:
        st.session_state.document = None  # Store uploaded document once
    if "query_engine" not in st.session_state:
        st.session_state.query_engine = None  # Store the query engine once
    if "questions" not in st.session_state:
        st.session_state.questions = []  # List to store all dynamically added questions
    if "responses" not in st.session_state:
        st.session_state.responses = []  # List to store responses corresponding to each question

    # ---------------- File Upload ----------------
    # File uploader widget for PDF or text documents
    doc = st.file_uploader("📂 Upload your document", type=["pdf", "txt"])  

    # ---------------- Add New Question ----------------
    # Button to add a new empty question input dynamically
    if st.button("➕ Add New Question"):
        st.session_state.questions.append("")  # Append an empty string to the questions list

    # ---------------- Display Dynamic Question Inputs ----------------
    # Loop through all questions in session state and create input boxes
    for i in range(len(st.session_state.questions)):
        # Create a text input for the i-th question
        st.session_state.questions[i] = st.text_input(
            f"❓ Question {i+1}",  # Label for the input
            value=st.session_state.questions[i],  # Pre-fill with existing question if any
            key=f"question_{i}"  # Unique key for each input to prevent conflicts
        )

        # Create a submit button for this specific question
        if st.button(f"Submit Question {i+1}", key=f"submit_{i}"):
            # Check if a document has been uploaded
            if doc is None:
                st.warning("⚠️ Please upload a document first!")
            # Check if the question is empty
            elif st.session_state.questions[i].strip() == "":
                st.warning("⚠️ Please enter a question!")
            else:
                # Display a spinner while processing the question
                with st.spinner("Processing..."):
                    try:
                        # Load document only once to avoid reprocessing
                        if st.session_state.document is None:
                            st.session_state.document = load_data(doc)

                        # Load model and create query engine only once
                        if st.session_state.query_engine is None:
                            model = load_model()  # Load Google Gemini LLM
                            st.session_state.query_engine = download_gemini_embedding(
                                model, st.session_state.document, google_api_key=GOOGLE_API_KEY
                            )

                        # Query the engine with the current question
                        response = st.session_state.query_engine.query(st.session_state.questions[i])

                        # Store the response in session state
                        if len(st.session_state.responses) <= i:
                            st.session_state.responses.append(response.response)  # Append if new
                        else:
                            st.session_state.responses[i] = response.response  # Update if exists

                        # Display the response in an expandable section
                        with st.expander(f"💡 Response to Question {i+1}"):
                            st.success(st.session_state.responses[i])  # Display model's answer

                    # Handle exceptions and display error
                    except Exception as e:
                        st.error(f"❌ An error occurred: {str(e)}")

    # ---------------- Footer ----------------
    st.markdown("---")  # Add a horizontal line separator
    st.markdown("Made with ❤️ by **Yitayew Solomon**")  # Footer credit

# ---------------- Run the App ----------------
if __name__ == "__main__":
    main()  # Execute the main function when the script runs
