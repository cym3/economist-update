from src.businessConfidenceAggregate.domain.requiredFields.business_confidence import Quarter
from src.businessConfidenceAggregate.domain.requiredFields.business_confidence import Indicator
from src.businessConfidenceAggregate.services.fetch.fetch import fetchBusinessConfidence
from datetime import datetime

def check_updateService(quarter: Quarter, indicator: Indicator):   
  fetch_result = fetchBusinessConfidence(quarter)

  if fetch_result is not None:
    path = fetch_result['path']

    year = fetch_result['quarter']['year']
    month = fetch_result['quarter']['toMonth']

    now = datetime(year, month, 1)
    new_date = now.strftime('%Y-%m-%d %H:%M:%S')

    scheduleCode = indicator['scheduleCode']
    name = indicator['name']

    howToUpdate = f"""
      Go to INE website download {name} pdf file, go to https://www.ilovepdf.com/ convert the pdf file to excel, download and rename to 'business-confidence.xlsx'
      then add the file to {name} update system, and run the system.

      Link to the pdf file: {path}
    """

    task = {
      'scheduleCode': scheduleCode,
      'howToUpdate': howToUpdate,
      'date': new_date
    }

    return task

  return None
