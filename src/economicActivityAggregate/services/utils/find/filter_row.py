# Get only the first 12 list elements and make sure all numbers are numbers
import numpy as np
import re

def filter_row(row: list):
  new_row = []

  for el in row[-12:]:

    match = re.search(r'\d+', el)

    if match is not None:
      new_row.append(int(el))

    else:
      new_row.append(el)



  rr = np.array(new_row)

  print(rr)
  return new_row