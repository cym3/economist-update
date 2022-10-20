from datetime import datetime
from src.businessConfidenceBySector.domain.requiredFields.business_confidence import Quarter, Indicator
from src.businessConfidenceBySector.services.utils.formatter import formatter
from src.businessConfidenceBySector.services.utils.find.main import findNewQuarter

def businessConfidenceService(table: list, quarter: Quarter, indicator: Indicator):
    
    table_data = findNewQuarter(table=table, indicator=indicator)

    table = table_data['table']
    new_quarter = table_data['new_quarter']

    last_date_on_db = datetime(quarter['year'], quarter['toMonth'], 1)
    last_date_on_table = datetime(new_quarter['year'], new_quarter['toMonth'], 1)

    if last_date_on_table <= last_date_on_db:
        return None

    formatted = formatter(
        table=table,
        new_quarter=new_quarter,
        indicator=indicator
    )

    return formatted
