from pprint import pprint
from src.creditByPurpose.services.utils.content.construction import constructionFormatter
from src.creditByPurpose.services.utils.content.electricity_gas_and_water import electricityGasAndWaterFormatter
from src.creditByPurpose.services.utils.content.extractive_industry import extractiveIndustryFormatter
from src.creditByPurpose.services.utils.content.fishery import fisheryFormatter
from src.creditByPurpose.services.utils.content.livestock import livestockFormatter
from src.creditByPurpose.services.utils.content.manufacturing_industry import manufacturingIndustryFormatter
from src.creditByPurpose.services.utils.content.monetary_and_financial_institutions import monetaryAndFinancialInstitutionsFormatter
from src.creditByPurpose.services.utils.content.other_sectores import otherSectoresFormatter
from src.creditByPurpose.services.utils.content.silviculture import silvicultureFormatter
from src.creditByPurpose.services.utils.content.total import totalFormatter
from src.creditByPurpose.services.utils.content.tourism import tourismFormatter
from src.creditByPurpose.services.utils.content.trades import tradesFormatter
from src.creditByPurpose.services.utils.content.transport_and_communication import transportAndCommunicationFormatter
from src.creditByPurpose.domain.requiredFields.credit import DateCredit
from src.creditByPurpose.services.utils.content.agriculture import agricultureFormatter

def formatter(
  table: list[list[float]],
  new_date: DateCredit
):
  agriculture = agricultureFormatter(table, new_date)
  construction = constructionFormatter(table, new_date)
  electricity_gas_and_water = electricityGasAndWaterFormatter(table, new_date)
  extractive_industry = extractiveIndustryFormatter(table, new_date)
  fishery = fisheryFormatter(table, new_date)
  livestock = livestockFormatter(table, new_date)
  manufacturing_industry = manufacturingIndustryFormatter(table, new_date)
  monetary_and_financial_institutions = monetaryAndFinancialInstitutionsFormatter(table, new_date)
  other_sectores = otherSectoresFormatter(table, new_date)
  silviculture = silvicultureFormatter(table, new_date)
  total = totalFormatter(table, new_date)
  tourism = tourismFormatter(table, new_date)
  trades = tradesFormatter(table, new_date)
  transport_and_communication = transportAndCommunicationFormatter(table, new_date)

  return [
    agriculture,
    construction,
    electricity_gas_and_water,
    extractive_industry,
    fishery,
    livestock,
    manufacturing_industry,
    monetary_and_financial_institutions,
    other_sectores,
    silviculture,
    total,
    tourism,
    trades,
    transport_and_communication
  ]