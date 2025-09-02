# Import the logging module to handle logging messages for debugging or monitoring.
import logging  

# Import the os module to handle file paths and directories.
import os  

# Import datetime to generate timestamps for log file names.
from datetime import datetime  

# Create a log file name using the current date and time, formatted as:
# MM_DD_YYYY_HH_MM_SS.log
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  

# Define the path where log files will be stored.
# This creates a 'logs' directory in the current working directory.
log_path = os.path.join(os.getcwd(), "logs")  

# Create the 'logs' directory if it doesn't exist.
os.makedirs(log_path, exist_ok=True)  

# Combine the log directory path and log file name to get the full log file path.
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)  

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,                # Set the logging level to INFO (captures info, warning, error, etc.)
    filename=LOG_FILEPATH,             # Specify the file where logs will be written
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
    # Format of each log message:
    # [timestamp] line_number logger_name - log_level - message
)
# Example log output:
# [2024-01-10 15:57:26,997] 6 root - INFO - this is my second testing
