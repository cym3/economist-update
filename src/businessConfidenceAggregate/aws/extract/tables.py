import boto3
from economicActivityAggregate.domain.requiredFields.economic_activity import Indicator
from src.businessConfidenceAggregate.domain.entities.create_tasks import createTaskDB
from src.businessConfidenceAggregate.domain.errors.create_error import createError

def extractTable(documentPath: str, indicator: Indicator):
  response = None

  try:
    # Amazon Textract client
    client = boto3.client('textract')

    # Call Amazon Textract
    with open(documentPath, 'rb') as document:
      response = client.analyze_document(
        Document={
          'Bytes': document.read(),
        },
        FeatureTypes=['TABLES']
      )

  except Exception as err:
    print(err)
    errorMessage = f'AWS Textract failed to extract {documentPath} document table.'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage)

  return response
