#common file
import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
from src.logger import logging
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


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


def evaluate_model(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for i in range(len(list(models))):


            model = list(models.values())[i]  #get each model

            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            # model.fit(X_train, y_train) #Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred) #prediction for train 

            test_model_score = r2_score (y_test, y_test_pred) #prediction for test

            report[list(models.keys())[i]] = test_model_score

        return report
    except Exception as e:
        raise CustomException(e, sys)
#evaluate 
