from src.interestRates.infra.main import ratesInfra
from src.interestRates.domain.requiredFields.page_validator import dataValidator
from src.interestRates.domain.entities.get_last_update_date import getLastUpdateDateDB
from src.interestRates.services.main import interestRatesService
from src.interestRates.domain.entities.save_interest_rates import saveInterestRatesDB
from datetime import datetime
from src.interestRates.indicators import indicators


def interestRatesUseCase(): 
    interestRates = []
    
    for indicator in indicators:
        rates = ratesInfra(indicator=indicator)
        dataValidator(data=rates, indicator=indicator)

        now = datetime.now()
        today = now.strftime('%Y-%m-%d')

        last_date_in_DB = getLastUpdateDateDB(indicator)

        if today != last_date_in_DB:
            interestRates = interestRatesService(today, rates, indicator)

            saveInterestRatesDB(interestRates, indicator)

    return interestRates
