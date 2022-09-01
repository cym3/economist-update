from src.core.domain.errors.domain_error import DatabaseFailError
from src.core.domain.mail.sand_mail import sandMail
from src.core.connect_db import db
from pydantic import BaseModel

class CurrencyTrade(BaseModel):
  isoCode: str
  buy: float
  sale: float
  date: str

async def saveCurrentTradesDB (currencyTrades: list[CurrencyTrade]):
  try:
    database = db()
    collection = database['exchange-rates']

    for currency in currencyTrades:
      collection.update_one(
        {
          'iso.code': currency['isoCode']
        },
        { '$set': { 'currentTrades': currency['trade'] }}
    )

  except Exception:
    errorTitle = f'Database has failed'
    errorMessage = f'Was not able to save exchange rates, { currencyTrades[0].date }'

    await sandMail(title=errorTitle, message=errorMessage)

    raise DatabaseFailError(f'{errorTitle} f{errorMessage}')

  return 'Done'