indicators = [
  {
    'name': 'Índices do Volume de Negócios',
    'page_number': 10,
    'page_identifiers': [
      'Quadro',
      '2.1:',
      'Índices Agregados do Volume de Negócios, Variação Mensal dos Índices Agregados do Volume de Negócios',
      'Base:',
      'Média Anual'
    ],
    'db_name': 'turnover-index',
    'scheduleCode': '01-schedule-economic-activity'
  },
  # {
  #   'name': 'Índices de Emprego',
  #   'page_number': 11,
  #   'page_identifiers': [
  #     'Quadro',
  #     '2.2:',
  #     'Índices Agregados do Emprego, Variação Mensal dos Índices Agregados do Emprego',
  #     'Base:',
  #     'Média Anual'
  #   ],
  #   'db_name': 'employment-index',
  #   'scheduleCode': '02-schedule-economic-activity'
  # },
  # {
  #   'name': 'Índices de Remunerações',
  #   'page_number': 12,
  #   'page_identifiers': [
  #     'Quadro',
  #     '2.3:',
  #     'Índices Agregados de Remunerações, Variação Mensal dos Índices Agregados de Remunerações',
  #     'Base:',
  #     'Média Anual'
  #   ],
  #   'db_name': 'income-index',
  #   'scheduleCode': '03-schedule-economic-activity'
  # },
]

# scheduleCode - used to identify the schedule in database
# name - Name of the indicator, used to filter indicator data
# page_identifiers - The identifies of the pdf page containing indicator table data, It's used to validate the pdf page containing table data.
# page_number - number of the pdf page containing indicator table data