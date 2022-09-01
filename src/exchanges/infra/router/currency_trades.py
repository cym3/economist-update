from fastapi import APIRouter
from src.exchanges.useCases.currencyTrades.current_trades import currentTradesUseCase

currencyTradesRouter = APIRouter(
    prefix='/currency-trades',
    tags=['Currencies']
)

@currencyTradesRouter.get('/current-trades')
async def controller():
  data = await currentTradesUseCase()

  return data
  
  
  
  