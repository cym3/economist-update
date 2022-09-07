from typing import Union
import re

def find_clothing_and_footwear(table: list[list[Union[float, int]]]):
  def find():
    for row in table:
      el = str(row[1]).lower()
      match1 = re.search('vestuário', el)
      match2 = re.search('calçado', el)

      if (match1 is not None) and (match2 is not None):

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
    "id": 2,
    "name": "Vestuários e Calçados",
    "values": values
  }