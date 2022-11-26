from pydantic import BaseModel

class DateMoneyPrinting(BaseModel):
  month: int
  year: int


class Value(BaseModel):
  date: DateMoneyPrinting
  value: int

class MoneyPrinting(BaseModel):
  id: str
  name: str
  volumes: list[Value]
  values: list[Value]

class Indicator(BaseModel):
  name: str
  description: str
  page_identifiers: list[str]
  db_name: str
  jobCode: str