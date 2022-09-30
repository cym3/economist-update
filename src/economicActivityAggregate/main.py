import re
from src.economicActivityAggregate.domain.requiredFields.page_validator import fileValidator
from src.economicActivityAggregate.aws.extract.tables import extractTable
from src.economicActivityAggregate.infra.main import economicActivityInfra
from src.economicActivityAggregate.aws.parse.tables import tablesParser
from src.economicActivityAggregate.services.economic_activity import economicActivityService
from src.economicActivityAggregate.domain.entities.save_economic_activity import saveEconomicActivityDB
from src.economicActivityAggregate.domain.entities.get_last_update_date import getLastUpdateDateDB
from src.economicActivityAggregate.indicators import indicators


def economicActivityUseCase():
    economicActivity = []
    
    for indicator in indicators:
        db_name = indicator['db_name']

        last_update_date_on_db = getLastUpdateDateDB(db_name)

        file_path = economicActivityInfra(date=last_update_date_on_db, indicator=indicator)

        if file_path:
            response = extractTable(documentPath=file_path)

            is_valid_page = fileValidator(response, indicator)

            if is_valid_page:
                tables = tablesParser(response)

                economicActivity = economicActivityService(
                    table=tables[0],
                    date=last_update_date_on_db,
                    indicator=indicator
                )

                # saveEconomicActivityDB(economicActivities=economicActivity, db_name=db_name)
                print(db_name)

        else:
            print(f'No new {db_name} to update')

    return economicActivity
