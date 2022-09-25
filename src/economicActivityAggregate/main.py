from src.economicActivityAggregate.services.economic_activity import economicActivityService
from src.economicActivityAggregate.domain.entities.save_economic_activity import saveEconomicActivityDB
from src.economicActivityAggregate.domain.entities.get_last_update_date import getLastUpdateDateDB
from src.economicActivityAggregate.indicators import indicators

def economicActivityUseCase():
    economicActivity = []
    
    for indicator in indicators:
        db_name = indicator['db_name']

        last_update_date = getLastUpdateDateDB(db_name)

        economicActivities = economicActivityService(date=last_update_date, indicator=indicator)

        if economicActivity is not None:
            saveEconomicActivityDB(economicActivities=economicActivities, db_name=db_name)
            print(db_name)

        else:
            print('No new IPC to update')

    return economicActivity
