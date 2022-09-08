from calendar import month
from src.cpi.services.cpi import cpiService
from src.cpi.domain.entities.save_cpi import saveCpiDB
from src.cpi.domain.entities.get_last_update_date import getLastUpdateDateDB
from src.cpi.regions import regions
from datetime import datetime
from dateutil.relativedelta import relativedelta

async def cpiUseCase():
    
    for region in regions:
        db_region_id = region['db_id']
        web_region_id = region['web_id']

        last_update_date = await getLastUpdateDateDB(db_region_id)

        CPI = await cpiService(region=web_region_id, date=last_update_date)

        if CPI is not None:
            print(CPI)

            # await saveCpiDB(CPI)

    return 'Done'
