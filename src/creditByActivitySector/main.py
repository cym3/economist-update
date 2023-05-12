from src.creditByActivitySector.infra.main import creditByActivitySectorInfra
from src.creditByActivitySector.xlsx.read import readXlsx
from src.creditByActivitySector.xlsx.parser import parseXlsx
from src.creditByActivitySector.services.main import creditByActivitySectorService
from src.creditByActivitySector.domain.entities.save_credit import saveCreditByActivitySectorDB
from src.creditByActivitySector.domain.entities.get_last_update_date import getLastUpdateDateDB
from src.creditByActivitySector.indicators import indicators

def creditByActivitySectorUseCase():
    credit = []
    
    for indicator in indicators:
        db_name = indicator['db_name']

        old_date = getLastUpdateDateDB(indicator)

        path = creditByActivitySectorInfra(date=old_date, indicator=indicator)

        if path:
            response = readXlsx(path=path, indicator=indicator)
            # path.unlink()

            creditTable = parseXlsx(response)

            print(creditTable)

            credit = creditByActivitySectorService(
                table=creditTable,
                date=old_date,
                indicator=indicator
            )

            saveCreditByActivitySectorDB(
                creditByActivitySector=credit,
                indicator=indicator
            )
            print(db_name)

        else:
            print(f'No new {db_name} to update')

    return credit
