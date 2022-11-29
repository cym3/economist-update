from src.currentCryptoTrades.services.utils.format_currency_trades import formatCurrencyTrades
from src.currentCryptoTrades.domain.requiredFields.currencies import Currency, Indicator
from datetime import datetime

def currencyTradesService(currencies: list[Currency], trade: dict, indicator: Indicator):
  now = datetime.now()
  date = now.strftime('%Y-%m-%d %H:%M:%S')

  updatedCryptoCurrencies = []

  for currency in currencies: 
    isoCode = currency['iso']['code']

    new_updates = {
      'current_change': trade['current_change'][f'{isoCode}-USD'],
      'current_price': trade['current_price'][f'{isoCode}-USD'],
      'current_percent_change': trade['current_percent_change'][f'{isoCode}-USD'],
      'market_cap': trade['market_cap'][f'{isoCode}-USD'],
      'current_volume': trade['current_volume'][f'{isoCode}-USD'],
      'date': date
    }

    currency['currentTrades'] = new_updates
    currency['_id'] = ''

    updatedCryptoCurrencies.append(currency)
    
  return updatedCryptoCurrencies
    