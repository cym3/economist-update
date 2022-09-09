from src.interestRates.domain.entities.create_tasks import createTaskDB
from src.interestRates.domain.errors.create_error import createError
from src.interestRates.services.utils.format_interest_rates import formatInterestRates
from src.interestRates.services.fetch.fetch_rates import fetchRates
from src.interestRates.services.utils.find_interest_rates import findInterestRates

def interestRatesService(date: str):

  html = fetchRates(date)
  table = findInterestRates(html)

  interestRates = formatInterestRates(table=table, date=date)

  return interestRates
