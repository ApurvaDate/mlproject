import sys
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer  
#this ColumnTransformer is used to create pipelines
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    #this config will give me any path that I will be requiring the inputs
    preprocessor_ob_file_path = os.path.join("artifact", "preprocessor.pkl")#preprocessing or object file path,ani pipeline or pickle file
    #we just want to give the input to the data transformation

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):  
        """
        this function is responsible for data transformation
        
        """
        #this function is to create all pickle files, which will be responsible in converting the categorical features into numerical features

        # gender,race/ethnicity,parental level of education,lunch,test preparation course,math score,reading score,writing score
        try:
            numerical_columns = ['writing score', 'reading score']
            categorical_columns = [
                'gender',
                'race/ethnicity',
                'parental level of education',
                'lunch',
                'test preparation course'
            ]

            #now to create a pipeline,
            numerical_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy="median")) ,#for handeling the missing values
                    ("scaler", StandardScaler(with_mean=False))

                ]
                #here we have created a pipeline which is doing two important things, handeling the missing values, and scaling the data
                #this pipeline runs on the training data, transform on the test data
            )

            categorical_pipeline = Pipeline(
                steps = [
                        ("imputer", SimpleImputer(strategy="most_frequent")),#missing values handeling for categorical features
                        ("one_hot_encoder", OneHotEncoder()),
                        ("scaler", StandardScaler(with_mean=False))
                        ]
                     )
           
            #now we need to combine numerical pipeline with categorical pipeline
            logging.info("Numerical columns standard scaling completed")

            logging.info("categorical columns encoding completed")

            preprocessor = ColumnTransformer(
                [
                    ("numerical_pipeline",numerical_pipeline, numerical_columns),
                    ("categorical_pipeline", categorical_pipeline, categorical_columns)
                ]
            )

            #here above we created a numerical pipeline which is doing two tasks,
            #then categorical pipeline doing three tasks,
            #then we created logging.info
            #column transformer is a combination of numerical pipeline and categorical pipeline.

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
    
    def initiate_data_transformation(self, train_path,test_path):
        try:
            pass

            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessor_obj = self.get_data_transformer_object()

            target_column_name = "math score"
            numerical_columns = ['writing score', 'reading score']

            input_feature_train_df = train_df.drop(columns = [target_column_name], axis=1)
            #we also need to save the pickle file of the preprocessor object
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns = [target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.data_transformation_config.preprocessor_ob_file_path, #file _path
                obj=preprocessor_obj #object

            )

            #where do we write the save object?
            #we write in utils
            #utils will have all the common things which we are trying to import

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_ob_file_path

            )
        except Exception as e:
            raise CustomException(e,sys)


