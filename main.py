import random, config
from config import Name, send_email

# Load in the gang.
beth = Name('Beth', config.bethEmail, ['Jeff', 'Beth'])
jeff = Name('Jeff', config.jeffEmail, ['Beth', 'Jeff'])
jude = Name('Jude', config.judeEmail, ['Greg', 'Jude'])
greg = Name('Greg', config.gregEmail, ['Jude', 'Greg'])
joel = Name('Joel', config.joelEmail, ['Chelsea', 'Joel'])
chelsea = Name('Chelsea', config.chelseaEmail,['Joel', 'Chelsea'])
jerry = Name('Jerry', config.jerryEmail, ['Cindy', 'Jerry'])
cindy = Name('Cindy', config.cindyEmail, ['Jerry', 'Cindy'])
nate = Name('Nate', config.nateEmail, ['Nate'])
abbey = Name('Abbey', config.abbeyEmail, ['Abbey'])

# Add everyone to two lists and then mix 'em up.
names = [beth, jeff, jude, greg, joel, chelsea, jerry, cindy, nate]
random.shuffle(names)
picks = [beth, jeff, jude, greg, joel, chelsea, jerry, cindy, nate]
random.shuffle(picks)

# Choose names until there is a conflict, then keep starting over.
i = 0
trys = 0
while picks and i < 9:
    if picks[-1].name not in names[i].conflicts:
        names[i].pick = picks[-1].name
        picks.pop()
        i += 1
    else: # Start over.
        picks = [beth, jeff, jude, greg, joel, chelsea, jerry, cindy, nate]
        for i in names:
            i.pick = ''
        random.shuffle(picks)
        i = 0
        trys += 1

allPicks = []

# Fire out the emails.
for i in names:
    subject = 'Your Secret Santa'
    body = f'Your secret santa is {i.pick}! It took {trys} repicks to get it right.'
    allPicks.append(f'{i.name} picked {i.pick}')
    sender = config.EMAILUSER
    password = config.EMAILPASSWORD
    recipients = i.email
    # if i.email:
    #     send_email(subject, body, sender, recipients, password)

# Send the all picks list to Abbey to check.
allBody = f'The secret santa picks are {allPicks}.\nIt took {trys} repicks to get it right.'
send_email("All secret santa", allBody, config.EMAILUSER, jude.email, config.EMAILPASSWORD)