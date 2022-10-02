from fastapi import APIRouter
from src.businessConfidenceAggregate.main import businessConfidenceAggregateUseCase
from src.businessConfidenceBySector.main import businessConfidenceBySectorUseCase

businessConfidenceRouter = APIRouter(
    prefix='/business-confidence',
    tags=['Business Confidence']
)

@businessConfidenceRouter.get('/aggregate')
def controller():
  data = businessConfidenceAggregateUseCase()

@businessConfidenceRouter.get('/by-sector')
def controller():
  data = businessConfidenceBySectorUseCase()

  return data
  