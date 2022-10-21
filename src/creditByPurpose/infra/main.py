from pathlib import Path
from src.creditByPurpose.domain.requiredFields.credit import DateCredit
from src.creditByPurpose.infra.fetch.fetch import fetchCreditByPurpose

def creditByPurposeInfra(date: DateCredit):   
  folder_path = Path(__file__).parents[1].joinpath('assets')
   
  documentPath = fetchCreditByPurpose(date, folder_path)

  return documentPath