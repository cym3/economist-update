from pathlib import Path
from src.utils.date.index import CreateDateUTC
from src.interestRates.domain.requiredFields.interest_rates import Indicator
from src.core.mail.sand_mail import sandMail
from src.utils.create_excel import createExcelFile
from src.utils.tasks import tasks_header

def createError(massage: str, indicator: Indicator):
    name = indicator['name']
    jobCode = indicator['jobCode']
    description = indicator['description']
    title = f'Atualização {name}: Relatório da Ultima actividade'
    
    folder_path = Path(__file__).parents[2].joinpath('assets')
    folder_path.mkdir(parents=True, exist_ok=True)
    path = folder_path.joinpath('report.xlsx')
    documentPath = str(path)

    date = CreateDateUTC().strftime


    body = [
        [jobCode, name, description, 'No', massage, date ]
    ]

    createExcelFile(body=body, title=title, header=tasks_header, path=documentPath)
    
    sandMail(title=title, message=massage, attachmentPath=path)

    path.unlink()