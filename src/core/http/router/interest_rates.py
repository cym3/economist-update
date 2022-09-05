from fastapi import APIRouter
from src.interestRates.main import interestRatesUseCase

interestRatesRouter = APIRouter(
    prefix='/interest-rates',
    tags=['InterestRates']
)

@interestRatesRouter.get('')
async def controller():
  data = await interestRatesUseCase()

  return data
  
  
  
  