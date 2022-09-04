from src.currentCurrencyTrades.services.current_trades import currencyTradesService
from src.currentCurrencyTrades.domain.entities.save_current_trades import saveCurrentTradesDB
from src.currentCurrencyTrades.domain.entities.get_all_currencies import getAllCurrenciesDB

async def currentTradesUseCase():
    currencies = await getAllCurrenciesDB()
    
    currenciesTrades = await currencyTradesService(currencies)

    await saveCurrentTradesDB(currenciesTrades)

    return currenciesTrades
