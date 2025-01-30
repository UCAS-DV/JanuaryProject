# Music Festival Management System

# Part of ticket function, Adds a new ticket to the ticket list
def TicketAdd(ticket_list):
    ticket_info = []
    user_questions = ["""What ticket would the customer like?
  Tickets include: 1-day, 3-day, and VIP,
    --->  """, 
    "What is the customers name?  --->  ", 
    "How old is the customer?  --->  "]
    for question in range(len(user_questions)):
        while True:
            info = input(user_questions[question])
            if question == 0:
                if info.lower() in ['1-day','1day','1 day','3-day','3day','3 day','vip']:
                    if not info == 'vip':
                        info = f'{info[0]}-day'
                    break
            elif question == 1:
                info = info.title()
                break
            elif question == 2:
                if info.isdigit():
                    break
            print('\033cError That was not a valid option, please try again!')
        ticket_info.append(info)
    ticket_list.append(ticket_info)
    return ticket_list

# Part of ticket function, Changes an existing ticket in the ticket list
def TicketChange(ticket_list):
    while True:
        search1 = input('What name would you like to search for?  --->  ')
        search2 = input('What age would you like to search for?  --->  ')
        search_list = []
        for ticket in ticket_list:
            if search1.startswith(ticket[1]) or ticket[1].startswith(search1):
                if search2 == ticket[2]:
                    search_list.append(ticket)
        if len(search_list) == 1: # If only one item was found, it tells you.
            print(f'A {search_list[-1][0]} ticket with the name: {search_list[-1][1]}, age: {search_list[-1][2]} was found. Is this the right ticket?')
            while True:
                again = input('(y/n) --->  ')
                if again.lower() in ['y','n']:
                    break
                print('\nNot a valid option.')
            if again == 'n': break
        elif len(search_list) >= 2: # If multiple items were would it prints them out and allows you to choose between them
            print(f'{len(search_list)} tickets have been found.')
            for ticket in range(len(search_list)):
                print(f'  {ticket}. {search_list[ticket]}')
            print('\nWhich ticket seemed correct to you?')
            correct = input(' (Input a number)  --->  ')
            # 
        else: # If no items were found it gives the option to do again
            print('\033cNothing was found. Would you like to search again?')
            while True:
                again = input('(y/n) --->  ')
                if again.lower() in ['y','n']:
                    break
                print('\033cNot a valid option.')
            if again == 'n': break


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
ticket_list = TicketUI([['vip','John Cena','84'],['1-day','Jenna','2'],['3-day','Joshua','23']])
print(ticket_list)

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