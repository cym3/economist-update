from pathlib import Path
from src.eai.domain.requiredFields.eai import DateEAI, Indicator
from src.eai.services.utils.formatter import formatter
from src.eai.services.utils.find.main import findTable

def eaiService(date: DateEAI, indicator: Indicator):
    path = str(Path(__file__).parents[1].joinpath('assets/economic-activity.xlsx')) 

    table_data = findTable(path=path, indicator=indicator)

    table = table_data['table']
    dates_row = table_data['dates_row']

    formatted = formatter(
        table=table,
        dates_row=dates_row,
        date=date
    )

    return formatted
