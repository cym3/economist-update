import re
from src.currentCurrencyTrades.domain.requiredFields.currencies import Indicator
from src.currentCurrencyTrades.domain.entities.create_tasks import createTaskDB
from src.currentCurrencyTrades.domain.errors.create_error import createError
from src.currentCurrencyTrades.aws.parse.text import textParser
from rapidfuzz.fuzz import partial_ratio

page_identifiers: list[str] = ['1. POR UNIDADE DE MOEDA ESTRANGEIRA', '2. METICAIS POR 1000 UNIDADES DE MOEDA ESTRANGEIRA']

def fileValidator(textExtractResponse: dict, indicator: Indicator):
  db_name = indicator['db_name']
  try: 
    valide_page = True
    texts = textParser(textExtractResponse)
    text = ' '.join(texts)

    for identifier in page_identifiers:
      match_score = partial_ratio(text, identifier)

      if (match_score < 85):
        valide_page = False

    if valide_page is False:
      raise Exception(f'Invalid pdf page, the data contained by pdf dois not look like {db_name} data.')
  
  except Exception as err:
    print(err)
    errorMessage = f'Invalid pdf page, the data contained by pdf dois not look like {db_name} data.'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return valide_page