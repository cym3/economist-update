from pathlib import Path
from src.creditByActivitySector.domain.requiredFields.credit import DateCredit
from src.creditByActivitySector.infra.fetch.fetch import fetchCreditByActivitySector

def creditByActivitySectorInfra(date: DateCredit):   
  folder_path = Path(__file__).parents[1].joinpath('assets')
   
  documentPath = fetchCreditByActivitySector(date, folder_path)

  return documentPath