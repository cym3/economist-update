from src.interestRates.domain.requiredFields.interest_rates import Indicator
from src.interestRates.services.utils.format_interest_rates import formatInterestRates
from src.interestRates.services.fetch.fetch_rates import fetchRates
from src.interestRates.services.utils.find_interest_rates import findInterestRates

def interestRatesService(date: str, indicator: Indicator):
  html = fetchRates(date)
  table = findInterestRates(html)

  interestRates = formatInterestRates(table=table, date=date, indicator=indicator)

  return interestRates
