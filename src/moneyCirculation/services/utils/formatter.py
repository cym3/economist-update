from datetime import datetime
from src.moneyCirculation.domain.requiredFields.main import Indicator
from src.moneyCirculation.services.utils.content.banknotes import banknotesFormatter
from src.moneyCirculation.services.utils.content.coins import coinsFormatter
from src.moneyCirculation.domain.requiredFields.main import DateMoneyCirculation, Indicator


def formatter(
  table: list[list[float]],
  new_date: DateMoneyCirculation,
  indicator: Indicator
):
  banknotes = banknotesFormatter(table, new_date, indicator)
  coins = coinsFormatter(table, new_date, indicator)

  return [
    banknotes,
    coins
  ]