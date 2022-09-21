from pydantic import BaseModel

class DateEAI(BaseModel):
  month: int
  year: int


class Indicator(BaseModel):
  id: str
  name: str
  page_title: str
  page_number: int


class Schedule(BaseModel):
  id: str
  howToUpdate: str
  date: str
