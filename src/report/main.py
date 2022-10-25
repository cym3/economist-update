from datetime import datetime
from pathlib import Path
from src.core.mail.sand_mail import sandMail
from src.report.services.report import reportService
from src.report.domain.entities.get_tasks import getTasksDB
from src.utils.tasks import tasks_header
from src.utils.create_excel import createExcelFile

def reportUseCase():
    folder_path = Path(__file__).parent.joinpath('assets')
    folder_path.mkdir(parents=True, exist_ok=True)
    path = folder_path.joinpath('report.xlsx')
    documentPath = str(path)

    now = datetime.now()
    date = now.strftime('%Y-%m-%d %H:%M:%S')

    tasks = getTasksDB()
    tasksReport = reportService(tasks)

    title = f'Relatório das Ultimas 24 horas {date}'

    createExcelFile(body=tasksReport, title=title, header=tasks_header, path=documentPath)

    massage = f"""
        {date}

        Bom dia!
        Trago o relatório das atualizações do sistema nas últimas 24 horas.

        Desejo-lhe uma boa leitura.
        Até amanhã à mesma hora.
    """

    sandMail(title=title, message=massage, attachmentPath=documentPath)

    path.unlink()

    return tasksReport
