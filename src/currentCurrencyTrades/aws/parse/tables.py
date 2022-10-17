from trp import Document
from src.businessConfidenceAggregate.aws.parse.type_format import dataType

def tablesParser(textExtractResponse: dict):
  doc = Document(textExtractResponse)

  tables = []

  for page in doc.pages:
    for table in page.tables:
      new_table = []

      for r, row in enumerate(table.rows):
        new_row = []
        for c, cell in enumerate(row.cells):
          text = dataType(cell.text)
          new_row.append(text)

        new_table.append(new_row)
      tables.append(new_table)

  return tables