from pathlib import Path
from datetime import datetime
from src.core.mail.sand_mail import sandMail
from src.utils.create_excel import createExcelFile
from src.utils.tasks import tasks_header

file_title = 'Atualização dos indices de preços: Relatório da Ultima actividade'

async def createError(massage: str):
    
    path = str(Path(__file__).parents[2].joinpath(f'assets/report.xlsx'))

    now = datetime.now()
    date = now.strftime('%Y-%m-%d %H:%M:%S')

    title = f'Consumer Price Index could not be updated {date}'

    body = [
        ['T1', 'IPC', 'Consumer Price Index update', 'No', massage, date ]
    ]

    await createExcelFile(body=body, title=file_title, header=tasks_header, path=path)
    
    await sandMail(title=title, message=massage, attachmentPath=path)