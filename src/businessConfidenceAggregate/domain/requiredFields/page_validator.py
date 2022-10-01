import re
from src.businessConfidenceAggregate.domain.entities.create_tasks import createTaskDB
from src.businessConfidenceAggregate.domain.errors.create_error import createError
from src.businessConfidenceAggregate.aws.parse.text import textParser
from src.businessConfidenceAggregate.domain.requiredFields.business_confidence import Indicator

def fileValidator(textExtractResponse: dict, indicator: Indicator):
  page_identifiers: list[str] = indicator['page_identifiers']
  db_name: str = indicator['db_name']

  valide_page = True

  try: 
    texts = textParser(textExtractResponse)
    text = ' '.join(texts)

    for identifier in page_identifiers:
      if re.search(identifier, text) is None:
        valide_page = False

    if valide_page is False:
      raise Exception(f'Invalid pdf page, the data contained by pdf dois not look like {db_name} data.')
  
  except Exception as err:
    print(err)
    errorMessage = f'Invalid pdf page, the data contained by pdf dois not look like {db_name} data.'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)

  return valide_page