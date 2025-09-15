import smtplib
from email.mime.text import MIMEText

def send_email(subject,body):
    sender_email = "<sender email>"
    receiver_email = "<receiver email>"
    password = "<app password>"

    msg=MIMEText(body)
    msg['subject']=subject
    msg['body']=body
    msg['from']=sender_email
    msg['to']=receiver_email

    with smtplib.SMTP("smtp.gmail.com","587") as server:
        server.starttls()
        server.login(sender_email,password)
        server.send_message(msg)
        print("Message sent successfully")
        server.quit()

send_email("Backup Completed","Backup Created Successfully")