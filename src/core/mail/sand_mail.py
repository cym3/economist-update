from email.mime.base import MIMEBase
from email import encoders
from os.path import basename
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import os
from typing import Union

mail_from = 'mozeconomia@gmail.com'
mail_to = 'arlindojosboa@gmail.com,mozeconomia@gmail.com,team@mozeconomia.co.mz'

def sandMail(title: str, message: str, attachmentPath: Union[str, None] = None):  
  mail_content = message
  
  password = os.getenv('EMAIL_HOST_PASSWORD')

  msg = MIMEMultipart()
  msg['Subject'] = title 
  msg['From'] = mail_from
  msg['To'] = mail_to
  msg.attach(MIMEText(mail_content, 'plain'))

  context = ssl.create_default_context()

  if (attachmentPath is not None):
    with open(attachmentPath, 'rb') as file:
      attachment =MIMEBase('application', 'octet-stream')

      attachment.set_payload(file.read())
      encoders.encode_base64(attachment)

      attachment.add_header('Content-Disposition','attachment; filename="{}"'.format(basename(attachmentPath)))

    msg.attach(attachment)

  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(mail_from, password)
    smtp.sendmail(mail_from, mail_to, msg.as_string())
