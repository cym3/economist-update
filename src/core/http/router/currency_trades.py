from fastapi import APIRouter
from src.currentCurrencyTrades.main import currentCurrencyTradesUseCase

currencyTradesRouter = APIRouter(
    prefix='/current-currency-trades',
    tags=['Currencies']
)

@currencyTradesRouter.get('')
def controller():
  data = currentCurrencyTradesUseCase()

  return data
  
  
  
  