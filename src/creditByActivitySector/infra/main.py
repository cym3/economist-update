from pathlib import Path
from src.creditByActivitySector.domain.requiredFields.credit import DateCredit, Indicator
from src.creditByActivitySector.infra.fetch.fetch import fetchCreditByActivitySector

def creditByActivitySectorInfra(date: DateCredit, indicator: Indicator):   
  folder_path = Path(__file__).parents[1].joinpath('assets')
  folder_path.mkdir(parents=True, exist_ok=True)

   
  documentPath = fetchCreditByActivitySector(date, folder_path, indicator)

  return documentPath