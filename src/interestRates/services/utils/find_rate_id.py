def findRateId(rateName: str):
  id = None

  if rateName.lower() == 'Taxa Mimo'.lower():
    id = '6306d5b6181a74367f812bd5'
  if rateName.lower() == 'FPC'.lower():
    id = '6306d5b6181a74367f812bd4'
  if rateName.lower() == 'FPD'.lower():
    id = '6306d5b6181a74367f812bd3'
  if rateName.lower() == 'Prime Rate'.lower():
    id = '6306d5b6181a74367f812bd6'
  
  return id