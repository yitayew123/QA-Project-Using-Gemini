<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>QA with Documents - README</title>
</head>
<body>

  <h1>📄 QA with Documents - README</h1>

  <h2>📌 Project Overview</h2>
  <p>
    This project allows users to perform <b>Question Answering (QA)</b> on uploaded documents using 
    Google’s <b>Gemini LLM</b> and embeddings. It uses <b>LlamaIndex</b> to create a vector-based index 
    for semantic search and <b>Streamlit</b> as the front-end interface.
  </p>

  <h2>✨ Features</h2>
  <ul>
    <li>Upload PDF or text documents.</li>
    <li>Ask natural language questions about the content.</li>
    <li>Gemini embeddings generate vector representations for semantic search.</li>
    <li>Streamlit interface for interactive question-answering.</li>
    <li>Logs and custom exceptions for debugging and tracking.</li>
  </ul>

  <h2>📂 Project Structure</h2>
  <pre>
QAWithPDF/
    ├── __init__.py
    ├── data_ingestion.py       # Load documents from disk or uploaded files
    ├── embedding.py            # Generate embeddings and create query engine
    └── model_api.py            # Load Gemini LLM model

Experiments/
    └── experiment.ipynb        # Jupyter notebook for testing the system

StreamlitApp.py                 # Main Streamlit application
logger.py                       # Logging configuration
exception.py                    # Custom exception handling
setup.py                        # Python package setup file
.env                            # Environment file storing your Google API key
  </pre>

  <h2>⚙️ Requirements</h2>
  <ul>
    <li>Python 3.11+</li>
    <li>Streamlit</li>
    <li>llama-index</li>
    <li>google-generativeai</li>
    <li>python-dotenv</li>
    <li>tiktoken (latest version)</li>
    <li>Other dependencies in setup.py</li>
  </ul>

  <h2>🚀 Installation</h2>
  <ol>
    <li>Clone this repository:
      <pre>git clone &lt;repository_url&gt;</pre>
    </li>
    <li>Navigate to project folder:
      <pre>cd qasystem</pre>
    </li>
    <li>Create a virtual environment (recommended):
      <pre>
conda create -n venvQA python=3.11
conda activate venvQA
      </pre>
    </li>
    <li>Install required packages:
      <pre>pip install -r requirements.txt</pre>
    </li>
    <li>Create a <code>.env</code> file in the project root:
      <pre>GOOGLE_API_KEY=your_actual_google_api_key_here</pre>
    </li>
  </ol>

  <h2>▶️ Running the Streamlit App</h2>
  <ol>
    <li>Activate your virtual environment:
      <pre>conda activate venvQA</pre>
    </li>
    <li>Run the app:
      <pre>streamlit run StreamlitApp.py</pre>
    </li>
    <li>In the browser, upload a document and ask your question.</li>
  </ol>

  <h2>📝 Notes</h2>
  <ul>
    <li>Ensure your Google API key is valid; otherwise, the Gemini model will not load.</li>
    <li>Keep <code>tiktoken</code> updated to avoid tokenizer errors with embeddings.</li>
    <li>Uploaded documents should be in PDF or text format.</li>
  </ul>

  <h2>🐛 Troubleshooting</h2>
  <ol>
    <li><b>API Key Error</b>: Ensure <code>.env</code> exists and <code>GOOGLE_API_KEY</code> is set correctly.</li>
    <li><b>Unknown encoding <code>cl100k_base</code></b>: Upgrade <code>tiktoken</code> to the latest version:
      <pre>pip install --upgrade tiktoken</pre>
    </li>
    <li><b>Module not found</b>: Ensure all required packages are installed in the active environment.</li>
  </ol>

  <h2>📧 Contact</h2>
  <p>
    For questions or issues, contact: <a href="mailto:yitayewsolomon3@gmail.com">yitayewsolomon3@gmail.com</a>
  </p>

</body>
</html>
