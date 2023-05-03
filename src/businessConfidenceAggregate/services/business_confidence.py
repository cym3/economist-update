from src.utils.date.index import CreateDateUTC
from src.businessConfidenceAggregate.domain.requiredFields.business_confidence import Quarter, Indicator
from src.businessConfidenceAggregate.services.utils.formatter import formatter
from src.businessConfidenceAggregate.services.utils.find.main import findNewQuarter

def businessConfidenceService(table: list, quarter: Quarter, indicator: Indicator):
    
    table_data = findNewQuarter(table=table, indicator=indicator)

    table = table_data['table']
    new_quarter = table_data['new_quarter']

    last_date_on_db = CreateDateUTC(quarter['year'], quarter['toMonth'], 1).date
    last_date_on_table = CreateDateUTC(new_quarter['year'], new_quarter['toMonth'], 1).date

    if last_date_on_table <= last_date_on_db:
        return None

    formatted = formatter(
        table=table,
        new_quarter=new_quarter,
        indicator=indicator
    )

    return formatted
