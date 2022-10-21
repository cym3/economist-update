from datetime import datetime
from src.creditByPurpose.domain.requiredFields.credit import DateCredit, Indicator
from src.creditByPurpose.services.utils.formatter import formatter
from src.creditByPurpose.services.utils.find.find_date import getNewDate

def creditByPurposeService(table: list, date: DateCredit, indicator: Indicator):
    new_date = getNewDate(table, date, indicator)

    last_date_on_db = datetime(date['year'], date['month'], 1)
    last_date_on_table = datetime(new_date['year'], new_date['month'], 1)

    if last_date_on_table <= last_date_on_db:
        return None

    formatted = formatter(
        table=table,
        new_date=new_date
    )

    return formatted
