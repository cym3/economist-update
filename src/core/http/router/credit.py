from fastapi import APIRouter
from src.creditByPurpose.main import creditByPurposeUseCase
from src.creditByActivitySector.main import creditByActivitySectorUseCase

creditRouter = APIRouter(
    prefix='/credit',
    tags=['Credit']
)

@creditRouter.get('/by-purpose')
def controller():
  data = creditByPurposeUseCase()
  return data

@creditRouter.get('/by-sector')
def controller():
  data = creditByActivitySectorUseCase()

  return data
  