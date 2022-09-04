class DomainError(Exception):
    pass

class DatabaseFailError(DomainError):
  """Raised when database fails"""
  pass

class EmailReportError(DomainError):
  """Raised when the email report fails"""
  pass

