import random, config
from config import Name, send_email

def main():
    
    # Load in the gang.
    beth: Name = Name('Beth', config.bethEmail, ['Jeff', 'Beth'])
    jeff: Name = Name('Jeff', config.jeffEmail, ['Beth', 'Jeff'])
    jude: Name = Name('Jude', config.judeEmail, ['Greg', 'Jude'])
    greg: Name = Name('Greg', config.gregEmail, ['Jude', 'Greg'])
    joel: Name = Name('Joel', config.joelEmail, ['Chelsea', 'Joel'])
    chelsea: Name = Name('Chelsea', config.chelseaEmail,['Joel', 'Chelsea'])
    jerry: Name = Name('Jerry', config.jerryEmail, ['Cindy', 'Jerry'])
    cindy: Name = Name('Cindy', config.cindyEmail, ['Jerry', 'Cindy'])
    nate: Name = Name('Nate', config.nateEmail, ['Nate'])
    abbey: Name = Name('Abbey', config.abbeyEmail, ['Abbey'])

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
        sender: str = config.EMAILUSER
        password: str = config.EMAILPASSWORD
        recipients: str = recipient.email
        if recipient.email:
            send_email(subject, body, sender, recipients, password)

    # Send the all picks list to Abbey to check.
    allBody: str = f'The secret santa picks are {allPicks}.\n\nIt took {trys} repicks to get it right.'
    send_email("All secret santa", allBody, config.EMAILUSER, abbey.email, config.EMAILPASSWORD)

if __name__ == '__main__':
    main()