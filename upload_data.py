#!pip install pymongo


from pymongo.mongo_client import MongoClient
import pandas as pd
import json


#url
uri ="mongodb+srv://ag8827932659_db_user:Ansh1234@sensorcluster.sgdrxde.mongodb.net/?appName=SensorCluster"

#create a new client and coonect to server
client = MongoClient(uri)

#create database name and collection name
DATABASE_NAME="ANSH"
COLLECTION_NAME ="waferfault"

df =pd.read_csv(r"C:\Users\HP\Downloads\SensorProject\notebooks\wafer_23012020_041211.csv")

df = df.drop("Unnamed: 0",axis =1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)