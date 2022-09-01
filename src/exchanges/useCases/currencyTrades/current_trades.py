from src.core.domain.mail.sand_mail import sandMail
from src.exchanges.services.currencyTrades.current_trades import currencyTradesService
from src.exchanges.domain.entities.currencyTrades.save_current_trades import saveCurrentTradesDB
from src.exchanges.domain.entities.currencyTrades.get_all_currencies import getAllCurrenciesDB

async def currentTradesUseCase():
    currencies = await getAllCurrenciesDB()
    
    currenciesTrades = await currencyTradesService(currencies)

    await saveCurrentTradesDB(currenciesTrades)

    errorTitle = f'Database has failed'
    errorMessage = f'Database failed to get currencies'

    await sandMail(title=errorTitle, message=errorMessage)

    return currenciesTrades
