from src.eai.domain.requiredFields.eai import DateEAI
from src.eai.services.utils.format_eai import formatEAI
from src.eai.services.utils.find.find_table import findTable
from src.eai.services.fetch.fetch import fetchEAI

def eaiService(date: DateEAI):    
    fetch_result = fetchEAI(date)

    if fetch_result is not None:
        path = fetch_result['path']
        date = fetch_result['date']

        table = findTable(path)
        return table

        # formatted = formatEAI(table, date=date)

        # return formatted

    return None
