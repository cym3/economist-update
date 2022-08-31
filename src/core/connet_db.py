from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os

def db ():
  DATABASE_URL = os.getenv('DATABASE_URL')
  client = MongoClient(DATABASE_URL, server_api=ServerApi('1'))
  db = client.economist

  return db