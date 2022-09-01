from src.exchanges.services.currencyTrades.current_trades import currencyTradesService
from src.exchanges.domain.entities.currencyTrades.save_current_trades import saveCurrentTradesDB
from src.exchanges.domain.entities.currencyTrades.get_all_currencies import getAllCurrenciesDB

async def currentTradesUseCase():
    currencies = getAllCurrenciesDB()
    
    currenciesTrades = await currencyTradesService(currencies)

    await saveCurrentTradesDB(currenciesTrades)

    return currenciesTrades
