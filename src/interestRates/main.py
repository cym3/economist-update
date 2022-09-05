from src.interestRates.services.interest_rates import interestRatesService
from src.interestRates.domain.entities.save_interest_rates import saveInterestRatesDB

async def interestRatesUseCase():    
    interestRates = await interestRatesService()

    await saveInterestRatesDB(interestRates)

    return interestRates
