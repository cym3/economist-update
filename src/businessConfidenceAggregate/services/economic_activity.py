from src.businessConfidenceAggregate.domain.requiredFields.business_confidence import Quarter, Indicator
from src.businessConfidenceAggregate.services.utils.formatter import formatter
from src.businessConfidenceAggregate.services.utils.find.main import filterDates

def businessConfidenceService(table: list, quarter: Quarter, indicator: Indicator):
    
    table_data = filterDates(table=table, indicator=indicator)

    table = table_data['table']
    dates_row = table_data['dates_row']

    formatted = formatter(
        table=table,
        dates_row=dates_row,
        indicator=indicator,
        quarter=quarter
    )

    return formatted
