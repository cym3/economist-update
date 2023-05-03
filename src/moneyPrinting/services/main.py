from src.utils.date.index import CreateDateUTC
from src.moneyPrinting.domain.requiredFields.main import DateMoneyPrinting, Indicator
from src.moneyPrinting.services.utils.formatter import formatter
from src.moneyPrinting.services.utils.find.find_date import getNewDate

def moneyPrintingService(table: list, date: DateMoneyPrinting, indicator: Indicator):
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
