from src.businessConfidenceAggregate.domain.requiredFields.business_confidence import Indicator, Quarter
from src.businessConfidenceAggregate.services.utils.content.economic_climate import economicClimateFormatter
from src.businessConfidenceAggregate.services.utils.content.employment_expectations import employmentExpectationsFormatter
from src.businessConfidenceAggregate.services.utils.content.current_employment import currentEmploymentFormatter
from src.businessConfidenceAggregate.services.utils.content.demand_expectations import demandExpectationsFormatter
from src.businessConfidenceAggregate.services.utils.content.price_expectations import priceExpectationsFormatter

def formatter(
  table: list[list[float]],
  new_quarter: Quarter,
  indicator: Indicator
):
  economic_climate = economicClimateFormatter(table, new_quarter, indicator)
  employment_expectations = employmentExpectationsFormatter(table, new_quarter, indicator)
  current_employment = currentEmploymentFormatter(table, new_quarter, indicator)
  demand_expectations = demandExpectationsFormatter(table, new_quarter, indicator)
  price_expectations = priceExpectationsFormatter(table, new_quarter, indicator)

  return [
    economic_climate,
    employment_expectations,
    current_employment,
    demand_expectations,
    price_expectations
  ]