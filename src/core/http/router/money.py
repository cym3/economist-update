from fastapi import APIRouter
from src.moneyPrinting.main import moneyPrintingUseCase
from src.moneyCirculation.main import moneyCirculationUseCase

MoneyRouter = APIRouter(
    prefix='/money',
    tags=['Money']
)

@MoneyRouter.get('/circulation')
def controller():
  data = moneyCirculationUseCase()

  return data

@MoneyRouter.get('/printing')
def controller():
  data = moneyPrintingUseCase()

  return data
  
  
  
  