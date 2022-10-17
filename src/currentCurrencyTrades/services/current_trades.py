from src.currentCurrencyTrades.domain.entities.create_tasks import createTaskDB
from src.currentCurrencyTrades.domain.errors.create_error import createError
from src.currentCurrencyTrades.services.utils.format_currency_trades import formatCurrencyTrades
from src.currentCurrencyTrades.services.utils.find_currency_trades import findCurrencyTrades
from src.currentCurrencyTrades.domain.requiredFields.currencies import Currency
from datetime import datetime

def currencyTradesService(currencies: list[Currency], tables: list):
    now = datetime.now()
    date = now.strftime('%Y-%m-%d %H:%M:%S')

    trades_by_1 = tables[0]
    trades_by_1000 = tables[1]

    newCurrenciesTrades = []
    
    for currency in currencies:
        countryName: str = currency['country']
        tableRow = findCurrencyTrades(countryName=countryName, currenciesTrades=trades_by_1)

        if tableRow is not None:
            formattedTrades = formatCurrencyTrades(
                tableRow=tableRow,
                date=date,
                divider=1,
                countryName=countryName,
                isoCode=currency['iso']['code']
            )

            newCurrenciesTrades.append(formattedTrades)

        if tableRow is None:
            tableRow = findCurrencyTrades(countryName=countryName, currenciesTrades=trades_by_1000)

            if tableRow is not None:
                formattedTrades = formatCurrencyTrades(
                    tableRow=tableRow,
                    date=date,
                    divider=1000,
                    countryName=countryName,
                    isoCode=currency['iso']['code']
                )

                newCurrenciesTrades.append(formattedTrades)

            if tableRow is None:
                createTaskDB(isDone=False)
                errorMessage = f'The {countryName} currency could not be found'

                createError(errorMessage)

    return newCurrenciesTrades
