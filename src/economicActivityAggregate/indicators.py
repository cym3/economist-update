indicators = [
  {
    'name': 'Índices do Volume de Negócios',
    'page_title': 'Índices Agregados do Volume de Negócios, Variação Mensal dos Índices Agregados do Volume de Negócios',
    'sheet_name': 'Table 2',
    'db_name': 'turnover-index',
    'scheduleCode': '01-schedule'
  },
  {
    'name': 'Índices de Emprego',
    'page_title': 'Índices Agregados do Emprego, Variação Mensal dos Índices Agregados do Emprego',
    'sheet_name': 'Table 3',
    'db_name': 'employment-index',
    'scheduleCode': '02-schedule'
  },
  {
    'name': 'Índices de Remunerações',
    'page_title': 'Índices Agregados de Remunerações, Variação Mensal dos Índices Agregados de Remunerações',
    'sheet_name': 'Table 4',
    'db_name': 'income-index',
    'scheduleCode': '03-schedule'
  },
]

# scheduleCode - used to identify the schedule in database
# name - Name of the indicator, used to filter indicator data
# page_title - The title of the indicator on the pdf/excel file, It's used to validate the table data of the indicator
# sheet_name - name of the indicator sheet on the excel file