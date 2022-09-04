from pathlib import Path
from datetime import datetime
from src.core.mail.sand_mail import sandMail
from src.utils.create_excel import createExcelFile

file_title = 'Atualização das taxas correntes de câmbio: Relatório da Ultima actividade'
file_header = ['Task Code', 'Name', 'description', 'Is Done', 'error', 'date']

async def createError(massage: str):
    
    path = str(Path(__file__).parents[2].joinpath(f'assets/report.xlsx'))

    now = datetime.now()
    date = now.strftime('%Y-%m-%d %H:%M:%S')

    title = f'Exchange Rates could not be updated {date}'

    body = [
        ['T1', 'CurrentCurrencyTrades', 'Update of current exchange rates', 'No', massage, date ]
    ]

    await createExcelFile(body=body, title=file_title, header=file_header, path=path)
    
    await sandMail(title=title, message=massage, attachmentPath=path)

    print(f'{title}, {massage}')