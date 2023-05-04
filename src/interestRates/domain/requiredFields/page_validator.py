from pydantic import BaseModel
from src.currentCurrencyTrades.domain.requiredFields.currencies import Indicator
from src.currentCurrencyTrades.domain.entities.create_tasks import createTaskDB
from src.currentCurrencyTrades.domain.errors.create_error import createError
from jsonschema import validate

class Rate(BaseModel):
  name: str
  value: str

class InterestRates(BaseModel):
  currency: str
  name: str
  location: str
  rates: list[Rate]

schema = {
    "type": "object",
    "properties": {
      "currency": {"type": "string"},
      "name": {"type": "string"},
      "location": {"type": "string"},
      "values": {"type": "array"},
      "rates": {
        "type": "array",
        "items": {
        "name": "string",
        "value": "string",
      }
    }
  },
  "required": ["name", "currency", "location", "rates"],
}

def dataValidator(data: InterestRates, indicator: Indicator):
  db_name = indicator['db_name']

  try: 
    validate(instance=data, schema=schema)
  
  except Exception as err:
    print(err)
    errorMessage = f'{db_name}: invalid data.'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)