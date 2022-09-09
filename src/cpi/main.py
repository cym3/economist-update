from src.cpi.services.cpi import cpiService
from src.cpi.domain.entities.save_cpi import saveCpiDB
from src.cpi.domain.entities.get_last_update_date import getLastUpdateDateDB
from src.cpi.regions import regions

def cpiUseCase():
    
    for region in regions:
        db_region_id = region['db_id']
        web_region_id = region['web_id']

        last_update_date = getLastUpdateDateDB(db_region_id)

        CPI = cpiService(region=web_region_id, date=last_update_date)

        if CPI is not None:
            saveCpiDB(CPIs=CPI, region=db_region_id)
            print(CPI)

        else:
            print('No new IPC to update')

    return 'Done'
