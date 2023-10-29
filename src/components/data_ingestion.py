#read the dataset from various data source, 
#read data, split the data

import os
import sys
# print(sys.path)
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass  #used to create classvariables

from src.components.data_transformation import DataTransformation, DataTransformationConfig

import sys
print(sys.path)


#there should be input required by this data_ingestion component
#where to save the data

# inside a class to define a variable we use init, but when we use this dataclass, we are able to define variabale
@dataclass  #here we use the decorator
class DataIngestionConfig:
    #any input required will be given by this class
    train_data_path :str =  os.path.join('artifact', 'train.csv')  #data ingestion output will be saved in this path. create an artifact folder for that
    #here above all the output will be stored in "artifact" folder and the filename will be "train.csv"
    test_data_path :str =  os.path.join('artifact', 'test.csv')
    raw_data_path :str =  os.path.join('artifact', 'data.csv')

    #above are the inputs which we are going to give to DataIngestion components, not component knows where to save the files

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        #when we call this class, these three paths defined above will get saved inside this class variable.
    def initiate_data_ingestion(self):
        #if data is stored in the database, for that we need to create mongoDB client in utils.py
        #for starters, start with basic
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv(r"notebook\data\stud.csv")  #here we can read data from csv as well
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)  #getting the directory name, wrt path
            #if the file is already there, we are not deleting it and keeping it.

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info('train test split initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            #done the splitting, now save it above.
            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)

if __name__ =="__main__":
    obj = DataIngestion()
    train_data, test_data =obj.initiate_data_ingestion()

    data_transformation = DataTransformation() 
    data_transformation.initiate_data_transformation(train_data,test_data)

