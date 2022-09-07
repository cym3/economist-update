from typing import Union
import re

def find_communications(table: list[list[Union[float, int]]]):
  def find():
    for row in table:
      el = str(row[1]).lower()

      match1 = re.search('comunicações', el)

      if match1 is not None:

        values = []
        year = 2019
        month = 11

        index = 0
        for col in row:

          if index >= 4:
            values.append({
              "date": {
                "year": year,
                "month": month
              },
              "value": float(col)
            })

            if month == 12:
              month = 1
              year += 1
            else:
              month += 1

          index += 1

        return values
  
  values = find()

  return {
    "id": 7,
    "name": "Comunicações",
    "values": values
  }