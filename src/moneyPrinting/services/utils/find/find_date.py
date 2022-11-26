from datetime import datetime
from src.moneyPrinting.domain.requiredFields.main import DateMoneyPrinting
from src.moneyPrinting.domain.entities.create_tasks import createTaskDB
from src.moneyPrinting.domain.errors.create_error import createError
from src.moneyPrinting.domain.requiredFields.main import Indicator

def findDateRow(table: list[list]):
  return table[1]

def getNewDate(table: list, date: DateMoneyPrinting, indicator: Indicator):
  db_name = indicator['db_name']

  try:
    dates_row = findDateRow(table)

    new_date: datetime = dates_row[-1]

    year = new_date.year
    month = new_date.month

    date = {
      'year': year,
      'month': month
    }

  except Exception as err:
    print(err)
    errorMessage = f'Date in the {db_name} table could not be processed. It could be a problem format from header table row or column.'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return date
