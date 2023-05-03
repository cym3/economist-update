from src.currentCurrencyTrades.infra.main import tradesInfra
from src.currentCurrencyTrades.domain.requiredFields.page_validator import dataValidator
from src.currentCurrencyTrades.services.main import currencyTradesService
from src.currentCurrencyTrades.domain.entities.save_current_trades import saveCurrentTradesDB
from src.currentCurrencyTrades.domain.entities.get_all_currencies import getAllCurrenciesDB
from src.currentCurrencyTrades.indicators import indicators

def currentCurrencyTradesUseCase():
    currenciesRates = []
    
    for indicator in indicators:

        response = tradesInfra(indicator=indicator)
        trades = dataValidator(data=response, indicator=indicator)

        currencies = getAllCurrenciesDB(indicator)
                
        currenciesRates = currencyTradesService(currencies, trades, indicator)

        saveCurrentTradesDB(currenciesRates, indicator)

    return currenciesRates
