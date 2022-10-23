from pathlib import Path
from datetime import datetime
from src.businessConfidenceAggregate.domain.requiredFields.business_confidence import Indicator
from src.core.mail.sand_mail import sandMail
from src.utils.create_excel import createExcelFile
from src.utils.tasks import tasks_header

def createError(massage: str, indicator: Indicator):
    name = indicator['name']
    jobCode = indicator['jobCode']
    description = indicator['description']
    title = f'Atualização {name}: Relatório da Ultima actividade'
    
    path = Path(__file__).parents[2].joinpath(f'assets/report.xlsx')
    documentPath = str(path)

    now = datetime.now()
    date = now.strftime('%Y-%m-%d %H:%M:%S')


    body = [
        [jobCode, name, description, 'No', massage, date ]
    ]

    createExcelFile(body=body, title=title, header=tasks_header, path=documentPath)
    
    sandMail(title=title, message=massage, attachmentPath=path)

    path.unlink()