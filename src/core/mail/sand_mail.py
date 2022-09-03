import smtplib
import email.message
import os
from typing import Union
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

async def sandMail(title: str, message: str, attachments: Union[list[str], None]=None):  
  mail_content = f"""
  <p>{message}</p>
  """
  msg = email.message.Message()
  msg['Subject'] = title
  msg['From'] = 'mozeconomia@gmail.com'
  msg['To'] = 'arlindojosboa@gmail.com,mozeconomia@gmail.com,team@mozeconomia.co.mz'
  msg.add_header('Content-Type', 'text/html')
  msg.set_payload(mail_content)

  password = os.getenv('EMAIL_HOST_PASSWORD')

  s = smtplib.SMTP('smtp.gmail.com: 587')
  s.starttls()
  s.login(msg['From'], password)
  s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
