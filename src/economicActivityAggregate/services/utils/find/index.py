from rapidfuzz.process import extractOne

from src.economicActivityAggregate.domain.requiredFields.economic_activity import Indicator

def findFirstRow(table: list, indicator: Indicator):
  pattern: str = indicator['name']

  names = [row[0] for row in table]

  match = extractOne(pattern, names)
  match_score  = match[-2]
  matched_index  = match[-1]

  if (match_score > 90):
    return matched_index


def findLastRow(table: list):
  pattern = 'Indicador de Expectativas de Preços'

  names = [row[0] for row in table]

  match = extractOne(pattern, names)
  match_score  = match[-2]
  matched_index  = match[-1]

  if (match_score > 90):
    return matched_index