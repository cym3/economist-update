from src.economicActivityAggregate.domain.requiredFields.economic_activity import DateEconomicActivity, Indicator
from src.economicActivityAggregate.services.utils.formatter import formatter
from src.economicActivityAggregate.services.utils.find.main import filterDates

def economicActivityService(table: list, date: DateEconomicActivity, indicator: Indicator):
    
    table_data = filterDates(table=table, indicator=indicator)

    table = table_data['table']
    dates_row = table_data['dates_row']

    formatted = formatter(
        table=table,
        dates_row=dates_row,
        indicator=indicator,
        date=date
    )

    return formatted
