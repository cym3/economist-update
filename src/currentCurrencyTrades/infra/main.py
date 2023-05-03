from pathlib import Path
from src.currentCurrencyTrades.domain.requiredFields.currencies import Indicator
from src.currentCurrencyTrades.infra.fetch.fetch import fetchTrades

def tradesInfra(indicator: Indicator):   
  trades = fetchTrades(indicator)

  return trades
