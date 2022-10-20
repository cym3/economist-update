from src.creditByActivitySector.domain.requiredFields.page_validator import fileValidator
from src.creditByActivitySector.infra.main import businessConfidenceInfra
from src.creditByActivitySector.xlsx.read import readXlsx
from src.creditByActivitySector.xlsx.parser import parseXlsx
from src.creditByActivitySector.services.business_confidence import businessConfidenceService
from src.creditByActivitySector.domain.entities.save_economic_activity import saveBusinessConfidenceDB
from src.creditByActivitySector.domain.entities.get_last_update_date import getLastUpdateDateDB
from src.creditByActivitySector.indicators import indicators


def creditByActivitySectorUseCase():
    businessConfidence = []
    
    for indicator in indicators:
        db_name = indicator['db_name']

        last_update_date_on_db = getLastUpdateDateDB(db_name)

        file_path = businessConfidenceInfra(quarter=last_update_date_on_db, indicator=indicator)

        if file_path:
            response = readXlsx(documentPath=file_path)

            is_valid_page = fileValidator(response, indicator)

            if is_valid_page:
                tables = parseXlsx(response)

                businessConfidence = businessConfidenceService(
                    table=tables[0],
                    quarter=last_update_date_on_db,
                    indicator=indicator
                )

                saveBusinessConfidenceDB(businessConfidence=businessConfidence, db_name=db_name)
                print(db_name)

        else:
            print(f'No new {db_name} to update')

    return businessConfidence
