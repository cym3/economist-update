from src.exchanges.services.currencyTrades.current_trades import currenctTradesService
from src.exchanges.domain.entities.currencyTrades.current_trades import currentTratesDB

async def currentTradesUseCase():
    currencies = currenctTradesService()

    # exchangeRate = currentTratesDB()

    return currencies
