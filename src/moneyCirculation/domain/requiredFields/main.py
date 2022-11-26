from pydantic import BaseModel

class DateMoneyCirculation(BaseModel):
  month: int
  year: int


class Value(BaseModel):
  date: DateMoneyCirculation
  value: int

class MoneyCirculation(BaseModel):
  _id: str
  name: str
  volumes: list[Value]
  values: list[Value]

class Indicator(BaseModel):
  name: str
  description: str
  page_identifiers: list[str]
  db_name: str
  jobCode: str