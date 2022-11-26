from pathlib import Path
from src.moneyPrinting.domain.requiredFields.main import MoneyPrinting, Indicator
from src.moneyPrinting.infra.fetch.fetch import fetchMoneyPrinting

def moneyPrintingInfra(date: MoneyPrinting, indicator: Indicator):   
  folder_path = Path(__file__).parents[1].joinpath('assets')
  folder_path.mkdir(parents=True, exist_ok=True)

   
  documentPath = fetchMoneyPrinting(date, folder_path, indicator)

  return documentPath