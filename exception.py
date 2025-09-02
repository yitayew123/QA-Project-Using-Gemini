# Import the sys module to access system-specific parameters and functions,
# particularly to get exception details.
import sys  

# Define a custom exception class inheriting from Python's base Exception class.
class customexception(Exception):
    
    # Constructor method to initialize the custom exception
    # error_message: the actual exception message
    # error_details: the sys module to extract traceback info
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message  # Store the original error message
        
        # Extract exception type, value, and traceback from sys
        _, _, exc_tb = error_details.exc_info()  
        
        # Print the traceback object (for debugging, optional)
        print(exc_tb)  
        
        # Get the line number where the exception occurred
        self.lineno = exc_tb.tb_lineno  
        
        # Get the file name where the exception occurred
        self.file_name = exc_tb.tb_frame.f_code.co_filename  

    # Define how the exception is converted to a string (when printed)
    def __str__(self):
        return "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message)
        )

# Code to test the custom exception
if __name__ == "__main__":
    try:
        # This will raise a ZeroDivisionError intentionally
        a = 1 / 0  

    except Exception as e:
        # Raise the custom exception with the original exception and sys module
        raise customexception(e, sys)  
