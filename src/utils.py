#common file
import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
from src.logger import logging
import dill


#create a function

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)  #this will take a file path
 
        os.makedirs(dir_path,exist_ok=True) #it will make a directory like this

        with open(file_path, "wb") as file_obj:  #open the file path
            dill.dump(obj, file_obj)  #dill is a library used to create a pickle file, which will be saved in specifi file path.
    except  Exception as e:
        raise CustomException(e,sys)
    
#by using this we are saving this pickle file in the hard disk
#in order to use this, we just import it