from rapidfuzz.process import extractOne

def findFirstRow(table: list):
  pattern = 'Produção Industrial'

  names = [row[0] for row in table]

  match = extractOne(pattern, names)

  match_score  = match[-2]
  matched_index  = match[-1]

  if (match_score > 90):
    return matched_index


def findLastRow(table: list):
  pattern = 'Perspectivas Volume de Negócios'

  names = [row[0] for row in table]

  match = extractOne(pattern, names)
  match_score  = match[-2]
  matched_index  = match[-1]

  if (match_score > 90):
    return matched_index