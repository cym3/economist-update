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
mail_to = 'arlindojosboa@gmail.com'

async def sandMyMail(title: str, message: str): 
  title = 'Bom Dia Arlindo José Boa'
  mail_content = """
    Arlindo, você é o melhor. Por favor, continua fazendo o que você faz o Mundo agradece.

    Obrigado!


    -----------------------------------------------------


    Arlindo, you're the best. Please keep doing what you do, the World grateful.

    Thank you!
  """
  
  password = os.getenv('EMAIL_HOST_PASSWORD')

  msg = MIMEMultipart()
  msg['Subject'] = title 
  msg['From'] = mail_from
  msg['To'] = mail_to
  msg.attach(MIMEText(mail_content, 'plain'))

  context = ssl.create_default_context()

  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(mail_from, password)
    smtp.sendmail(mail_from, mail_to, msg.as_string())

