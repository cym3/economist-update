from pathlib import Path
from src.eai.domain.requiredFields.eai import DateEAI, Indicator
from src.eai.services.utils.format_eai import formatEAI
from src.eai.services.utils.find.table.main import findTable

def eaiService(date: DateEAI, indicator: Indicator):
    path = str(Path(__file__).parents[1].joinpath('assets/economist-activity.xlsx')) 

    table = findTable(path=path, indicator=indicator)
    return table

        # formatted = formatEAI(table, date=date)

        # return formatted
