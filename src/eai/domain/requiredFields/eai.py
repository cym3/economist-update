from pydantic import BaseModel

class DateEAI(BaseModel):
  month: int
  year: int


class Indicator(BaseModel):
  title: str
  page_number: int