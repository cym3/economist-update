import re
from src.economicActivityAggregate.domain.requiredFields.economic_activity import Indicator
from src.economicActivityAggregate.domain.entities.create_tasks import createTaskDB
from src.economicActivityAggregate.domain.errors.create_error import createError

def validatePage(df: dict,indicator: Indicator):
  title = indicator['page_title']
  name = indicator['name']

  try:
    text = str(df.loc[0])

    if re.search(title, text) is None:
      raise Exception('Page not found')

  except Exception as err:
    print(err)
    errorMessage = f'{name}: Invalid indicator sheet'

    createTaskDB(isDone=False, error=errorMessage)

    createError(errorMessage)