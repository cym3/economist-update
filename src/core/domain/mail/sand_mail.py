import smtplib
import os
from src.core.domain.errors.domain_error import EmailReportError

async def sandMail(title: str, message: str):
  EMAIL_HOST = os.getenv('EMAIL_HOST')
  EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
  EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
  EMAIL_PORT = os.getenv('EMAIL_PORT')

  sender = "Economist System updater <arlindoboa@mozeconomia.co.mz>"
  receiver = "System Support Team <team@mozeconomia.co.mz>"

  mail_message = f"""\
  Subject: {title}
  To: {receiver}
  From: {sender}

  {message}"""

  with smtplib.SMTP(EMAIL_HOST, int(EMAIL_PORT)) as server:
    try:
      server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
      server.sendmail(sender, receiver, mail_message)

    except Exception as err:
      raise EmailReportError(f'The Email was not sent ${err.args}')