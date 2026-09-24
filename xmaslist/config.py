import smtplib
from email.mime.text import MIMEText

# Email info.
with open('secrets.txt') as f:
    email_info: list[str] = f.read().splitlines()
    EMAILUSER: str = email_info[0]
    EMAILPASSWORD: str = email_info[1]
    abbeyEmail: str = email_info[2]
    bethEmail: str = email_info[3] 
    jeffEmail: str = email_info[4]
    judeEmail: str = email_info[5]
    gregEmail: str = email_info[6]
    joelEmail: str = email_info[7]
    chelseaEmail: str = email_info[8]
    jerryEmail: str = email_info[9]
    cindyEmail: str = email_info[10]
    nateEmail: str = email_info[11]

# The people as objects.
class Name:
    def __init__(self, name: str, email: str, conflicts: list[str]):
        self.name: str = name
        self.email: str = email
        self.conflicts: list[str] = conflicts
        self.pick: str = ''

# The email sender.
def send_email(subject: str, body: str, sender: str, recipients: str, password: str):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print('Message Sent')