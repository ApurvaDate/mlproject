#we are going to write our own exception


############ exception handling ############
import sys 
from src.logger import logging


#the sys module in python provides various functions and variables that are used
#  to manipulate different parts of the python runtime environment

def error_message_details(error, error_detail: sys):  #error_details will be present in sys
    _, _, exe_tb = error_detail.exc_info() 
    file_name = exe_tb.tb_frame.f_code.co_filename  #to get the filename
     #execution info, this will give us three info we are interested in the last one.
    #on which line exception has occured, in which file exception  has occured
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(file_name, exe_tb.tb_lineno, str(error))

    return error_message
        
    
    #whenever error occurs we are going to call this function.

#created own exception class   
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        #inheriting from exception
        super().__init__(error_message) #inherit exception class 
        self.error_message = error_message_details(error_message, error_detail= error_detail)

#whenever we raise custom exception, it is inheriting from parent exception, whatever error msg is coming,
# it will initialize and gets assigned to a class variable

    def __str__(self):
        return self.error_message   #to print the error message is called.
    

import logging

if __name__ == "__main__":

    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by zero ")
        raise CustomException(e, sys)