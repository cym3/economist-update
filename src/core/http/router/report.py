from fastapi import APIRouter
from src.report.main import reportUseCase

reportRouter = APIRouter(
    prefix='/report',
    tags=['Report']
)

@reportRouter.get('')
def controller():
  data = reportUseCase()

  return data
  
  
  
  