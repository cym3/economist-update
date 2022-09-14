from pathlib import Path
from datetime import datetime
from src.core.mail.sand_mail import sandMail
from src.utils.create_excel import createExcelFile
from src.utils.tasks import tasks_header

file_title = 'Atualização das taxas correntes de câmbio: Relatório da Ultima actividade'

def createError(massage: str):
    
    path = str(Path(__file__).parents[2].joinpath(f'assets/report.xlsx'))

    now = datetime.now()
    date = now.strftime('%Y-%m-%d %H:%M:%S')

    title = f'Exchange Rates could not be updated {date}'

    body = [
        ['T1', 'CurrentCurrencyTrades', 'Current exchange rates update', 'No', massage, date ]
    ]

    createExcelFile(body=body, title=file_title, header=tasks_header, path=path)
    
    sandMail(title=title, message=massage, attachmentPath=path)