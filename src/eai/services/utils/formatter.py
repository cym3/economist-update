from datetime import datetime
from src.eai.domain.requiredFields.eai import DateEAI
from src.eai.services.utils.content.industry import industry_formatter

def formatter(
  table: list[list[float]],
  dates_row: list[datetime],
  date: DateEAI
):
  return table

  # industry_formatted = industry_formatter(sheet=)
  
  # return [
  #   industry_formatted
  # ]