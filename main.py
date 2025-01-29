# Music Festival Management System

# Part of ticket function, Adds a new ticket to the ticket list
def TicketAdd(ticket_list):
    ticket_info = []
    user_questions = ["""What ticket would the customer like?
  Tickets include: 1-day, 3-day, and VIP,
    --->  ||1-day|1day|1 day:3-day|3day|3 day:vip""", 
    "What is the customers name?  --->  ||title", 
    "How old is the customer?  --->  ||digit"]
    for i in range(len(user_questions)):
        while True:
            info = input(user_questions[i].split('||')[0])
            if user_questions[i].split('||')[-1] == 'digit':
                try: int(info)
                except:
                    print('That was not a number, please try again!')
                    continue
            elif user_questions[i].split('||')[-1] == 'title':
                info = info.title()
            else:
                for answerGroup in user_questions[i].split('||')[-1].split(':'):
                    for answer in answerGroup.split('|'):
                        if info == answer:
                            info = answerGroup.split('|')[0]
                            break # This checks if the user input is equal to a viable answe and beraks not very good, needs to break out of mulriple loops
            ticket_info.append(info)
    print(ticket_info)

# Part of ticket function, Changes an existing ticket in the ticket list
def TicketChange(ticket_list):
    pass

# Part of ticket function, Removes an existing ticket in the ticket list
def TicketRemove(ticket_list):
    pass

# This UI function is used for giving user options to add, change, remove their ticket in the ticket list. Returns a changed ticket list like this [[ticket, name, age], [ticket, name, age]] ect. (Gabe's Section)
def TicketUI(ticket_list):
    print('\033c')
    while True:
        print('''Please select a ticket option (Choose a number 1-3):
  1. Add a Ticket
  2. Change a Ticket
  3. Remove a Ticket''')
        option = input(' --->  ')
        if option == '1':
            ticket_list = TicketAdd(ticket_list)
        elif option == '2':
            pass
        elif option == '3':
            pass
        else:
            print('\033cThat was not a valid option please try again!\n')
            continue
        return ticket_list
TicketUI(1)

"""
currentTimes = ()
currentTimeframes = []

schedule = ()

def updateCurrentTimes():
    

artist_list = [{'name': 'Eminem', 'genre': 'Rap', 'start': schedule[9], 'end': 11.30}]

days = int(input("How many days are you going to have the festival be?:"))

def ListArtists():
    for artist in artist_list:
        print(f'Name: {artist['name']}')
        print(f'Genre: {artist['genre']}')

ListArtists()
"""