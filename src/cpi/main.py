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

        last_date_in_DB = await getLastUpdateDateDB(db_region_id)

        print(region)
        print(last_date_in_DB)
         
        year = last_date_in_DB['year']
        month = last_date_in_DB['month']

        new_date = datetime(year, month, 1) + relativedelta(months=1)

        date = {
            'year': new_date.year,
            'month': new_date.month
        }

        CPI = await cpiService(region=web_region_id, date=date)

        if CPI is not None:
            print(CPI)

            # await saveCpiDB(CPI)

    return 'Done'
