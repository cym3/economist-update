from fastapi import APIRouter
from src.cpi.main import cpiUseCase

cpiRouter = APIRouter(
    prefix='/cpi',
    tags=['CPI']
)

@cpiRouter.get('')
def controller():
  data = cpiUseCase()

  return data
  
  
  
  