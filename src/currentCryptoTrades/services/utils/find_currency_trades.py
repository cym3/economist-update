from src.currentCryptoTrades.domain.requiredFields.currencies import Currency
from src.currentCryptoTrades.domain.entities.create_tasks import createTaskDB
from src.currentCryptoTrades.domain.errors.create_error import createError
from src.currentCryptoTrades.domain.requiredFields.currencies import Indicator
from yahoofinancials import YahooFinancials


def findCurrencyTrades(currencies: list[Currency], indicator: Indicator):
  new_updates = {}
  
  try: 
    cryptoIsoCodes: list[str] = []
    
    for currency in currencies:
      isoCode: str = currency['iso']['code']
      cryptoIsoCodes.append(f'{isoCode}-USD')   

    yahoo_financials_cryptocurrencies = YahooFinancials(cryptoIsoCodes)

    current_change = yahoo_financials_cryptocurrencies.get_current_change()
    current_price = yahoo_financials_cryptocurrencies.get_current_price()
    current_percent_change = yahoo_financials_cryptocurrencies.get_current_percent_change()
    market_cap = yahoo_financials_cryptocurrencies.get_market_cap()
    current_volume = yahoo_financials_cryptocurrencies.get_current_volume()

    new_updates = {
      'current_change': current_change,
      'current_price': current_price,
      'current_percent_change': current_percent_change,
      'market_cap': market_cap,
      'current_volume': current_volume
    }

  except Exception as err:
    print(err)
    errorMessage = 'Failed to get crypto currencies trades from Yahoo Finance'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return new_updates