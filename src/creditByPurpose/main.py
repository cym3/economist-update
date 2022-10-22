from src.creditByPurpose.infra.main import creditByPurposeInfra
from src.creditByPurpose.xlsx.read import readXlsx
from src.creditByPurpose.xlsx.parser import parseXlsx
from src.creditByPurpose.services.main import creditByPurposeService
from src.creditByPurpose.domain.entities.save_credit import saveCreditByPurposeDB
from src.creditByPurpose.domain.entities.get_last_update_date import getLastUpdateDateDB
from src.creditByPurpose.indicators import indicators

def creditByPurposeUseCase():
    credit = []
    
    for indicator in indicators:
        db_name = indicator['db_name']

        old_date = getLastUpdateDateDB(db_name, indicator)

        documentPath = creditByPurposeInfra(date=old_date, indicator=indicator)
        
        if documentPath:
            response = readXlsx(documentPath=documentPath, indicator=indicator)

            creditTable = parseXlsx(response)

            credit = creditByPurposeService(
                table=creditTable,
                date=old_date,
                indicator=indicator
            )

            saveCreditByPurposeDB(
                creditByPurpose=credit,
                db_name=db_name,
                indicator=indicator
            )
            print(db_name)

        else:
            print(f'No new {db_name} to update')

    return credit
