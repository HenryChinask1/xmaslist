import smtplib
from email.mime.text import MIMEText
import random, config

class Name:

    def __init__(self, name, email, conflicts, number):
        self.name = name
        self.email = email
        self.conflicts = conflicts
        self.number = number

beth = Name('Beth', 'bethbaier1007@outlook.com', 'Jeff', 0)
jeff = Name('Jeff', 'jeffbaier72@yahoo.com', 'Beth', 1)
jude = Name('Jude', 'judeherman1@aol.com', 'Greg', 2)
greg = Name('Greg', 'undecidedgd@yahoo.com', 'Jude', 3)
joel = Name('Joel', 'jbaier@ewmi.com', 'Chelsea', 4)
chelsea = Name('Chelsea', 'ex@ex.com','Joel', 5)
jerry = Name('Jerry', 'ex@ex.com', 'Cindy', 6)
cindy = Name('Cindy', 'ex@ex.com', 'Jerry', 7)

# The gang and thier conflicts.
names = {'Beth': ['bethbaier1007@outlook.com', 'Jeff'], 
         'Jeff': ['jeffbaier72@yahoo.com', 'Beth'], 
         'Jude': ['judeherman1@aol.com', 'Greg'], 
         'Greg': ['undecidedgd@yahoo.com', 'Jude'], 
         'Joel': ['jbaier@ewmi.com', 'Chelsea'], 
         'Chelsea': ['ex@ex.com','Joel'], 
         'Jerry': ['ex@ex.com', 'Cindy'], 
         'Cindy': ['ex@ex.com', 'Jerry']}

print(names)
random.shuffle(names)
print(names)
numbers = [str(i) for i in range(8)]
random.shuffle(numbers)
print(numbers)

# subject = 'Your Secret Santa'
# body = f'Your secret santa is {name}!'
# sender = config.EMAILUSER
# recipients = name.email
# password = config.PASSWORD

# def send_email(subject, body, sender, recipients, password):
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = sender
#     msg['To'] = recipients
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
#         smtp_server.login(sender, password)
#         smtp_server.sendmail(sender, recipients, msg.as_string())
#     print('Message Sent')

# send_email()