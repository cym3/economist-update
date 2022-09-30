from fastapi import APIRouter
from src.economicActivityAggregate.main import economicActivityAggregateUseCase

economicActivityRouter = APIRouter(
    prefix='/economic-activity',
    tags=['Economic Activity']
)

@economicActivityRouter.get('/aggregate')
def controller():
  data = economicActivityAggregateUseCase()

  return data
