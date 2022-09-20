from src.eai.services.eai import eaiService
from src.eai.domain.entities.save_cpi import saveCpiDB
from src.eai.domain.entities.get_last_update_date import getLastUpdateDateDB
from src.eai.indicator import indicator

def eaiUseCase():
    
    # for region in regions:
    #     db_region_id = region['db_id']
    #     web_region_id = region['web_id']

    # last_update_date = getLastUpdateDateDB()

    last_update_date = {
        'month': 1,
        'year': 2022
    }

    eai = eaiService(date=last_update_date, indicator=indicator)

        # if CPI is not None:
        #     saveCpiDB(CPIs=CPI, region=db_region_id)
        #     print(CPI)

        # else:
        #     print('No new IPC to update')

    return eai
