from src.cpi.domain.requiredFields.cpi import DateCpi
from src.cpi.domain.entities.create_tasks import createTaskDB
from src.cpi.domain.errors.create_error import createError
from src.cpi.services.utils.format_cpi import formatCpi
from src.cpi.services.utils.find.find_table import findTable
from src.cpi.services.fetch.fetch import fetchCpi

async def cpiService(region: str, db_region: str, date: DateCpi):    
    fetch_result = await fetchCpi(date, region)

    if fetch_result is None:
        return 'No new IPC to update'

    path = fetch_result['path']
    date = fetch_result['date']

    table = await findTable(path, region)

    formatted = await formatCpi(table, db_region, date=date)

    return formatted
