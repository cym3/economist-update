from fastapi import APIRouter
from src.cpi.main import cpiUseCase

cpiRouter = APIRouter(
    prefix='/cpi',
    tags=['CPI']
)

@cpiRouter.get('')
async def controller():
  data = await cpiUseCase()

  return data
  
  
  
  