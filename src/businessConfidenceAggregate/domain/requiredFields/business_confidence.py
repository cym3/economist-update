from pydantic import BaseModel

class Quarter(BaseModel):
  year: int
  sign: str
  fromMonth: str
  toMonth: str

  class Indicator(BaseModel):
    name: str
    description: str
    page_identifiers: list[str]
    db_name: str
    jobCode: str