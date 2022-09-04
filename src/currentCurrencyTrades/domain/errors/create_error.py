from pathlib import Path
from datetime import datetime
from src.core.mail.sand_mail import sandMail

async def create_error(massage: str):
    path = str(Path(__file__).parents[2].joinpath(f'assets/report.xlsx'))

    now = datetime.now()
    date = now.strftime('%Y-%m-%d %H:%M:%S')

    title = f'Exchange Rates could not be updated {date}'

    await sandMail(title=title, message=massage, attachmentPath=path)

    print(f'{title}, {massage}')