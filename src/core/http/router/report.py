from fastapi import APIRouter
from src.report.main import reportUseCase

reportRouter = APIRouter(
    prefix='',
    tags=['Report']
)

@reportRouter.get('/report')
async def controller():
  data = await reportUseCase()

  return data
  
  
  
  