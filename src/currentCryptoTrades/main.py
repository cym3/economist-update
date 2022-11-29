from src.currentCryptoTrades.services.main import currencyTradesService
from src.currentCryptoTrades.domain.entities.save_current_trades import saveCurrentTradesDB
from src.currentCryptoTrades.domain.entities.get_all_currencies import getAllCurrenciesDB
from src.currentCryptoTrades.indicators import indicators

def currentCryptoTradesUseCase():
    currenciesTrades = []

    for indicator in indicators:
        currencies = getAllCurrenciesDB(indicator)
                
        currenciesTrades = currencyTradesService(currencies, indicator)

        # saveCurrentTradesDB(currenciesTrades, indicator)

    return currenciesTrades
