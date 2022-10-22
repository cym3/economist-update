from src.businessConfidenceBySector.domain.requiredFields.page_validator import fileValidator
from src.businessConfidenceBySector.aws.extract.tables import extractTable
from src.businessConfidenceBySector.infra.main import businessConfidenceInfra
from src.businessConfidenceBySector.aws.parse.tables import tablesParser
from src.businessConfidenceBySector.services.business_confidence import businessConfidenceService
from src.businessConfidenceBySector.domain.entities.save_economic_activity import saveBusinessConfidenceDB
from src.businessConfidenceBySector.domain.entities.get_last_update_date import getLastUpdateDateDB
from src.businessConfidenceBySector.indicators import indicators


def businessConfidenceBySectorUseCase():
    businessConfidence = []
    
    for indicator in indicators:
        db_name = indicator['db_name']

        last_update_date_on_db = getLastUpdateDateDB(indicator)

        file_path = businessConfidenceInfra(quarter=last_update_date_on_db, indicator=indicator)

        if file_path:
            response = extractTable(documentPath=file_path, indicator=indicator)

            is_valid_page = fileValidator(response, indicator)

            if is_valid_page:
                tables = tablesParser(response)

                businessConfidence = businessConfidenceService(
                    table=tables[0],
                    quarter=last_update_date_on_db,
                    indicator=indicator
                )

                saveBusinessConfidenceDB(
                    businessConfidence=businessConfidence,
                    db_name=db_name,
                    indicator=indicator
                )
                print(db_name)

        else:
            print(f'No new {db_name} to update')

    return businessConfidence
