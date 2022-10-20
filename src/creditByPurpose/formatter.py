
def getCreditByPurposeLine(creditByPurposes: list[int]):
  year = 2005
  month = 1
  formatted = []

  circulIndex = 1 
  investmentIndex = 2
  totalIndex = 3

  while year != 2022 or month != 9:

    if month >= 13:
      year += 1
      month = 1

    formatted.append({
      'date': {
        'year': year,
        'month': month
      },
      'circul': creditByPurposes[circulIndex],
      'investment': creditByPurposes[investmentIndex],
      'total': creditByPurposes[totalIndex]
    })

    circulIndex += 3 
    investmentIndex += 3
    totalIndex += 3

    month += 1

  return formatted

def creditByPurposeFormatter(creditByPurposeLines):
  creditByPurposeLine4 = creditByPurposeLines['creditByPurposeLine4']
  creditByPurposeLine12 = creditByPurposeLines['creditByPurposeLine12']
  creditByPurposeLine13 = creditByPurposeLines['creditByPurposeLine13']
  creditByPurposeLine14 = creditByPurposeLines['creditByPurposeLine14']
  creditByPurposeLine15 = creditByPurposeLines['creditByPurposeLine15']
  creditByPurposeLine18 = creditByPurposeLines['creditByPurposeLine18']
  creditByPurposeLine24 = creditByPurposeLines['creditByPurposeLine24']
  creditByPurposeLine25 = creditByPurposeLines['creditByPurposeLine25']
  creditByPurposeLine26 = creditByPurposeLines['creditByPurposeLine26']
  creditByPurposeLine27 = creditByPurposeLines['creditByPurposeLine27']
  creditByPurposeLine28 = creditByPurposeLines['creditByPurposeLine28']
  creditByPurposeLine33 = creditByPurposeLines['creditByPurposeLine33']
  creditByPurposeLine34 = creditByPurposeLines['creditByPurposeLine34']
  creditByPurposeLine38 = creditByPurposeLines['creditByPurposeLine38']

  return [
    {
      'name': 'AGRICULTURA',
      'type': 'Por Sector de Atividades',
      'values': getCreditByPurposeLine(creditByPurposeLine4)
    },
    {
      'name': 'PECUÁRIA',
      'type': 'Por Sector de Atividades',
      'values': getCreditByPurposeLine(creditByPurposeLine12)
    },
    {
      'name': 'SILVICULT.E EXPL. FLORESTAL',
      'type': 'Por Sector de Atividades',
      'values': getCreditByPurposeLine(creditByPurposeLine13)
    },
    {
      'name': 'PESCAS',
      'type': 'Por Sector de Atividades',
      'values': getCreditByPurposeLine(creditByPurposeLine14)
    },
    {
      'name': 'INDUSTRIA EXTRACTIVA',
      'type': 'Por Sector de Atividades',
      'values': getCreditByPurposeLine(creditByPurposeLine15)
    },
    {
      'name': 'INDÚSTRIAS TRANSFORMAD.',
      'type': 'Por Sector de Atividades',
      'values': getCreditByPurposeLine(creditByPurposeLine18)
    },
    {
      'name': 'ELECTRICIDADE GÁS E AGUA',
      'type': 'Por Sector de Atividades',
      'values': getCreditByPurposeLine(creditByPurposeLine24)
    },
    {
      'name': 'CONSTRUÇÃO E OBRAS PÚBLICAS',
      'type': 'Por Sector de Atividades',
      'values': getCreditByPurposeLine(creditByPurposeLine25)
    },
    {
      'name': 'INDÚSTRIA  DE TURISMO',
      'type': 'Por Sector de Atividades',
      'values': getCreditByPurposeLine(creditByPurposeLine26)
    },
    {
      'name': 'COMÉRCIO',
      'type': 'Por Sector de Atividades',
      'values': getCreditByPurposeLine(creditByPurposeLine27)
    },
    {
      'name': 'TRANSPORTES E COMUNICAÇÕES',
      'type': 'Por Sector de Atividades',
      'values': getCreditByPurposeLine(creditByPurposeLine28)
    },
    {
      'name': 'INST. FINANC.N/ MONETÁRIAS',
      'type': 'Por Sector de Atividades',
      'values': getCreditByPurposeLine(creditByPurposeLine33)
    },
    {
      'name': 'OUTROS SECTORES',
      'type': 'Por Sector de Atividades',
      'values': getCreditByPurposeLine(creditByPurposeLine34)
    },
    {
      'name': 'TOTAL',
      'type': 'Por Sector de Atividades',
      'values': getCreditByPurposeLine(creditByPurposeLine38)
    }
  ]
