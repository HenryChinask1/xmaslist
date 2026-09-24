import random, smtplib
from emails import sender_email, santas, secret_keeper
from email.mime.text import MIMEText

class Name:
    def __init__(self, name: str, email: str, conflicts: list[str]):
        self.name: str = name
        self.email: str = email
        self.conflicts: list[str] = conflicts
        self.pick: str = ''

def create_names() -> tuple[list[Name], list[Name]]:
    names: list[Name] = []
    picks: list[Name] = []

    # Load in your gang from emails.py
    # emails should be in the form {name: (email, [exclusions])}
    for name, email in santas.items():
        name = Name(name, email[0], email[1])
        names.append(name)
        picks.append(name)

    random.shuffle(names)
    random.shuffle(picks)
    return names, picks

def send_email(subject: str, body: str, sender: str, recipients: str, password: str):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print('Message Sent')

def main():

    (names, picks) = create_names()
    # Choose names until there is a conflict, then keep starting over.
    picked: int = 0
    trys: int = 0
    while picks and picked < len(names):
        if picks[-1].name not in names[picked].conflicts:
            names[picked].pick = picks[-1].name
            picks.pop()
            picked += 1
        else: # Start over.
            (names, picks) = create_names()
            picked = 0
            trys += 1

    allPicks: list[str] = []

    # Fire out the emails.
    for recipient in names:
        subject: str = 'Your Secret Santa'
        body: str = f'Your secret santa is {recipient.pick}!\n\n It took {trys} repicks to get it right.'
        allPicks.append(f'{recipient.name} picked {recipient.pick}')
        sender: str = sender_email['email']
        password: str = sender_email['key']
        recipients: str = recipient.email
        send_email(subject, body, sender, recipients, password)

    # Send the all picks list to the secret_keeper to check.
    allBody: str = f'The secret santa picks are {allPicks}.\n\nIt took {trys} repicks to get it right.'
    knows_all: Name = Name(secret_keeper[0], secret_keeper[1], [secret_keeper[0]])
    send_email("All secret santa picks", allBody, sender_email['email'], knows_all.email, sender_email['key'])

if __name__ == '__main__':
    main()