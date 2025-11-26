import smtplib
from email.mime.text import MIMEText

# Email info.
with open('info.txt').read().split('\n') as f:
    EMAILUSER = f[0]
    EMAILPASSWORD = f[1]

# The people.
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