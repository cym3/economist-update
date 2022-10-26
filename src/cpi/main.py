from src.cpi.services.cpi import cpiService
from src.cpi.domain.entities.save_cpi import saveCpiDB
from src.cpi.domain.entities.get_last_update_date import getLastUpdateDateDB
from src.cpi.indicators import indicators

def cpiUseCase():
    for indicator in indicators:
        db_name = indicator['db_name']
        last_update_date = getLastUpdateDateDB(indicator)

        CPI = cpiService(date=last_update_date, indicator=indicator)

        if CPI is not None:
            saveCpiDB(CPIs=CPI, indicator=indicator)
            print(CPI)

        else:
            print(f'No new {db_name} to update')

    return 'Done'
