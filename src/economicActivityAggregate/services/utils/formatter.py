from datetime import datetime
from src.utils.date.index import CreateDateUTC
from src.economicActivityAggregate.domain.requiredFields.economic_activity import DateEconomicActivity, Indicator
from src.economicActivityAggregate.services.utils.content.industry import industryFormatter
from src.economicActivityAggregate.services.utils.content.transport import transportFormatter
from src.economicActivityAggregate.services.utils.content.accommodations_restaurants import accommodationsRestaurantsFormatter
from src.economicActivityAggregate.services.utils.content.energy_water_and_san import energyWaterAndSanFormatter
from src.economicActivityAggregate.services.utils.content.main_index import mainIndexFormatter
from src.economicActivityAggregate.services.utils.content.other_services import otherServicesFormatter
from src.economicActivityAggregate.services.utils.content.trade import tradeFormatter

def formatter(
  table: list[list[float]],
  dates_row: list[datetime],
  date: DateEconomicActivity,
  indicator: Indicator
):
  last_date_on_db = CreateDateUTC(date['year'], date['month'], 1).date
  last_date_on_table = dates_row[-1]

  if last_date_on_table <= last_date_on_db:
    return None

  industry = industryFormatter(table, dates_row, last_date_on_db, indicator)
  transport = transportFormatter(table, dates_row, last_date_on_db, indicator)
  accommodations_restaurants = accommodationsRestaurantsFormatter(table, dates_row, last_date_on_db, indicator)
  energy_water_and_san = energyWaterAndSanFormatter(table, dates_row, last_date_on_db, indicator)
  other_services = otherServicesFormatter(table, dates_row, last_date_on_db, indicator)
  trade = tradeFormatter(table, dates_row, last_date_on_db, indicator)

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