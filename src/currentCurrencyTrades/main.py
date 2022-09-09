from src.currentCurrencyTrades.services.current_trades import currencyTradesService
from src.currentCurrencyTrades.domain.entities.save_current_trades import saveCurrentTradesDB
from src.currentCurrencyTrades.domain.entities.get_all_currencies import getAllCurrenciesDB

def currentCurrencyTradesUseCase():
    currencies = getAllCurrenciesDB()
    
    currenciesTrades = currencyTradesService(currencies)

    saveCurrentTradesDB(currenciesTrades)

    return currenciesTrades
