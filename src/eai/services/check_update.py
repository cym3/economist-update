from src.eai.domain.requiredFields.eai import DateEAI, Indicator
from src.eai.services.fetch.fetch import fetchEAI
from datetime import datetime

def check_updateService(date: DateEAI, indicator: Indicator):   
  fetch_result = fetchEAI(date)

  if fetch_result is not None:
    path = fetch_result['path']

    year = fetch_result['date']['year']
    month = fetch_result['date']['month']

    now = datetime(year, month, 1)
    new_date = now.strftime('%Y-%m-%d %H:%M:%S')

    id = indicator['id']
    name = indicator['name']

    howToUpdate = f"""
      Go to INE website download {name} pdf file, convert the file to excel and rename to 'economist-activity.xlsx'
      then add the excel file to {name} update system, and run the system.

      Link to the pdf file: {path}
    """

    task = {
      'id': id,
      'howToUpdate': howToUpdate,
      'date': new_date
    }

    return task

  return None
