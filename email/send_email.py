import smtplib, ssl
from email.mime.text import MIMEText


#Email details
PORT_SMTP = 465
FROM = ''
FROM_PASS = ''
SUBJECT = ''
TO = ''
###################################


#Sending Email
def send_email(TO, text):
    context = ssl.create_default_context()
    message = f'Subject: {SUBJECT}\n\n'
    message = message + text

    with smtplib.SMTP_SSL("smtp.gmail.com", PORT_SMTP, context=context) as server:
        server.login(FROM, FROM_PASS)
        server.sendmail(FROM, TO, message)
        print(f"Email sent to {TO}")
