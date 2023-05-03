from src.utils.date.index import CreateDateUTC
from dateutil.relativedelta import relativedelta
import re
from src.economicActivityAggregate.services.utils.find.filter_row import filter_row
from src.economicActivityAggregate.services.utils.months import months

def get_end_year(years_row: list):
  years = []

  for el in years_row:
    if type(el) == type(1):
      years.append(el)

  return years[-1]


def get_end_month(months_row: list):
  end_month = months_row[-1]

  index = 0
  for m in months:
    if re.search(end_month.lower(), m) is not None:
      return index + 1
    index += 1


def findDatesRow(table: list, first_row_index: int):
  years_row = filter_row(table[first_row_index -2])
  end_year = get_end_year(years_row)

  months_row = filter_row(table[first_row_index -1])
  end_month = get_end_month(months_row)

  dates_row = []

  index = 0
  for m in months_row:
    now = CreateDateUTC(end_year, end_month, 1).date
    new_date = now - relativedelta(months=index)

    dates_row.insert(0, new_date)
    index += 1
    
  return dates_row