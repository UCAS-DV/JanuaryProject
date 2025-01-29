# Music Festival Management System

# This UI function is used for giving user options to add, change, remove their ticket in the ticket list. Returns a changed ticket list like this [[ticket, name, age], [ticket, name, age]] ect.
def TicketUI(ticket_list):
    print('\033c')
    while True:
        print('''Please select a ticket option (Choose a number 1-3):
  1. Add a Ticket
  2. Change a Ticket
  3. Remove a Ticket''')
        option = input(' --->  ')
        if option == '1':
            pass
        elif option == '2':
            pass
        elif option == '3':
            pass
        else:
            print('\033cThat was not a valid option please try again!\n')
            continue
        return ticket_list


# This UI function is used for giving user options to add, change, remove their ticket in the ticket list. Returns a changed ticket list like this [[ticket, name, age], [ticket, name, age]] ect.
def TicketUI(ticket_list):
    print('\033c')
    while True:
        print('''Please select a ticket option (Choose a number 1-3):
  1. Add a Ticket
  2. Change a Ticket
  3. Remove a Ticket''')
        option = input(' --->  ')
        if option == '1':
            pass
        elif option == '2':
            pass
        elif option == '3':
            pass
        else:
            print('\033cThat was not a valid option please try again!\n')
            continue
        return ticket_list


currentTimes = ()
currentTimeframes = []

schedule = ()

def updateCurrentTimes():
    pass

artist_list = [{'name': 'Eminem', 'genre': 'Rap', 'start': schedule[9], 'end': 11.30}]

days = int(input("How many days are you going to have the festival be?:"))

def ListArtists():
    for artist in artist_list:
        print(f'Name: {artist['name']}')
        print(f'Genre: {artist['genre']}')

ListArtists()
