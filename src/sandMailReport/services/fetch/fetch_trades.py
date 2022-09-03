import camelot
from src.core.errors.domain_error import DataFetchError
from src.core.mail.sand_mail import sandMail

url = 'https://www.bancomoc.mz/Files/REFR/ZMMIREFR.pdf'

async def fetchTrades(date: str):
  try:
    table_by_1 = camelot.read_pdf(url, flavor='stream', table_regions=['170,530,560,270'])[0] 
    table_by_1000 = camelot.read_pdf(url, flavor='stream', table_regions=['170,210,600,130'])[0] 

    trades_by_1 = table_by_1.df.values.tolist()
    trades_by_1000 = table_by_1000.df.values.tolist()
      
    return { 
        'trades_by_1': trades_by_1,
        'trades_by_1000': trades_by_1000
    }
  except Exception:
    errorTitle = f'Exchange Rates could not be updated {date}'
    errorMessage = f'Could not fetch the exchange Rates, the url is {url}'

    await sandMail(title=errorTitle, message=errorMessage)

    raise DataFetchError(f'{errorTitle} f{errorMessage}')