import logging
import os
from datetime import datetime

# Generate a log file name based on the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a 'logs' directory if it doesn't exist
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)

# Construct the full path for the log file
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Configure the logging module
logging.basicConfig(
    level=logging.INFO,               # Set the logging level to INFO
    filename=LOG_FILEPATH,            # Specify the log file path
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
    # Define the log message format with timestamp, line number, logger name, log level, and message
)

if __name__=="__main__":
    logging.info("I am Checking my logger file...")