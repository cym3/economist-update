from fastapi import APIRouter, HTTPException, status
from src.exchanges.useCases.currencyTrades.current_trates import currentTradesUseCase

currencyTradesRouter = APIRouter(
    prefix='/currency-trades',
    tags=['Currencies']
)

@currencyTradesRouter.get('/current-trades')
async def controller():
  data = await currentTradesUseCase()

  return data
  
  
  
  