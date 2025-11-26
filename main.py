import smtplib
from email.mime.text import MIMEText
import random, config

class Name:

    def __init__(self, name, email, conflicts, number):
        self.name = name
        self.email = email
        self.conflicts = conflicts
        self.number = number
        self.pick = ''

beth = Name('Beth', 'bethbaier1007@outlook.com', ['Jeff', 'Beth'], 0)
jeff = Name('Jeff', 'jeffbaier72@yahoo.com', ['Beth', 'Jeff'], 1)
jude = Name('Jude', 'judeherman1@aol.com', ['Greg', 'Jude'], 2)
greg = Name('Greg', 'undecidedgd@yahoo.com', ['Jude', 'Greg'], 3)
joel = Name('Joel', 'jbaier@ewmi.com', ['Chelsea', 'Joel'], 4)
chelsea = Name('Chelsea', 'ex@ex.com',['Joel', 'Chelsea'], 5)
jerry = Name('Jerry', 'ex@ex.com', ['Cindy', 'Jerry'], 6)
cindy = Name('Cindy', 'ex@ex.com', ['Jerry', 'Cindy'], 7)

names = [beth, jeff, jude, greg, joel, chelsea, jerry, cindy]
random.shuffle(names)
picks = [beth, jeff, jude, greg, joel, chelsea, jerry, cindy]
random.shuffle(picks)

i = 0
while picks and i < 8:
    if picks[-1].name not in names[i].conflicts:
        names[i].pick = picks[-1].name
        picks.pop()
        i += 1
    else:
        picks = [beth, jeff, jude, greg, joel, chelsea, jerry, cindy]
        for i in names:
            i.pick = ''
        random.shuffle(picks)
        i = 0

for i in names:
    print(i.name, i.pick)


subject = 'Your Secret Santa'
body = f'Your secret santa is {jeff.pick}!'
sender = config.EMAILUSER
recipients = jeff.email
password = config.EMAILPASSWORD

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print('Message Sent')

send_email(subject, body, sender, recipients, password)