from datetime import datetime
from src.moneyCirculation.domain.requiredFields.main import MoneyCirculation, Indicator
from src.moneyCirculation.services.utils.formatter import formatter
from src.moneyCirculation.services.utils.find.find_date import getNewDate

def moneyCirculationService(table: list, date: MoneyCirculation, indicator: Indicator):
    new_date = getNewDate(table, date, indicator)

    old_Date = datetime(date['year'], date['month'], 1)
    new_Date = datetime(new_date['year'], new_date['month'], 1)

    if new_Date <= old_Date:
        return None

    formatted = formatter(
        table=table,
        new_date=new_date,
        indicator=indicator
    )

    return formatted
