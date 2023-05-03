from datetime import datetime


def createDateUTC(year: int = None, month: int = None, day: int = None):
  date = None

  if (year == None) or (month == None) or (day == None):
    date = datetime.now()
  else:
    date = datetime(year, month, day)

  dateFormatted = date.strftime('%Y-%m-%dT%H:%M:%SZ')

  return dateFormatted
