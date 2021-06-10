import  smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

email_from = 'brunooragnner@gmail.com'
email_password = os.getenv('EMAIL_PASSWORD')
email_smtp_server = 'smtp.gmail.com'

destination = 'brunooragnner@gmail.com'
subject = '''


sisitema automatico de massagem 
---------------------//--------------------------

confirmação de email

'''
msg = MIMEMultipart()
msg['From'] = email_from
msg['Subject'] = subject

text = 'equipe de desenvolvimento '
msg_text = MIMEText(text, 'html')
msg.attach(msg_text)
try:
    smtp = smtplib.SMTP(email_smtp_server, 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(email_from, email_password)
    smtp.sendmail(email_from, ','.join(destination), msg.as_string())
    smtp.quit()
    print('Email enviado com sucesso')
except Exception as err:
    print(f'Falha ao enviar e-mail:{err}')