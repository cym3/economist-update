from src.cpi.domain.requiredFields.cpi import DateCpi, Indicator
from src.cpi.services.utils.format_cpi import formatCpi
from src.cpi.services.utils.find.find_table import findTable
from src.cpi.services.fetch.fetch import fetchCpi

def cpiService(date: DateCpi, indicator: Indicator):    
    fetch_result = fetchCpi(date, indicator)

    if fetch_result is not None:
        path = fetch_result['path']
        date = fetch_result['date']

        table = findTable(path, indicator)

        formatted = formatCpi(table, date=date)

        return formatted

    return None
