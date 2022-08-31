from src.core.connet_db import db


def saveCurrentTratesDB ():
  database = db()
  collection = database['exchange-rates-test']

  currentTrades = {
    'buy': 639.24,
    'sale': 643.5,
    'date': '2022-08-20 17:00'
  }

  collection.update_one(
    {'iso.code': 'USD'},
    {'$set': { 'currentTrades': currentTrades }}
  )

  return 'Done'