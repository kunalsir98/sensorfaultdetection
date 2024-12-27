import os 
import sys
import json
import pymongo
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi 
ca=certifi.where()

import pandas as pd 
import numpy as np
from sensor.exception.exception import SensorException
from sensor.logging.logger import logging

class SensorDataExtractor:
    try:
        pass
    except Exception as e:
        raise SensorException(e,sys)
    
    def csv_to_json_converter(self,file_path):
        try:
            df=pd.read_csv(file_path)
            df.reset_index(drop=True,inplace=True)
            records=list(json.loads(df.T.to_json()).values())
            return records
        except Exception as e:
            raise SensorException(e,sys)
    
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.databse=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.databse=self.mongo_client[self.databse]
            self.collection=self.databse[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise SensorException(e,sys)
        
if __name__=='__main__':
    FILE_PATH='Sensor_Data\sensordata.csv'
    DATABASE='SENSORDB'
    collection='SensorData'
    sensorobj=SensorDataExtractor()
    records=sensorobj.csv_to_json_converter(file_path=FILE_PATH)
    print(records)
    no_of_records=sensorobj.insert_data_mongodb(records,DATABASE,collection)
    print(no_of_records)

