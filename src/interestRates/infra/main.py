from src.interestRates.domain.requiredFields.interest_rates import Indicator
from src.interestRates.infra.fetch.fetch import fetchTrades

def ratesInfra(indicator: Indicator):   
  rates = fetchTrades(indicator)

  return rates
