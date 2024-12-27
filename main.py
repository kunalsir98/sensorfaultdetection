from sensor.components.data_ingestion import DataIngestion,DataIngestionArtifact
from sensor.exception.exception import SensorException
from sensor.logging.logger import logging

from sensor.entity import config__entity,artifact_entity
from sensor.entity.config__entity import DataIngestionConfig
from sensor.entity.config__entity import TrainingPipelineConfig
import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
    except Exception as e:
        raise SensorException(e,sys)