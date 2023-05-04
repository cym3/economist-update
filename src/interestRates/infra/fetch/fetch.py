from src.currentCurrencyTrades.domain.requiredFields.currencies import Indicator
from src.currentCurrencyTrades.domain.entities.create_tasks import createTaskDB
from src.currentCurrencyTrades.domain.errors.create_error import createError
import requests

url = 'https://www.bancomoc.mz/bmapi/interest-rates'

headers = {
  'authority': 'www.bancomoc.mz',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'gid=GA1.2.1374688689.1682940354; _gat_UA-217411436-1=1; _ga=GA1.1.1118171234.1682788112; _ga_PF3QZGT45B=GS1.1.1683000555.5.1.1683000572.0.0.0',
  'referer': 'https://www.bancomoc.mz/',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
}

def fetchTrades(indicator: Indicator):
  db_name = indicator['db_name']

  result = {}
  try:
    response = requests.get(url=url, headers=headers)
    result = response.json()

  except Exception as err:
    print(err)
    errorMessage = f'Could not fetch the {db_name}, the url is {url}'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return result