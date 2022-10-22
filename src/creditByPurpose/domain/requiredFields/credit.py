from pydantic import BaseModel

class DateCredit(BaseModel):
  month: int
  year: int

class Indicator(BaseModel):
  name: str
  description: str
  page_identifiers: list[str]
  db_name: str
  jobCode: str