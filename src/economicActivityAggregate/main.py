from src.economicActivityAggregate.services.economic_activity import economicActivityService
from src.economicActivityAggregate.domain.entities.save_cpi import saveCpiDB
from src.economicActivityAggregate.domain.entities.get_last_update_date import getLastUpdateDateDB
from src.economicActivityAggregate.indicators import indicators

def economicActivityUseCase():
    economicActivity = []
    
    for indicator in indicators:
        db_name = indicator['db_name']

        last_update_date = getLastUpdateDateDB(db_name)

        economicActivity = economicActivityService(date=last_update_date, indicator=indicator)

            # if CPI is not None:
            #     saveCpiDB(CPIs=CPI, region=db_region_id)
            #     print(CPI)

            # else:
            #     print('No new IPC to update')

    return economicActivity
