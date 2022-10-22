from src.businessConfidenceBySector.domain.requiredFields.business_confidence import Indicator, Quarter
from typing import Union
from src.businessConfidenceBySector.domain.entities.create_tasks import createTaskDB
from src.businessConfidenceBySector.domain.errors.create_error import createError
from rapidfuzz.process import extractOne

name = 'Serviços'

def servicesFormatter(
  table: list[list[Union[float, str]]],
  new_quarter: Quarter,
  indicator: Indicator
):
  db_name = indicator['db_name']
  values = []

  try:
    row_is_found = False

    names = [row[0] for row in table]

    match = extractOne(name, names)
    match_score  = match[-2]
    matched_index  = match[-1]

    if (match_score > 85):
      row_is_found = True

      row = table[matched_index]
      column_index = indicator['column_index']

      value = row[column_index]

      values.append({
        'quarter': new_quarter,
        'value': value
      })

    if row_is_found == False:
      raise Exception(f"'{name}' index is not found on the excel file.")

  except Exception as err:
    print(err)
    errorMessage = f'{db_name}: has a format error on {name}'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return {
    'id': '6332ee71feef414249d8dc37',
    'values': values
  }
