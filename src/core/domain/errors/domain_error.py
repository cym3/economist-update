class DomainError(Exception):
    pass

class DatabaseFailError(DomainError):
  """Raised when database fails"""
  pass

class DataFetchError(DomainError):
  """Raised when data fetch fails or these's an error on the data fetched"""
  pass

