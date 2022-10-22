from pydantic import BaseModel

class DateEconomicActivity(BaseModel):
  month: int
  year: int

class Indicator(BaseModel):
  name: str
  page_title: str
  sheet_name: str
  db_name: str
  description: str
  page_identifiers: list[str]
  jobCode: str


class Schedule(BaseModel):
  scheduleCode: str
  howToUpdate: str
  date: str
