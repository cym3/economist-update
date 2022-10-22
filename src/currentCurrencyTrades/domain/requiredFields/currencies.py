from pydantic import BaseModel
from typing import Union

class Trade(BaseModel):
  buy: float
  sale: float
  date: str

class ISO(BaseModel):
  code: str
  number: float

class UnitsFrequency(BaseModel):
  name: str
  symbol: str
  majorValue: Union[str, None]

class Banknotes(BaseModel):
  frequent: list[str]
  rare: list[str]

class Coins(BaseModel):
  frequent: list[str]
  rare: list[str]

class Units(BaseModel):
  major: UnitsFrequency
  minor: UnitsFrequency

class Currency(BaseModel):
  country: str
  flag: str
  name: str
  iso: ISO
  units: Units
  banknotes: Banknotes
  coins: Coins
  currentTrades: Trade
  dailyTrades: list[Trade]

class Indicator(BaseModel):
  name: str
  description: str
  page_identifiers: list[str]
  db_name: str
  jobCode: str