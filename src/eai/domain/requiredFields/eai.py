from pydantic import BaseModel

class DateEAI(BaseModel):
  month: int
  year: int
