from src.creditByPurpose.domain.requiredFields.credit import DateCredit
from src.creditByPurpose.domain.entities.create_tasks import createTaskDB
from src.creditByPurpose.domain.errors.create_error import createError
from src.creditByPurpose.services.utils.months import months
from src.creditByPurpose.domain.requiredFields.credit import Indicator
from rapidfuzz.fuzz import partial_ratio

dateRowName = 'Sectores de Actividade'
def findDateRow(table: list[list]):
  for row in table:
    match_score = partial_ratio(dateRowName, f'{row[1]}')

    if (match_score > 90):
      return row


def findNewYear(old_year: int, new_date: str):
  years = [old_year, old_year + 1]

  for year in years:
    strs_y = [x for x in str(year)]
    min_year = f'{strs_y[2]}{strs_y[3]}'

    match_score = partial_ratio(min_year, new_date)

    if (match_score > 90):
      return year

def findNewMonth(new_date: str):
  new_date = new_date.lower()
  index = 0
  for month in months:
    match_score = partial_ratio(new_date, month)

    if (match_score > 90):
      return index + 1

    index +=1

def getNewDate(table: list, date: DateCredit, indicator: Indicator):
  db_name = indicator['db_name']

  try:
    dates_row = findDateRow(table)

    new_date = dates_row[-3]

    old_year = date['year']

    year = findNewYear(old_year, new_date)
    
    month = findNewMonth(new_date)

    date = {
      'year': year,
      'month': month
    }

  except Exception as err:
    print(err)
    errorMessage = f'Date in the {db_name} table could not be processed. It could be a problem format from header table row or column.'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return date
