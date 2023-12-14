import os
import sys
import logging


log_filename = "runninglogs.log"
log_file_path = os.path.join(os.getcwd(), "logs", log_filename)

# create directory for the logfile 
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

with open(log_file_path, 'w') as file:
    pass

log_format = '[%(asctime)s] : %(levelname)s : %(module)s : %(message)s]' # format

logging.basicConfig(
    level = logging.INFO,
    format= log_format, 
    handlers=[
        logging.FileHandler(log_file_path), 
        logging.StreamHandler(sys.stdout)
    ]
)