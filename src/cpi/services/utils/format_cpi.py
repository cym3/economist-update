from typing import Union
from src.cpi.services.utils.find.date_row_formatter import datesRowFormatter
from src.cpi.services.utils.find.find_date_row import findDateRow
from src.cpi.domain.requiredFields.cpi import DateCpi, Indicator
from src.cpi.services.utils.content.non_alcoholic_food import find_non_alcoholic_food
from src.cpi.services.utils.content.alcoholic_tobacco_and_narcotics import find_alcoholic_tobacco_and_narcotics
from src.cpi.services.utils.content.clothing_and_footwear import find_clothing_and_footwear
from src.cpi.services.utils.content.housing_water_electricity_gas_fuels import find_housing_water_electricity_gas_fuels
from src.cpi.services.utils.content.furniture_decoration_items_household_equipment import find_furniture_decoration_items_household_equipment
from src.cpi.services.utils.content.health import find_health
from src.cpi.services.utils.content.transport import find_transport
from src.cpi.services.utils.content.total import findTotal
from src.cpi.services.utils.content.communications import find_communications
from src.cpi.services.utils.content.leisure_recreation_culture import find_leisure_recreation_culture
from src.cpi.services.utils.content.education import find_education
from src.cpi.services.utils.content.restaurants_hotels_cafes import find_restaurants_hotels_cafes
from src.cpi.services.utils.content.other_goods_and_services import find_other_goods_and_services

def formatCpi(table: list[list[Union[float, int]]], date: DateCpi, indicator: Indicator):
  dates_row = findDateRow(table, indicator)
  dates_row = datesRowFormatter(dates_row, date, indicator)

  total = findTotal(table, dates_row, date)
  
  non_alcoholic_food = find_non_alcoholic_food(table, dates_row, date)

  alcoholic_tobacco_and_narcotics = find_alcoholic_tobacco_and_narcotics(table, dates_row, date)

  clothing_and_footwear = find_clothing_and_footwear(table, dates_row, date)

  housing_water_electricity_gas_fuels = find_housing_water_electricity_gas_fuels(table, dates_row, date)

  furniture_decoration_items_household_equipment = find_furniture_decoration_items_household_equipment(table, dates_row, date)

  health = find_health(table, dates_row, date)

  transport = find_transport(table, dates_row, date)

  communications = find_communications(table, dates_row, date)

  leisure_recreation_culture = find_leisure_recreation_culture(table, dates_row, date)

  education = find_education(table, dates_row, date)

  restaurants_hotels_cafes = find_restaurants_hotels_cafes(table, dates_row, date)
    
  other_goods_and_services = find_other_goods_and_services(table, dates_row, date)

  return {
    'products': [
      non_alcoholic_food,
      alcoholic_tobacco_and_narcotics,
      clothing_and_footwear,
      housing_water_electricity_gas_fuels,
      furniture_decoration_items_household_equipment,
      health,
      transport,
      communications,
      leisure_recreation_culture,
      education,
      restaurants_hotels_cafes,
      other_goods_and_services
    ],
    'total': total
  }