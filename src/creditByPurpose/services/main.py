from datetime import datetime
from src.creditByPurpose.domain.requiredFields.credit import DateCredit, Indicator
from src.creditByPurpose.services.utils.formatter import formatter
from src.creditByPurpose.services.utils.find.find_date import getNewDate

def creditByPurposeService(table: list, date: DateCredit, indicator: Indicator):
    new_date = getNewDate(table, date, indicator)

    old_Date = datetime(date['year'], date['month'], 1)
    new_Date = datetime(new_date['year'], new_date['month'], 1)

    if new_Date <= old_Date:
        return None

    formatted = formatter(
        table=table,
        new_date=new_date
    )

    return formatted
