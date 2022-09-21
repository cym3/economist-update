from src.eai.services.check_update import check_updateService
from src.eai.domain.entities.schedule_update import updateScheduleDB
from src.eai.domain.entities.get_last_update_date import getLastUpdateDateDB
from src.eai.indicator import indicator

def check_updateUseCase():
  name = indicator['name']
  last_update_date = getLastUpdateDateDB()

  task = check_updateService(date=last_update_date, indicator=indicator)

  if task is not None:
    updateScheduleDB(task=task)

  else:
    name = indicator['name']
    print(f'No new {name} to update')

  return task
