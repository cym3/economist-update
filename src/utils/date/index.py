from datetime import datetime

class CreateDateUTC:
  def __init__(self, year: int = None, month: int = None, day: int = None):
      date = None

      if (year == None) or (month == None) or (day == None):
        date = datetime.now()
      else:
        date = datetime(year, month, day)

      self.date = date
      self.strftime = date.strftime('%Y-%m-%dT%H:%M:%SZ')