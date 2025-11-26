import smtplib
from email.mime.text import MIMEText

# Email info.
f = open('info.txt').read().split('\n')
EMAILUSER = f[0]
EMAILPASSWORD = f[1]
abbeyEmail = f[2]
bethEmail = f[3] 
jeffEmail = f[4]
judeEmail = f[5]
gregEmail = f[6]
joelEmail = f[7]
chelseaEmail = f[8]
jerryEmail = f[9]
cindyEmail = f[10]
nateEmail = f[11]

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