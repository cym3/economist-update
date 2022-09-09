from fastapi import APIRouter
from src.currentCurrencyTrades.main import currentCurrencyTradesUseCase

currencyTradesRouter = APIRouter(
    prefix='/currency-trades',
    tags=['Currencies']
)

@currencyTradesRouter.get('/current-trades')
async def controller():
  data = await currentCurrencyTradesUseCase()

  return data
  
  
  
  