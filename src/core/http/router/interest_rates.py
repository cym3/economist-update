from fastapi import APIRouter
from src.interestRates.main import interestRatesUseCase

interestRatesRouter = APIRouter(
    prefix='/interest-rates',
    tags=['InterestRates']
)

@interestRatesRouter.get('')
def controller():
  data = interestRatesUseCase()

  return data
  
  
  
  