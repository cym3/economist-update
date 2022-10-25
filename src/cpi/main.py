from src.cpi.domain.entities.get_all import getAllDB
from src.cpi.domain.entities.get_update import updateCpiDB
from src.cpi.services.cpi import cpiService
from src.cpi.domain.entities.save_cpi import saveCpiDB
from src.cpi.domain.entities.get_last_update_date import getLastUpdateDateDB
from src.cpi.indicators import indicators

def cpiUseCase():
    for indicator in indicators:
        # last_update_date = getLastUpdateDateDB(indicator)
        CPIs = getAllDB(indicator)

        newCPIs = []
        for cpi in CPIs:
            values: list = cpi['values']

            cpi['values'] = values[:-1]

            newCPIs.append(cpi)

        updateCpiDB(newCPIs, indicator)

        # CPI = cpiService(date=last_update_date, indicator=indicator)

        # if CPI is not None:
        #     saveCpiDB(CPIs=CPI, indicator=indicator)
        #     print(CPI)

        # else:
        #     print('No new IPC to update')

    return 'Done'
