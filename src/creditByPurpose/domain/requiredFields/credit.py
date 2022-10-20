from pydantic import BaseModel

class DateCredit(BaseModel):
  month: int
  year: int

class Indicator(BaseModel):
  name: str
  page_identifiers: list[str]
  db_name: str
  scheduleCode: str

class Schedule(BaseModel):
  scheduleCode: str
  howToUpdate: str
  date: str