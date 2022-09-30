from fastapi import APIRouter
from src.economicActivityAggregate.main import economicActivityUseCase

economicActivityRouter = APIRouter(
    prefix='/economic-activity',
    tags=['Economic Activity']
)

@economicActivityRouter.get('/aggregate')
def controller():
  data = economicActivityUseCase()

  return data
