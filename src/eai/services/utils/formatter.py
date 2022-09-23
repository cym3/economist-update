from datetime import datetime
from src.eai.domain.requiredFields.eai import DateEAI
from src.eai.services.utils.content.industry import industry_formatter

def formatter(
  table: list[list[float]],
  dates_row: list[datetime],
  date: DateEAI
):
  last_date_on_db = datetime(date['year'], date['month'], 1)
  last_date_on_excel = dates_row[-1]

  if last_date_on_excel <= last_date_on_db:
    return None

  industry_formatted = industry_formatter(table, dates_row, last_date_on_db)
  
  return [
    industry_formatted
  ]