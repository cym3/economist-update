indicator = {
  'name': 'Indicadores de Confiança e de Clima Económico',
  'page_identifiers': {
    'positives': ['3.ANEXOS', '3.1. Resumo Estatístico dos Indicadores'],
    'negatives': ['Índice do cont', 'INTRODUÇÃO']
  },
  'db_name': 'business-confidence-aggregate',
  'scheduleCode': '01-schedule-business-confidence'
}

# scheduleCode - used to identify the schedule in database
# name - Name of the indicator, used to filter indicator data
# page_identifiers - The identifies of the page indicator on the pdf file, It's used to validate the table data. Positives - the page should contain and Negatives should not contain.
# sheet_name - name of the indicator sheet on the excel file