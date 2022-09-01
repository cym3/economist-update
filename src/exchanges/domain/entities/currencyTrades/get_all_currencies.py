from src.core.domain.errors.domain_error import DatabaseFailError
from src.core.domain.mail.sand_mail import sandMail
from src.core.connect_db import db

async def getAllCurrenciesDB ():
  currencies = []

  try: 
    database = db()
    collection = database['exchange-rates']

    currencies = collection.find()

  except Exception:
    errorTitle = f'Database has failed'
    errorMessage = f'Database failed to get currencies'

    await sandMail(title=errorTitle, message=errorMessage)

    raise DatabaseFailError(f'{errorTitle} f{errorMessage}')

  return currencies