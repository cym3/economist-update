indicators = [
  {
    'name': 'Índices do Volume de Negócios',
    'page_identifiers': {
      'positives': [
        'Quadro',
        '2.1:',
        'Índices Agregados do Volume de Negócios, Variação Mensal dos Índices Agregados do Volume de Negócios',
        'Base:',
        'Média Anual'
      ],
      'negatives': ['ÍNDICE', 'METODOLOGIA DOS ÍNDICES DE ACTIVIDADES ECONÓMICAS']
    },
    'db_name': 'turnover-index',
    'scheduleCode': '01-schedule-economic-activity'
  },
  {
    'name': 'Índices de Emprego',
    'page_identifiers': {
      'positives': [
        'Quadro',
        '2.2:',
        'Índices Agregados do Emprego, Variação Mensal dos Índices Agregados do Emprego',
        'Base:',
        'Média Anual'
      ],
      'negatives': ['ÍNDICE', 'METODOLOGIA DOS ÍNDICES DE ACTIVIDADES ECONÓMICAS']
    },
    'db_name': 'employment-index',
    'scheduleCode': '02-schedule-economic-activity'
  },
  {
    'name': 'Índices de Remunerações',
    'page_identifiers': {
      'positives': [
        'Quadro',
        '2.3:',
        'Agregado',
        'Remunerações',
        'Base:',
        'Média Anual'
        ],
      'negatives': ['ÍNDICE', 'METODOLOGIA DOS ÍNDICES DE ACTIVIDADES ECONÓMICAS']
    },
    'db_name': 'income-index',
    'scheduleCode': '03-schedule-economic-activity'
  },
]

# scheduleCode - used to identify the schedule in database
# name - Name of the indicator, used to filter indicator data
# page_title - The title of the indicator on the pdf/excel file, It's used to validate the table data of the indicator
# sheet_name - name of the indicator sheet on the excel file