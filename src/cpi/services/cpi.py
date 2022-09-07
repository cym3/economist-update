from src.cpi.domain.requiredFields.cpi import DateCpi
from src.cpi.domain.entities.create_tasks import createTaskDB
from src.cpi.domain.errors.create_error import createError
from src.cpi.services.utils.format_cpi import formatCpi
from src.cpi.services.utils.find.find_table import findTable
from src.cpi.services.fetch.fetch import fetchCpi

async def cpiService(region: str, date: DateCpi):    
    path = await fetchCpi(date, region)
    if path is None:
        return 'No new IPC to update'

    table = await findTable(path, region)

    formatted = await formatCpi(table)

    return formatted
