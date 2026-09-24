import smtplib
from email.mime.text import MIMEText

# Email info.
with open('secrets.txt') as f:
    email_info = f.read().splitlines()
    EMAILUSER = email_info[0]
    EMAILPASSWORD = email_info[1]
    abbeyEmail = email_info[2]
    bethEmail = email_info[3] 
    jeffEmail = email_info[4]
    judeEmail = email_info[5]
    gregEmail = email_info[6]
    joelEmail = email_info[7]
    chelseaEmail = email_info[8]
    jerryEmail = email_info[9]
    cindyEmail = email_info[10]
    nateEmail = email_info[11]

# The people as objects.
class Name:
    def __init__(self, name, email, conflicts):
        self.name = name
        self.email = email
        self.conflicts = conflicts
        self.pick = ''

# The email sender.
def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print('Message Sent')