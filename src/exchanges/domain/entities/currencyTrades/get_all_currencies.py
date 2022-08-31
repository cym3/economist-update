from src.core.connet_db import db

def getAllCurrenciesDB ():
  database = db()
  collection = database['exchange-rates']

  currencies = collection.find()

  return currencies