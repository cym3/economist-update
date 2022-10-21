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

        # last_update_date_on_db = getLastUpdateDateDB(db_name)

        last_update_date_on_db = { 'year': 2022, 'month': 6 }

        file_path = creditByPurposeInfra(date=last_update_date_on_db, indicator=indicator)
        
        if file_path:
            response = readXlsx(documentPath=file_path)

            creditTable = parseXlsx(response)

            credit = creditByPurposeService(
                table=creditTable,
                date=last_update_date_on_db,
                indicator=indicator
            )

            saveCreditByPurposeDB(creditByPurpose=credit, db_name=db_name)
            print(db_name)

        else:
            print(f'No new {db_name} to update')

    return credit
