from src.utils.date.index import CreateDateUTC
from src.creditByActivitySector.domain.requiredFields.credit import DateCredit, Indicator
from src.creditByActivitySector.services.utils.formatter import formatter
from src.creditByActivitySector.services.utils.find.find_date import getNewDate

def creditByActivitySectorService(table: list, date: DateCredit, indicator: Indicator):
    new_date = getNewDate(table, date, indicator)

    old_Date = CreateDateUTC(date['year'], date['month'], 1).date
    new_Date = CreateDateUTC(new_date['year'], new_date['month'], 1).date

    if new_Date <= old_Date:
        return None

    formatted = formatter(
        table=table,
        new_date=new_date,
        indicator=indicator
    )

    return formatted
