import logging
import os

# Path to log file
log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app.log')

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set to DEBUG to capture all levels of logs
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file_path, mode='w'),  # Logs to the log file. Will overwrite existing log statements.
        logging.StreamHandler()          # Logs to console (stderr)
    ]
)

# Optionally, you can create a specific logger for your app
logger = logging.getLogger("my_app_logger")
