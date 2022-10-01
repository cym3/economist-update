from datetime import datetime
from src.businessConfidenceAggregate.domain.requiredFields.business_confidence import Quarter, Indicator
from src.businessConfidenceAggregate.services.utils.content.industry import industryFormatter
from src.businessConfidenceAggregate.services.utils.content.transport import transportFormatter
from src.businessConfidenceAggregate.services.utils.content.accommodations_restaurants import accommodationsRestaurantsFormatter
from src.businessConfidenceAggregate.services.utils.content.energy_water_and_san import energyWaterAndSanFormatter
from src.businessConfidenceAggregate.services.utils.content.main_index import mainIndexFormatter
from src.businessConfidenceAggregate.services.utils.content.other_services import otherServicesFormatter
from src.businessConfidenceAggregate.services.utils.content.trade import tradeFormatter

def formatter(
  table: list[list[float]],
  dates_row: list[datetime],
  quarter: Quarter,
  indicator: Indicator
):
  last_date_on_db = datetime(quarter['year'], quarter['toMonth'], 1)
  last_date_on_table = dates_row[-1]

  if last_date_on_table <= last_date_on_db:
    return None

  industry = industryFormatter(table, dates_row, last_date_on_db)
  transport = transportFormatter(table, dates_row, last_date_on_db)
  accommodations_restaurants = accommodationsRestaurantsFormatter(table, dates_row, last_date_on_db)
  energy_water_and_san = energyWaterAndSanFormatter(table, dates_row, last_date_on_db)
  other_services = otherServicesFormatter(table, dates_row, last_date_on_db)
  trade = tradeFormatter(table, dates_row, last_date_on_db)

  indices_of_business = mainIndexFormatter(table, dates_row, last_date_on_db, indicator)
  
  return [
    indices_of_business,
    industry,
    energy_water_and_san,
    trade,
    transport,
    accommodations_restaurants,
    other_services,
  ]