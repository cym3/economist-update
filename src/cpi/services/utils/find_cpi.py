from msilib.schema import tables
import re
import pandas as pd

async def findCpi(path: str):
  tables = pd.read_excel(path)

  table = tables.values.tolist()

  return table