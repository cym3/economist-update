from src.moneyPrinting.infra.main import moneyPrintingInfra
from src.moneyPrinting.xlsx.read import readXlsx
from src.moneyPrinting.xlsx.parser import parseXlsx
from src.moneyPrinting.services.main import moneyPrintingService
from src.moneyPrinting.domain.entities.save import saveMoneyPrintingDB
from src.moneyPrinting.domain.entities.get_last_update_date import getLastUpdateDateDB
from src.moneyPrinting.indicators import indicators

def moneyPrintingUseCase():
    money = []
    
    for indicator in indicators:
        db_name = indicator['db_name']

        # old_date = getLastUpdateDateDB(indicator)
        old_date = { 'year': 2022, 'month': 9 }

        path = moneyPrintingInfra(date=old_date, indicator=indicator)

        if path:
            response = readXlsx(path=path, indicator=indicator)
            path.unlink()

            moneyTable = parseXlsx(response)

            money = moneyPrintingService(
                table=moneyTable,
                date=old_date,
                indicator=indicator
            )

            saveMoneyPrintingDB(
                moneyPrinting=money,
                indicator=indicator
            )
            print(db_name)

        else:
            print(f'No new {db_name} to update')

    return money
