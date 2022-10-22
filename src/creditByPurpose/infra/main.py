from pathlib import Path
from src.creditByPurpose.domain.requiredFields.credit import DateCredit, Indicator
from src.creditByPurpose.infra.fetch.fetch import fetchCreditByPurpose

def creditByPurposeInfra(date: DateCredit, indicator: Indicator):   
  folder_path = Path(__file__).parents[1].joinpath('assets')
   
  documentPath = fetchCreditByPurpose(date, folder_path, indicator)

  return documentPath