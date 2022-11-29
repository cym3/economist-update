from src.currentCryptoTrades.infra.main import currentCryptoTradesInfra
from src.currentCryptoTrades.services.main import currencyTradesService
from src.currentCryptoTrades.domain.entities.save_current_trades import saveCurrentTradesDB
from src.currentCryptoTrades.domain.entities.get_all_currencies import getAllCurrenciesDB
from src.currentCryptoTrades.indicators import indicators

def currentCryptoTradesUseCase():
    currenciesTrades = []

    for indicator in indicators:
        crypto_currencies = getAllCurrenciesDB(indicator)

        trade = currentCryptoTradesInfra(crypto_currencies, indicator)

        currenciesTrades = currencyTradesService(crypto_currencies, trade, indicator)

        # saveCurrentTradesDB(currenciesTrades, indicator)

    return currenciesTrades
