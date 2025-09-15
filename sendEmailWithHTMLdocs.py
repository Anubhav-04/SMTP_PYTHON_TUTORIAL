import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

def sendEmailTemplate(SMTP_SERVER,SMTP_PORT,FROM,PASSWORD,TO,SUBJECT,BODY):
    message = MIMEMultipart()
    message['FROM'] = FROM
    message['TO'] = TO
    message['SUBJECT'] = SUBJECT
    message['BODY'] = BODY

    message.attach(MIMEText(BODY,'plain'))
    emailTemplate = '/Users/assar/Desktop/todos-list/demo_folder/emailTemplate.html'
    with open(emailTemplate,'r') as f:
        html_content = f.read()
        message.attach(MIMEText(html_content,'html'))

    with smtplib.SMTP(SMTP_SERVER,SMTP_PORT) as server:
        server.starttls()
        server.login(FROM,PASSWORD)
        server.sendmail(FROM,TO,message.as_string())
        print("Email sent successfully")

SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = os.getenv('SMTP_PORT')
PASSWORD = os.getenv('SMTP_PASSWORD')
FROM = os.getenv('FROM')
TO = os.getenv('TO')
SUBJECT = "NEWSLETTER"
BODY = f"HELLO {TO} SUBSCRIBE OUR NEWSLETTER"

sendEmailTemplate(SMTP_SERVER,SMTP_PORT,FROM,PASSWORD,TO,SUBJECT,BODY)