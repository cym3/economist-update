from pydantic import BaseModel

class Quarter(BaseModel):
  year: int
  sign: str
  fromMonth: str
  toMonth: str

class Indicator(BaseModel):
  name: str
  page_identities: str
  db_name: int
  scheduleCode: str

class Schedule(BaseModel):
  scheduleCode: str
  howToUpdate: str
  date: str