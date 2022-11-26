from pathlib import Path
from src.moneyCirculation.domain.requiredFields.main import MoneyCirculation, Indicator
from src.moneyCirculation.infra.fetch.fetch import fetchMoneyCirculation

def moneyCirculationInfra(date: MoneyCirculation, indicator: Indicator):   
  folder_path = Path(__file__).parents[1].joinpath('assets')
  folder_path.mkdir(parents=True, exist_ok=True)

   
  documentPath = fetchMoneyCirculation(date, folder_path, indicator)

  return documentPath