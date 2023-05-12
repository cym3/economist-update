from pathlib import Path
from src.creditByActivitySector.domain.requiredFields.credit import DateCredit, Indicator
from src.creditByActivitySector.infra.fetch.fetch import fetchCreditByActivitySector

def creditByActivitySectorInfra(date: DateCredit, indicator: Indicator):   
  documentPath = Path(__file__).parents[1].joinpath('assets/crédito-por-finalidade-março-2023.xlsx')
  # folder_path.mkdir(parents=True, exist_ok=True)

  # documentPath = fetchCreditByActivitySector(date, folder_path, indicator)

  return documentPath