from src.cpi.domain.entities.create_tasks import createTaskDB
from src.cpi.domain.errors.create_error import createError
from src.cpi.services.utils.format_cpi import formatCpi
from src.cpi.services.utils.find_cpi import findCpi
from src.cpi.services.fetch.fetch import fetchCpi
from datetime import datetime

async def cpiService():
    now = datetime.now()
    new_date = now.strftime('%Y-%m-%d %H:%M:%S')

    date = {
        'month': 3,
        'year': 2022
    }
    
    path = await fetchCpi(date)

    table = await findCpi(path)

    # formatted = formatCpi()

    return table
