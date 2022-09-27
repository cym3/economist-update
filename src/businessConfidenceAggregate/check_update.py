from src.businessConfidenceAggregate.services.check_update import check_updateService
from src.businessConfidenceAggregate.domain.entities.update_schedule import updateScheduleDB
from src.businessConfidenceAggregate.domain.entities.get_last_update_date import getLastUpdateDateDB
from src.businessConfidenceAggregate.indicator import indicator

def checkBusinessConfidenceAggregateUpdateUseCase():
  db_name = indicator['db_name']

  last_update_quarter = getLastUpdateDateDB(db_name)

  schedule = check_updateService(quarter=last_update_quarter, indicator=indicator)

  if schedule is not None:
    updateScheduleDB(schedule=schedule)

  else:
    print(f'No new {db_name} to update')

  return schedule
