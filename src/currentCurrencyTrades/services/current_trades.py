from src.currentCurrencyTrades.domain.errors.create_error import create_error
from src.currentCurrencyTrades.services.utils.format_currency_trades import formatCurrencyTrades
from src.currentCurrencyTrades.services.utils.find_currency_trades import findCurrencyTrades
from src.currentCurrencyTrades.services.fetch.fetch_trades import fetchTrades
from src.currentCurrencyTrades.domain.requiredFields.currencies import Currency
from datetime import datetime


async def currencyTradesService(currencies: list[Currency]):
    now = datetime.now()
    date = now.strftime('%Y-%m-%d %H:%M:%S')

    trades = await fetchTrades(date=date)
    trades_by_1 = trades['trades_by_1']
    trades_by_1000 = trades['trades_by_1000']

    newCurrenciesTrades = []
    
    for currency in currencies:
        countryName: str = currency['country']
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
                errorMessage = f'The {countryName} currency could not be found'

                await create_error(errorMessage)

    return newCurrenciesTrades
