from src.cpi.domain.requiredFields.cpi import DateCpi, Indicator
from src.cpi.services.utils.format_cpi import formatCpi
from src.cpi.services.utils.find.find_table import findTable
from src.cpi.services.fetch.fetch import fetchCpi

def cpiService(date: DateCpi, indicator: Indicator):    
    path = fetchCpi(date, indicator)

    if path is not None:

        table = findTable(path, indicator)

        formatted = formatCpi(table=table, date=date, indicator=indicator)

        return formatted

    return None
