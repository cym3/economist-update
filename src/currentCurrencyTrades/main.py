from src.core.mail.sand_mail import sandMail
from src.currentCurrencyTrades.services.current_trades import currencyTradesService
from src.currentCurrencyTrades.domain.entities.save_current_trades import saveCurrentTradesDB
from src.currentCurrencyTrades.domain.entities.get_all_currencies import getAllCurrenciesDB

async def currentTradesUseCase():
    currencies = await getAllCurrenciesDB()
    
    currenciesTrades = await currencyTradesService(currencies)

    await saveCurrentTradesDB(currenciesTrades)

    errorTitle = f'Database has failed'
    errorMessage = f'Database failed to get currencies'

    await sandMail(title=errorTitle, message=errorMessage)

    return currenciesTrades
