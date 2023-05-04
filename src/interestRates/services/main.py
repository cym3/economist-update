from src.interestRates.domain.requiredFields.interest_rates import Indicator
from src.interestRates.services.utils.format_interest_rates import formatInterestRates
from src.interestRates.domain.requiredFields.page_validator import InterestRates

def interestRatesService(date: str, interestRates: InterestRates, indicator: Indicator):
  rates = interestRates['rates']

  interestRates = formatInterestRates(rates=rates, date=date, indicator=indicator)

  return interestRates
