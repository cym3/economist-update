from typing import Union
from src.cpi.domain.requiredFields.cpi import DateCpi
from src.currentCurrencyTrades.domain.entities.create_tasks import createTaskDB
from src.currentCurrencyTrades.domain.errors.create_error import createError
from src.cpi.services.utils.find.non_alcoholic_food import find_non_alcoholic_food
from src.cpi.services.utils.find.alcoholic_tobacco_and_narcotics import find_alcoholic_tobacco_and_narcotics
from src.cpi.services.utils.find.clothing_and_footwear import find_clothing_and_footwear
from src.cpi.services.utils.find.housing_water_electricity_gas_fuels import find_housing_water_electricity_gas_fuels
from src.cpi.services.utils.find.furniture_decoration_items_household_equipment import find_furniture_decoration_items_household_equipment
from src.cpi.services.utils.find.health import find_health
from src.cpi.services.utils.find.transport import find_transport
from src.cpi.services.utils.find.communications import find_communications
from src.cpi.services.utils.find.leisure_recreation_culture import find_leisure_recreation_culture
from src.cpi.services.utils.find.education import find_education
from src.cpi.services.utils.find.restaurants_hotels_cafes import find_restaurants_hotels_cafes
from src.cpi.services.utils.find.other_goods_and_services import find_other_goods_and_services

def formatCpi(table: list[list[Union[float, int]]], date: DateCpi):
  total = float(table[0][-1])
  
  non_alcoholic_food = find_non_alcoholic_food(table)

  alcoholic_tobacco_and_narcotics = find_alcoholic_tobacco_and_narcotics(table)

  clothing_and_footwear = find_clothing_and_footwear(table)

  housing_water_electricity_gas_fuels = find_housing_water_electricity_gas_fuels(table)

  furniture_decoration_items_household_equipment = find_furniture_decoration_items_household_equipment(table)

  health = find_health(table)

  transport = find_transport(table)

  communications = find_communications(table)

  leisure_recreation_culture = find_leisure_recreation_culture(table)

  education = find_education(table)

  restaurants_hotels_cafes = find_restaurants_hotels_cafes(table)
    
  other_goods_and_services = find_other_goods_and_services(table)

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
    'total': total,
    'date': date
  }