from src.eai.domain.requiredFields.eai import DateEAI, Indicator
from src.eai.services.fetch.fetch import fetchEAI

def check_updateService(date: DateEAI, indicator: Indicator):   
  fetch_result = fetchEAI(date)

  if fetch_result is not None:
    id = fetch_result['id']
    path = fetch_result['path']
    date = fetch_result['date']

    name = indicator['name']

    howToUpdate = f"""
      Go to INE website download {name} pdf file, convert the file to excel,
      then add the excel file to {name} update system, and run the system.

      Link to the pdf file: {path}
    """

    task = {
      'id': id,
      'howToUpdate': howToUpdate,
      'date': date
    }

    return task


  return None
