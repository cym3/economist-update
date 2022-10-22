indicators = [
  {
    'name': 'Índices do Volume de Negócios',
    'description': 'Índices Agregados do Volume de Negócios, Variação Mensal dos Índices Agregados do Volume de Negócios',
    'page_number': 10,
    'page_identifiers': [
      'Quadro',
      '2.1:',
      'Índices Agregados do Volume de Negócios, Variação Mensal dos Índices Agregados do Volume de Negócios',
      'Base:',
      'Média Anual'
    ],
    'db_name': 'turnover-index',
    'jobCode': '01-economic-activity'
  },
  {
    'name': 'Índices de Emprego',
    'description': 'Índices Agregados do Emprego, Variação Mensal dos Índices Agregados do Emprego',
    'page_number': 11,
    'page_identifiers': [
      'Quadro',
      '2.2:',
      'Índices Agregados do Emprego, Variação Mensal dos Índices Agregados do Emprego',
      'Base:',
      'Média Anual'
    ],
    'db_name': 'employment-index',
    'jobCode': '02-economic-activity'
  },
  {
    'name': 'Índices de Remunerações',
    'description': 'Índices Agregados de Remunerações, Variação Mensal dos Índices Agregados de Remunerações',
    'page_number': 12,
    'page_identifiers': [
      'Quadro',
      '2.3:',
      'Índices Agregados de Remunerações, Variação Mensal dos Índices Agregados de Remunerações',
      'Base:',
      'Média Anual'
    ],
    'db_name': 'income-index',
    'jobCode': '03-economic-activity'
  },
]

# jobCode - used to identify the Job in database
# db_name - used to identify the indicator in database
# name - Name of the indicator, used to filter indicator data
# description - Indicator description
# page_identifiers - The identifies of the pdf page containing indicator table data, It's used to validate the pdf page containing table data.
