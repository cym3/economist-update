from datetime import datetime
from typing import Union
from dateutil.relativedelta import relativedelta
import re
from src.cpi.domain.requiredFields.cpi import DateCpi
from src.cpi.services.utils.find.filter_row import filter_row
from src.cpi.services.utils.months import min_months

def get_year(date_str: str, date: DateCpi):
  old_year: int = date['year']
  years = [old_year - 1, old_year, old_year + 1]

  for y in years:
    strs_y = [x for x in str(y)]
    min_year = f'{strs_y[2]}{strs_y[3]}'

    yearMatch = re.search(min_year, date_str)

    if (yearMatch is not None):
      return y


def get_month(date_str: list):
  index = 0
  for m in min_months:
    monthMatch = re.search(m, date_str)

    if (monthMatch is not None):
      return index + 1

    index += 1


def datesRowFormatter(dates_row: list[str], date: DateCpi):
  dates_row = filter_row(dates_row)

  start_date: Union[datetime, str] = dates_row[0]

  start_year = 0
  start_month = 0

  if isinstance(start_date, datetime):
    start_year = start_date.year
    start_month = start_date.month
  else:
    start_year = get_year(start_date, date)
    start_month = get_month(start_date)

  new_dates = []

  index = 0
  for el in dates_row:
    now = datetime(start_year, start_month, 1)
    new_date = now + relativedelta(months=index)

    new_dates.append(new_date)
    index += 1
    
  return new_dates