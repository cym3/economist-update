from datetime import datetime
from dateutil.relativedelta import relativedelta
from src.moneyPrinting.services.utils.months import months
from src.moneyPrinting.domain.requiredFields.main import DateMoneyPrinting
from rapidfuzz.fuzz import partial_ratio

def isNewFile(date: DateMoneyPrinting, remote_name: str):
  old_Date = datetime(date['year'], date['month'], 1)
  new_Date = old_Date + relativedelta(months=+1)

  new_year = new_Date.year
  new_month = months[new_Date.month - 1]

  local_new_name = f'Estatísticas de Emissão Monetária - {new_month} {new_year}'

  match_score = partial_ratio(local_new_name.lower(), remote_name.lower())
  if (match_score > 97):
    return True

  return False
  

    