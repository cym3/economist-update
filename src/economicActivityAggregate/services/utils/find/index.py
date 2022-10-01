from rapidfuzz.process import extractOne

def findFirstRow(table: list):
  pattern = 'Indicador do Clima Económico'

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