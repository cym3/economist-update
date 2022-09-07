from src.cpi.domain.entities.create_tasks import createTaskDB
from src.cpi.domain.errors.create_error import createError
from src.cpi.services.utils.format_cpi import formatCpi
from src.cpi.services.utils.find.find_table import findTable
from src.cpi.services.fetch.fetch import fetchCpi
from datetime import datetime

async def cpiService():
    now = datetime.now()
    new_date = now.strftime('%Y-%m-%d %H:%M:%S')

    date = {
        'month': 2,
        'year': 2022
    }
    
    path = await fetchCpi(date)
    if path is None:
        return 'No new IPC to update'

    table = await findTable(path)

    formatted = await formatCpi(table)

    return formatted
