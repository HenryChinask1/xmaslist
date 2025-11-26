import smtplib
from email.mime.text import MIMEText
import random, config

class Name:

    def __init__(self, name, email, conflicts):
        self.name = name
        self.email = email
        self.conflicts = conflicts
        self.pick = ''

# Load in the gang.
beth = Name('Beth', 'bethbaier1007@outlook.com', ['Jeff', 'Beth'])
jeff = Name('Jeff', 'jeffbaier72@yahoo.com', ['Beth', 'Jeff'])
jude = Name('Jude', 'judeherman1@aol.com', ['Greg', 'Jude'])
greg = Name('Greg', 'undecidedgd@yahoo.com', ['Jude', 'Greg'])
joel = Name('Joel', 'jbaier@ewmi.com', ['Chelsea', 'Joel'])
chelsea = Name('Chelsea', 'ex@ex.com',['Joel', 'Chelsea'])
jerry = Name('Jerry', 'ex@ex.com', ['Cindy', 'Jerry'])
cindy = Name('Cindy', 'ex@ex.com', ['Jerry', 'Cindy'])

# Add everyone to two lists and then mix 'em up.
names = [beth, jeff, jude, greg, joel, chelsea, jerry, cindy]
random.shuffle(names)
picks = [beth, jeff, jude, greg, joel, chelsea, jerry, cindy]
random.shuffle(picks)

# Choose names until there is a conflict, then keep starting over.
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

# Fire out the emails.
for i in names:
    subject = 'Your Secret Santa'
    body = f'Your secret santa is {i.pick}!'
    sender = config.EMAILUSER
    password = config.EMAILPASSWORD
    recipients = i.email
    send_email(subject, body, sender, recipients, password)