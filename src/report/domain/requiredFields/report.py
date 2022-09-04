from pydantic import BaseModel

class Report(BaseModel):
  taskCode: str
  name: str
  description: str
  isDone: bool
  error: str
  date: str
