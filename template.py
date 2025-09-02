# Import the 'os' module to interact with the operating system
# (e.g., creating directories, checking file paths).
import os  

# Import 'Path' from 'pathlib' to handle filesystem paths more easily and cross-platform.
from pathlib import Path  

# Define a list of file paths that need to exist in the project.
list_of_files = [
    "QAWithPDF/__init__.py",
    "QAWithPDF/data_ingestion.py",
    "QAWithPDF/embedding.py",
    "QAWithPDF/model_api.py",
    "Experiments/experiment.ipynb",
    "StreamlitApp.py",
    "logger.py",
    "exception.py",
    "setup.py"
]

# Iterate over each file path in the list.
for filepath in list_of_files:
    # Convert the string path into a Path object for easier manipulation.
    filepath = Path(filepath)

    # Split the path into directory (filedir) and filename.
    filedir, filename = os.path.split(filepath)

    # If the directory part is not empty, create the directory (and any parent directories) if it doesn't exist.
    os.makedirs(filedir, exist_ok=True) if filedir != "" else None

    # Check if the file does not exist or if it exists but is empty (size 0).
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Open the file in write mode ('w') which will create the file if it doesn't exist.
        # 'pass' means no content is written; this just ensures the file exists.
        with open(filepath, 'w') as f:
            pass
