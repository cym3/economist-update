from fastapi import APIRouter
from src.currentCryptoTrades.main import currentCryptoTradesUseCase

cryptoTradesRouter = APIRouter(
    prefix='/trades',
    tags=['Crypto']
)

@cryptoTradesRouter.get('/current-crypto')
def controller():
  data = currentCryptoTradesUseCase()

  return data
  
  
  
  