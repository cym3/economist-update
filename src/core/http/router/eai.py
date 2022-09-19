from fastapi import APIRouter
from src.eai.main import eaiUseCase

eaiRouter = APIRouter(
    prefix='/eai',
    tags=['EAI']
)

@eaiRouter.get('')
def controller():
  data = eaiUseCase()

  return data
  
  
  
  