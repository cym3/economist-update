from src.interestRates.domain.entities.get_last_update_date import getLastUpdateDateDB
from src.interestRates.services.interest_rates import interestRatesService
from src.interestRates.domain.entities.save_interest_rates import saveInterestRatesDB
from datetime import datetime, timedelta

async def interestRatesUseCase():    
    last_update_str = await getLastUpdateDateDB()
    last_update = datetime.strptime(last_update_str, '%Y-%m-%d')

    new_date = last_update + timedelta(days=1)
    date = new_date.strftime('%Y-%m-%d')

    interestRates = await interestRatesService(date)

    await saveInterestRatesDB(interestRates)

    return interestRates
