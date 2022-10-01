from fastapi import APIRouter
from src.businessConfidenceAggregate.main import businessConfidenceAggregateUseCase

businessConfidenceRouter = APIRouter(
    prefix='/business-confidence',
    tags=['Business Confidence']
)

@businessConfidenceRouter.get('/aggregate')
def controller():
  data = businessConfidenceAggregateUseCase()

  return data
  