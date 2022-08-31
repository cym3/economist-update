from src.exchanges.services.currencyTrades.utils.find_currency_trades import findCurrencyTrades
from src.exchanges.services.currencyTrades.fetch.fetch_trades import fetchTrades
from src.exchanges.domain.requiredFields.currencyTrades.currencies import Currency



async def currenctTradesService(currecies: list[Currency]):
    trades = await fetchTrades()
    trades_by_1 = trades['trades_by_1']
    trades_by_1000 = trades['trades_by_1000']

    newCurrenciesTrades = []
    
    for currency in currecies:
        currencyTrades = findCurrencyTrades(trades_by_1, currency['country'])

        if currencyTrades is not None:
            currency['currentTrades'] = {
                'buy': 0.1673,
                'sale': 0.17063,
                'date': '2022-08-20 17:00'
            }
        if currencyTrades is None:
            currencyTrades = findCurrencyTrades(trades_by_1000, currency['country'])

            currency['currentTrades'] = {
                'buy': 0.1673,
                'sale': 0.17063,
                'date': '2022-08-20 17:00'
            }
            if currencyTrades is None :
                print(currency['country'])
        
        newCurrenciesTrades.append(currency)

    return 'Done'
