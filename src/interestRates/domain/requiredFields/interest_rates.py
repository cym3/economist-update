from pydantic import BaseModel

class Indicator(BaseModel):
  name: str
  description: str
  page_identifiers: list[str]
  db_name: str
  jobCode: str