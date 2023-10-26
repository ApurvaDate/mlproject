import logging
import os
from datetime import datetime


#create log file

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) 
#whatever logs will be created it will be respect to current working directory.
#logs folder will get created,
os.makedirs(logs_path, exist_ok=True) #even when there is file, keep on appending it.

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
#whenever we want to create the log, we have to set this up in basic config
#give the file name, where you want to store it
#format
#which level

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s- %(message)s", 
    level = logging.INFO, 


)# any print msg will use this config, wrt msg


# if __name__ == "__main__":
#     logging.info("Logging  has started")