import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
import re
from datetime import datetime
from email.mime.base import MIMEBase
from email import encoders
load_dotenv()

def check_log_and_send_email(log_file,error_pattern,SMTP_SERVER,SMTP_PORT,SMTP_USERNAME,SMTP_PASSWORD,FROM,TO):
    '''
    Checks the logfile for error and sends the email
    '''
    try:
        with open(log_file,'r') as f:
            log_content = f.read()
        if re.search(error_pattern,log_content,re.MULTILINE):
            subject = "Critical error detected in log"
            body = f"Error : {error_pattern} found in Log File : {log_file} at {datetime.now()}"

            msg = MIMEMultipart()
            msg['FROM'] = FROM
            msg['TO'] = TO
            msg['SUBJECT'] = subject
            msg['BODY'] = body
            msg.attach(MIMEText(body,'plain'))

            with open(log_file, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

                encoders.encode_base64(part)
                part.add_header(
                        "Content-Disposition",
                  f"attachment; filename={log_file.split('/')[-1]}",
                )

            msg.attach(part)

            with smtplib.SMTP(SMTP_SERVER,SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USERNAME,SMTP_PASSWORD)
                server.sendmail(FROM,TO,msg.as_string())
            print('Email Sent Successfuly')
        else:
            print("No Error Detected")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)
LOG_FILE = os.getenv('LOG_FILE')
ERROR_PATTERN = r'.* - (ERROR|CRITICAL) - *'
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = os.getenv('SMTP_PORT')
SMTP_USERNAME = os.getenv('SMTP_USERNAME')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
FROM = os.getenv('FROM')
TO = os.getenv('TO')
check_log_and_send_email(LOG_FILE,ERROR_PATTERN,SMTP_SERVER,SMTP_PORT,SMTP_USERNAME,SMTP_PASSWORD,FROM,TO)