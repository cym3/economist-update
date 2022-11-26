from src.moneyCirculation.infra.main import moneyCirculationInfra
from src.moneyCirculation.xlsx.read import readXlsx
from src.moneyCirculation.xlsx.parser import parseXlsx
from src.moneyCirculation.services.main import moneyCirculationService
from src.moneyCirculation.domain.entities.save import saveMoneyCirculationDB
from src.moneyCirculation.domain.entities.get_last_update_date import getLastUpdateDateDB
from src.moneyCirculation.indicators import indicators

def moneyCirculationUseCase():
    credit = []
    
    for indicator in indicators:
        db_name = indicator['db_name']

        # old_date = getLastUpdateDateDB(indicator)

        old_date = {'year': 2022, 'month': 9}

        path = moneyCirculationInfra(date=old_date, indicator=indicator)

        if path:
            response = readXlsx(path=path, indicator=indicator)
            path.unlink()

            creditTable = parseXlsx(response)

            # credit = moneyCirculationService(
            #     table=creditTable,
            #     date=old_date,
            #     indicator=indicator
            # )

            # saveMoneyCirculationDB(
            #     moneyCirculation=credit,
            #     indicator=indicator
            # )
            # print(db_name)

        else:
            print(f'No new {db_name} to update')

    return credit
