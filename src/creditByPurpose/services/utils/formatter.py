from src.businessConfidenceBySector.domain.requiredFields.business_confidence import Indicator, Quarter
from src.businessConfidenceBySector.services.utils.content.services import servicesFormatter
from src.businessConfidenceBySector.services.utils.content.industrial_production import industrialProductionFormatter
from src.businessConfidenceBySector.services.utils.content.trades import tradesFormatter

def formatter(
  table: list[list[float]],
  new_quarter: Quarter,
  indicator: Indicator
):
  industrial_production = industrialProductionFormatter(table, new_quarter, indicator)
  services =  servicesFormatter(table, new_quarter, indicator)
  trades = tradesFormatter(table, new_quarter, indicator)

  return [
    industrial_production,
    services,
    trades
  ]