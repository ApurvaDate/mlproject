import os
import sys
from dataclasses import dataclass

# from catboost import CatBoostClassifier

from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor

)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
# from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

#for every component we need to create config file

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifact", "model.pkl")  #model training config

#we will create another class which will responsible for model trainer
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()  #inside this variable we will get the path

    def initiate_model_trainer(self,train_array,test_array,preprocessor_path):
        try:
            logging.info("Splitting training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
          ) #converted data into train and test
        models = {
            "Random Forest": RandomForestRegressor(),
            "Decision Tree": DecisionTreeRegressor(),
            "Gradient Boosting": GradientBoostingRegressor(),
            "Linear Regression" : LinearRegression(),
            "K-Neighbours Classifier" : KNeighborsRegressor()
        }

        model_report : dict= evaluate_model(X=X_train)

        except:
            pass


