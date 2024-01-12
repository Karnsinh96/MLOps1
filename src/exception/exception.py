import sys

# Custom exception class that inherits from the built-in Exception class
class customexception(Exception):

    # Constructor to initialize the custom exception with an error message and details
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message
        
        # Get the traceback information
        _, _, exc_tb = error_details.exc_info()
        
        # Print the traceback information
        print(exc_tb)
        
        # Extract line number and file name from the traceback
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    # String representation of the custom exception
    def __str__(self):
        return "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message))


# Main block of code
if __name__ == "__main__":
    try:
        # Triggering a division by zero exception
        a = 1 / 0

    except Exception as e:
        # Catching the exception and raising the custom exception
        raise customexception(e, sys)