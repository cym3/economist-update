from fastapi import APIRouter
from src.eai.main import eaiUseCase
from src.eai.check_update import check_updateUseCase

economicActivityRouter = APIRouter(
    prefix='/economic-activity',
    tags=['Economic Activity']
)

@economicActivityRouter.get('/eai')
def controller():
  data = eaiUseCase()

  return data

@economicActivityRouter.get('/eai/schedule')
def controller():
  data = check_updateUseCase()

  return data
  