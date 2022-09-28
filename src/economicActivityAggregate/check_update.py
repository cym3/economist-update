from src.economicActivityAggregate.services.check_update import check_updateService
from src.economicActivityAggregate.domain.entities.update_schedule import updateScheduleDB
from src.economicActivityAggregate.domain.entities.get_last_update_date import getLastUpdateDateDB
from src.economicActivityAggregate.indicators import indicators

def checkEconomicActivityUpdateUseCase():
  for indicator in indicators:
    db_name = indicator['db_name']

    # last_update_date = getLastUpdateDateDB(db_name)

    last_update_date = {
      'year': 2022,
      'month': 1
    }


    schedule = check_updateService(date=last_update_date, indicator=indicator)

    if schedule is not None:
      updateScheduleDB(schedule=schedule)

    else:
      print(f'No new {db_name} to update')

  return schedule
