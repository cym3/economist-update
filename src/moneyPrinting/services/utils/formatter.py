from datetime import datetime
from src.moneyPrinting.domain.requiredFields.main import Indicator
from src.moneyPrinting.services.utils.content.banknotes import banknotesFormatter
from src.moneyPrinting.services.utils.content.coins import coinsFormatter
from src.moneyPrinting.domain.requiredFields.main import DateMoneyPrinting, Indicator


def formatter(
  table: list[list[float]],
  new_date: DateMoneyPrinting,
  indicator: Indicator
):
  banknotes = banknotesFormatter(table, new_date, indicator)
  coins = coinsFormatter(table, new_date, indicator)

  return [
    banknotes,
    coins
  ]