from fastapi import APIRouter
from src.currentCurrencyTrades.main import currentCurrencyTradesUseCase

currencyTradesRouter = APIRouter(
    prefix='/trades',
    tags=['Currencies']
)

@currencyTradesRouter.get('/current-currency')
def controller():
  data = currentCurrencyTradesUseCase()

  return data
  
  
  
  