from fastapi import APIRouter
from src.businessConfidenceAggregate.main import economicActivityUseCase
from src.businessConfidenceAggregate.check_update import checkBusinessConfidenceAggregateUpdateUseCase

businessConfidenceRouter = APIRouter(
    prefix='/business-confidence',
    tags=['Business Confidence']
)

@businessConfidenceRouter.get('/aggregate')
def controller():
  data = economicActivityUseCase()

  return data

@businessConfidenceRouter.get('/aggregate/schedule')
def controller():
  data = checkBusinessConfidenceAggregateUpdateUseCase()

  return data
  