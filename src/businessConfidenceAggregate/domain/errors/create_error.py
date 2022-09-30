from pathlib import Path
from datetime import datetime
from src.core.mail.sand_mail import sandMail
from src.utils.create_excel import createExcelFile
from src.utils.tasks import tasks_header

file_title = 'Atualização dos Indicadores de Confiança e de Clima Económico: Relatório da Ultima actividade'

def createError(massage: str):
    
    path = str(Path(__file__).parents[2].joinpath(f'assets/report.xlsx'))

    now = datetime.now()
    date = now.strftime('%Y-%m-%d %H:%M:%S')

    title = f'Aggregate Business Confidence could not be updated {date}'

    body = [
        ['04-job', 'Aggregate Business Confidence', 'Aggregate Business Confidence update', 'No', massage, now ]
    ]

    createExcelFile(body=body, title=file_title, header=tasks_header, path=path)
    
    sandMail(title=title, message=massage, attachmentPath=path)