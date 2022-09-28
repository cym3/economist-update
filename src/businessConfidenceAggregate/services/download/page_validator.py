import re
from src.businessConfidenceAggregate.domain.requiredFields.business_confidence import Indicator

def validator(text: str, indicator: Indicator):
  positives: list[str] = indicator['page_identifiers']['positives']
  negatives: list[str] = indicator['page_identifiers']['negatives']

  valide_page = True

  for identifier in positives:
    if re.search(identifier, text) is None:
      valide_page = False

  for identifier in negatives:
    if re.search(identifier, text) is not None:
      valide_page = False

  return valide_page