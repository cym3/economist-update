from pydantic import BaseModel
from src.currentCurrencyTrades.domain.requiredFields.currencies import Indicator
from src.currentCurrencyTrades.domain.entities.create_tasks import createTaskDB
from src.currentCurrencyTrades.domain.errors.create_error import createError
from jsonschema import validate

class Rate(BaseModel):
  currency: str
  location: str
  name: str
  date: str
  buy: int
  sell: int

class ExchangeRates(BaseModel):
  baseCurrency: str
  location: str
  name: str
  type: str
  rates: list[Rate]

schema = {
    "type": "object",
    "properties": {
      "baseCurrency": {"type": "string"},
      "name": {"type": "string"},
      "location": {"type": "string"},
      "type": {"type": "string"},
      "rates": {
        "type": "array",
        "items": {
        "currency": "string",
        "location": "string",
        "name": "string",
        "date": "string",
        "buy": "number",
        "sell": "number"
      }
    }
  },
  "required": ["name", "baseCurrency", "location", "type", "rates"],
}

def dataValidator(data: ExchangeRates, indicator: Indicator):
  db_name = indicator['db_name']

  try: 
    validate(instance=data, schema=schema)
  
  except Exception as err:
    print(err)
    errorMessage = f'Invalid pdf page, the data contained by pdf dois not look like {db_name} data.'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return data