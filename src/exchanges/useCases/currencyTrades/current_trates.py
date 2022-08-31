from src.exchanges.services.currencyTrades.current_trades import currenctTradesService
from src.exchanges.domain.entities.currencyTrades.save_current_trades import saveCurrentTratesDB
from src.exchanges.domain.entities.currencyTrades.get_all_currencies import getAllCurrenciesDB

async def currentTradesUseCase():
    currencies = getAllCurrenciesDB()
    
    currenciesTrades = await currenctTradesService(currencies)

    # exchangeRate = saveCurrentTratesDB()

    return currenciesTrades
