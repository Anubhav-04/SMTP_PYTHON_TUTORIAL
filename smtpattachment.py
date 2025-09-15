import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(subject, body,log_file_path):
  sender_email = "your email"
  receiver_email = "receiver email"
  password = "Your password"
  msg = MIMEMultipart(body)
  msg["subject"] = subject
  msg["from"] = sender_email
  msg["to"] = receiver_email

  msg.attach(MIMEText(body, 'plain'))

  with open('app.log', "rb") as attachment:
      part = MIMEBase("application", "octet-stream")
      part.set_payload(attachment.read())

  encoders.encode_base64(part)
  part.add_header(
      "Content-Disposition",
      f"attachment; filename={log_file_path.split('/')[-1]}",
  )

  msg.attach(part)

  try:
      server = smtplib.SMTP("smtp.gmail.com", 587)
      server.starttls() 
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, msg.as_string())
      print("Email sent successfully")
  except Exception as e:
     print(e)