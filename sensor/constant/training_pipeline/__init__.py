import pandas as pd 
import numpy as np 
from datetime import datetime
import os 
import sys 

TARGET_COLUMN='class'
PIPELINE_NAME:str = 'sensor'
ARTIFACT_DIR:str= 'Artifacts'
FILE_NAME:str='sensordata.csv'

TRAIN_FILE_NAME:str = 'train.csv'
TEST_FILE_NAME:str= 'test.csv'

"""
data ingestion constanst
"""

DATA_INGESTION_COLLECTION_NAME:str = 'SensorData'
DATA_INGSETION_DATABASE_NAME:str='SENSORDB'
DATA_INGESTION_DIR_NAME:str='data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR:str='feature_store'
DATA_INGESTION_INGESTED_DIR:str='ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float = 0.2
