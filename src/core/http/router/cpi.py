from fastapi import APIRouter
from src.save import saveUseCase
from src.cpi.main import cpiUseCase

cpiRouter = APIRouter(
    prefix='/cpi',
    tags=['CPI']
)

@cpiRouter.get('')
def controller():
  data = cpiUseCase()

  return data

@cpiRouter.get('/save')
def controller():
  data = saveUseCase()

  return data
  
  
  
  