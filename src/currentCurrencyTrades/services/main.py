from src.currentCurrencyTrades.domain.requiredFields.page_validator import ExchangeRates, Rate
from src.currentCurrencyTrades.services.utils.format_currency_rate import formatCurrencyRate
from src.currentCurrencyTrades.services.utils.find_currency_rate import findCurrencyRate
from src.currentCurrencyTrades.domain.requiredFields.currencies import Currency, Indicator
from src.utils.date.index import createDateUTC

def currencyTradesService(currencies: list[Currency], trades: ExchangeRates, indicator: Indicator):
    now = createDateUTC()

    updatedCurrencies = []

    rates: list[Rate] = trades['rates']
    
    for currency in currencies:
        isoCode: str = currency['iso']['code']
        rate = findCurrencyRate(isoCode=isoCode, rates=rates, indicator=indicator)

        if rate is not None:
            formattedRate = formatCurrencyRate(
                rate=rate,
                date=now,
                isoCode=isoCode,
                indicator=indicator
            )

            updatedCurrencies.append(formattedRate)


    return updatedCurrencies
