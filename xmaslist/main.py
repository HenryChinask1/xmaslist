import random, smtplib
from emails import sender_email, emails
from email.mime.text import MIMEText

class Name:
    def __init__(self, name: str, email: str, conflicts: list[str]):
        self.name: str = name
        self.email: str = email
        self.conflicts: list[str] = conflicts
        self.pick: str = ''

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
    
    # Load in the gang.
    beth: Name = Name('Beth', emails['beth'], ['Jeff', 'Beth'])
    jeff: Name = Name('Jeff', emails['jeff'], ['Beth', 'Jeff'])
    jude: Name = Name('Jude', emails['jude'], ['Greg', 'Jude'])
    greg: Name = Name('Greg', emails['greg'], ['Jude', 'Greg'])
    joel: Name = Name('Joel', emails['joel'], ['Chelsea', 'Joel'])
    chelsea: Name = Name('Chelsea', emails['chelsea'],['Joel', 'Chelsea'])
    jerry: Name = Name('Jerry', emails['jerry'], ['Cindy', 'Jerry'])
    cindy: Name = Name('Cindy', emails['cindy'], ['Jerry', 'Cindy'])
    nate: Name = Name('Nate', emails['nate'], ['Nate'])
    abbey: Name = Name('Abbey', emails['abbey'], ['Abbey'])

    # Add everyone to two lists and then mix 'em up.
    names: list[Name] = [beth, jeff, jude, greg, joel, chelsea, jerry, cindy, nate]
    random.shuffle(names)
    picks: list[Name] = [beth, jeff, jude, greg, joel, chelsea, jerry, cindy, nate]
    random.shuffle(picks)

    # Choose names until there is a conflict, then keep starting over.
    picked: int = 0
    trys: int = 0
    while picks and picked < 9:
        if picks[-1].name not in names[picked].conflicts:
            names[picked].pick = picks[-1].name
            picks.pop()
            picked += 1
        else: # Start over.
            picks: list[Name] = [beth, jeff, jude, greg, joel, chelsea, jerry, cindy, nate]
            for name_picking in names:
                name_picking.pick = ''
            random.shuffle(picks)
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
        if recipient.email:
            send_email(subject, body, sender, recipients, password)

    # Send the all picks list to Abbey to check.
    allBody: str = f'The secret santa picks are {allPicks}.\n\nIt took {trys} repicks to get it right.'
    send_email("All secret santa", allBody, sender_email['email'], abbey.email, sender_email['password'])

if __name__ == '__main__':
    main()