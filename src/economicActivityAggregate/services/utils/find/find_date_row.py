from datetime import datetime
import re
from src.economicActivityAggregate.services.utils.find.filter_row import filter_row
from src.economicActivityAggregate.services.utils.months import months

def findLastYear(years_row: list):
  years = []
  
  for el in years_row:
    if type(el) == type(1):
      years.append(el)

  return years[-1]


def yearsFilter(years_row: list):
  years_row = filter_row(years_row)

  year = findLastYear(years_row)
  years = []

  # reverse the order of list elements
  years_row.reverse()

  # Fill NaN list elements with the respective years
  for el in years_row:
    if type(el) == type(1):
      years.append(year)
      year = year -1

    else:
      years.append(year)

  # UnReverse the order of list elements
  years.reverse()
  return years

def createMonths(months_row: list):
  months_row = filter_row(months_row)

  months_int = []

  for el in months_row:
    index = 0

    for m in months:
      if re.search(el.lower(), m) is not None:
        months_int.append(index + 1)

      index += 1

  return months_int


def findDatesRow(sheet: list, first_row_index: int):
  years_row = yearsFilter(sheet[first_row_index -2])
  months_row = createMonths(sheet[first_row_index -1])

  dates_row = []

  index = 0
  for month in months_row:
    year = years_row[index]
    date = datetime(year, month, 1)
    dates_row.append(date)

    index += 1

  return dates_row