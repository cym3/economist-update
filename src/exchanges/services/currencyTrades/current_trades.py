from src.exchanges.services.currencyTrades.utils.format_currency_trades import formatCurrencyTrades
from src.exchanges.services.currencyTrades.utils.find_currency_trades import findCurrencyTrades
from src.exchanges.services.currencyTrades.fetch.fetch_trades import fetchTrades
from src.exchanges.domain.requiredFields.currencyTrades.currencies import Currency
from src.core.domain.errors.domain_error import DataFetchError
from datetime import datetime


async def currencyTradesService(currencies: list[Currency]):
    now = datetime.now()
    date = now.strftime('%Y-%m-%d %H:%M:%S')

    trades = await fetchTrades(date=date)
    trades_by_1 = trades['trades_by_1']
    trades_by_1000 = trades['trades_by_1000']

    newCurrenciesTrades = []
    
    for currency in currencies:
        countryName = currency['country']
        currencyTrades = findCurrencyTrades(countryName=countryName, currenciesTrades=trades_by_1)

        if currencyTrades is not None:
            formattedTrades = await formatCurrencyTrades(
                trades=currencyTrades,
                date=date,
                divider=1,
                countryName=countryName,
                isoCode=currency['iso']['code']
            )

            newCurrenciesTrades.append(formattedTrades)

        if currencyTrades is None:
            currencyTrades = findCurrencyTrades(countryName=countryName, currenciesTrades=trades_by_1000)

            if currencyTrades is not None:
                formattedTrades = await formatCurrencyTrades(
                    trades=currencyTrades,
                    date=date,
                    divider=1000,
                    countryName=countryName,
                    isoCode=currency['iso']['code']
                )

                newCurrenciesTrades.append(formattedTrades)

            if currencyTrades is None:
                raise DataFetchError(
                    f'Exchange Rates could not be updated {date}: The {countryName} currency could not be found'
                )
        
    return newCurrenciesTrades
