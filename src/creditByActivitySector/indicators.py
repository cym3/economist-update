indicators = [
  {
    'name': 'Crédito por Sector de Actividade',
    'page_identifiers': ['CRÉDITO TOTAL POR SECTORES DE ACTIVIDADE ECONÓMICA - SALDOS'],
    'db_name': 'credit-by-activity-sector',
    'scheduleCode': '01-credit-by-activity-sector'
  }
]

# scheduleCode - used to identify the schedule in database
# name - Name of the indicator, used to filter indicator data
# page_identifiers - The identifies of the pdf page containing indicator table data, It's used to validate the pdf page containing table data.
# page_number - number of the pdf page containing indicator table data
# column_index - index of the column containing data in the table  