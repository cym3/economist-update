from src.economicActivityAggregate.domain.requiredFields.economic_activity import DateEconomicActivity, Indicator
from src.economicActivityAggregate.services.fetch.fetch import fetchEconomicActivity
from datetime import datetime

def check_updateService(date: DateEconomicActivity, indicator: Indicator):   
  fetch_result = fetchEconomicActivity(date)

  if fetch_result is not None:
    path = fetch_result['path']

    year = fetch_result['date']['year']
    month = fetch_result['date']['month']

    now = datetime(year, month, 1)
    new_date = now.strftime('%Y-%m-%d %H:%M:%S')

    scheduleCode = indicator['scheduleCode']
    name = indicator['name']

    howToUpdate = f"""
      Go to INE website download {name} pdf file, go to https://www.ilovepdf.com/ convert the pdf file to excel, download and rename to 'economic-activity.xlsx'
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
