import os
import sys
from logger.logs import logging
from exception.exception import customexception
import pandas as pd

from components.data_ingestion import DataIngestion
from components.data_transformation import DataTransformation
from components.model_trainer import ModelTrainer
from components.model_evalution import ModelEvaluation

#Data Ingestion  
obj=DataIngestion()
train_data_path,test_data_path=obj.initiate_data_ingestion()

#Data Transformation
data_transformation=DataTransformation()
train_arr,test_arr=data_transformation.initialize_data_transformation(train_data_path,test_data_path)

#Model Training
model_trainer_obj=ModelTrainer()
model_trainer_obj.initate_model_training(train_arr,test_arr)

#Model Evaluation
model_eval_obj = ModelEvaluation()
model_eval_obj.initiate_model_evaluation(train_arr,test_arr)