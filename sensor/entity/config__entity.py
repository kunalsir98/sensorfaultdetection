import sys
import os 

from sensor.constant import training_pipeline
import pandas as pd 
import numpy as np
from datetime import datetime

print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR)



class TrainingPipelineConfig:

    def __init__(self,timestamp=datetime.now()):
        timestamp=timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name=training_pipeline.PIPELINE_NAME
        self.artifact_name=training_pipeline.ARTIFACT_DIR
        self.artifact_dir:str=os.path.join(self.artifact_name,timestamp)
        self.timestamp:str=timestamp

class DataIngestionConfig:
    def __init__(self,traing_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir:str=os.path.join(
            traing_pipeline_config.artifact_dir,training_pipeline.DATA_INGSETION_DATABASE_NAME

        )
        self.feature_store_file_path:str=os.path.join(
            self.data_ingestion_dir,training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,training_pipeline.FILE_NAME
        )
        self.train_file_path:str=os.path.join(
            self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TRAIN_FILE_NAME
        )
        self.test_file_path:str=os.path.join(
            self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TEST_FILE_NAME
        )
        self.train_test_split_ratio:float=training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        self.collection_name:str=training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.databse_name:str=training_pipeline.DATA_INGSETION_DATABASE_NAME


    