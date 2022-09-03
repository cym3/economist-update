from fastapi import APIRouter
from src.currentCurrencyTrades.main import currentTradesUseCase

currencyTradesRouter = APIRouter(
    prefix='/currency-trades',
    tags=['Currencies']
)

@currencyTradesRouter.get('/current-trades')
async def controller():
  data = await currentTradesUseCase()

  return data
  
  
  
  