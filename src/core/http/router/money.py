from fastapi import APIRouter
from src.moneyCirculation.main import moneyCirculationUseCase

MoneyRouter = APIRouter(
    prefix='/money',
    tags=['Money']
)

@MoneyRouter.get('/circulation')
def controller():
  data = moneyCirculationUseCase()

  return data
  
  
  
  