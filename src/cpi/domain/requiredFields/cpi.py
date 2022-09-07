from pydantic import BaseModel

class DateCpi(BaseModel):
  month: int
  year: int
