from src.interestRates.domain.entities.get_last_update_date import getLastUpdateDateDB
from src.interestRates.services.interest_rates import interestRatesService
from src.interestRates.domain.entities.save_interest_rates import saveInterestRatesDB
from datetime import datetime, timedelta

async def interestRatesUseCase(): 
    now = datetime.now()
    today = now.strftime('%Y-%m-%d')

    last_date_in_DB_str = await getLastUpdateDateDB()
    last_date_in_DB = datetime.strptime(last_date_in_DB_str, '%Y-%m-%d')

    date = last_date_in_DB + timedelta(days=1)
    new_date = date.strftime('%Y-%m-%d')

    interestRates = []

    while today != new_date:
        interestRates = await interestRatesService(new_date)

        await saveInterestRatesDB(interestRates)

        date = date + timedelta(days=1)
        new_date = date.strftime('%Y-%m-%d')

    return interestRates
