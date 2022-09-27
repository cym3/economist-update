from fastapi import APIRouter
from src.economicActivityAggregate.main import economicActivityUseCase
from src.economicActivityAggregate.check_update import checkEconomicActivityUpdateUseCase

economicActivityRouter = APIRouter(
    prefix='/economic-activity',
    tags=['Economic Activity']
)

@economicActivityRouter.get('/aggregate')
def controller():
  data = economicActivityUseCase()

  return data

@economicActivityRouter.get('/aggregate/schedule')
def controller():
  data = checkEconomicActivityUpdateUseCase()

  return data
  