from src.interestRates.domain.entities.get_last_update_date import getLastUpdateDateDB
from src.interestRates.services.interest_rates import interestRatesService
from src.interestRates.domain.entities.save_interest_rates import saveInterestRatesDB
from datetime import datetime, timedelta

def interestRatesUseCase(): 
    now = datetime.now()
    today = now.strftime('%Y-%m-%d')

    last_date_in_DB = getLastUpdateDateDB()
    date = datetime.strptime(last_date_in_DB, '%Y-%m-%d')

    new_date = date.strftime('%Y-%m-%d')

    interestRates = []

    while today != new_date:
        print(new_date)
        date = date + timedelta(days=1)
        new_date = date.strftime('%Y-%m-%d')

        interestRates = interestRatesService(new_date)

        saveInterestRatesDB(interestRates)

    return interestRates
