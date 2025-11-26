import random, config
from config import Name, send_email

# Load in the gang.
beth = Name('Beth', 'bethbaier1007@outlook.com', ['Jeff', 'Beth'])
jeff = Name('Jeff', 'jeffbaier72@yahoo.com', ['Beth', 'Jeff'])
jude = Name('Jude', 'judeherman1@aol.com', ['Greg', 'Jude'])
greg = Name('Greg', 'undecidedgd@yahoo.com', ['Jude', 'Greg'])
joel = Name('Joel', 'jbaier@ewmi.com', ['Chelsea', 'Joel'])
chelsea = Name('Chelsea', 'chelseakutun@gmail.com',['Joel', 'Chelsea'])
jerry = Name('Jerry', 'jerryfkw@ptd.net', ['Cindy', 'Jerry'])
cindy = Name('Cindy', 'crazy4baskets2@yahoo.com', ['Jerry', 'Cindy'])
nate = Name('Nate', 'email', ['Nate'])
abbey = Name('Abbey', 'apb091108@gmail.com', ['Abbey'])

# Add everyone to two lists and then mix 'em up.
names = [beth, jeff, jude, greg, joel, chelsea, jerry, cindy, nate]
random.shuffle(names)
picks = [beth, jeff, jude, greg, joel, chelsea, jerry, cindy, nate]
random.shuffle(picks)

# Choose names until there is a conflict, then keep starting over.
i = 0
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

allPicks = []

# Fire out the emails.
for i in names:
    subject = 'Your Secret Santa'
    body = f'Your secret santa is {i.pick}!'
    allPicks.append(f'{i.name} picked {i.pick}')
    sender = config.EMAILUSER
    password = config.EMAILPASSWORD
    recipients = i.email
    # if i.email:
    #     send_email(subject, body, sender, recipients, password)

# Send the all picks list to Abbey to check.
allBody = f'The secret santa picks are {allPicks}.'
send_email("All secret santa", allBody, config.EMAILUSER, joel.email, config.EMAILPASSWORD)