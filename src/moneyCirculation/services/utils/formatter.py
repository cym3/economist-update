from src.creditByActivitySector.services.utils.content.construction import constructionFormatter
from src.creditByActivitySector.services.utils.content.industry import extractiveIndustryFormatter
from src.creditByActivitySector.services.utils.content.other_sectores import otherSectoresFormatter
from src.creditByActivitySector.services.utils.content.total import totalFormatter
from src.creditByActivitySector.services.utils.content.tourism import tourismFormatter
from src.creditByActivitySector.services.utils.content.trades import tradesFormatter
from src.creditByActivitySector.services.utils.content.transport_and_communication import transportAndCommunicationFormatter
from src.creditByActivitySector.domain.requiredFields.credit import DateCredit, Indicator
from src.creditByActivitySector.services.utils.content.agriculture import agricultureFormatter

def formatter(
  table: list[list[float]],
  new_date: DateCredit,
  indicator: Indicator
):
  agriculture = agricultureFormatter(table, new_date, indicator)
  construction = constructionFormatter(table, new_date, indicator)
  industry = extractiveIndustryFormatter(table, new_date, indicator)
  other_sectores = otherSectoresFormatter(table, new_date, indicator)
  total = totalFormatter(table, new_date, indicator)
  tourism = tourismFormatter(table, new_date, indicator)
  trades = tradesFormatter(table, new_date, indicator)
  transport_and_communication = transportAndCommunicationFormatter(table, new_date, indicator)

  return [
    agriculture,
    construction,
    industry,
    other_sectores,
    total,
    tourism,
    trades,
    transport_and_communication
  ]