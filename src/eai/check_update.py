from src.eai.services.check_update import check_updateService
from src.eai.domain.entities.update_schedule import updateScheduleDB
from src.eai.domain.entities.get_last_update_date import getLastUpdateDateDB
from src.eai.indicator import indicator

def check_eai_updateUseCase():
  name = indicator['name']
  last_update_date = getLastUpdateDateDB()

  schedule = check_updateService(date=last_update_date, indicator=indicator)

  if schedule is not None:
    updateScheduleDB(schedule=schedule)

  else:
    print(f'No new {name} to update')

  return schedule
