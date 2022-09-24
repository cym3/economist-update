from pathlib import Path
from src.economicActivityAggregate.domain.requiredFields.economic_activity import DateEconomicActivity, Indicator
from src.economicActivityAggregate.services.utils.formatter import formatter
from src.economicActivityAggregate.services.utils.find.main import findTable

def economicActivityService(date: DateEconomicActivity, indicator: Indicator):
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
