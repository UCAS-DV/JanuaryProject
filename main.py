# Music Festival Management System

# ------------------------------------ START OF GABES CODE ------------------------------------------
# Displays tickets in a list with each ticket numbered
def TicketDisplay(ticket_list):
    print('\033cDisplaying tickets:')

    for i in range(len(ticket_list)):
        # Prints the name, the age, and then the ticket type
        print(f"{i+1}. Name: {ticket_list[i]['Name']}, Age: {ticket_list[i]['Age']}, Ticket Type: {ticket_list[i]['Type']}")


# Part of ticket function, Adds a new ticket to the ticket list
def TicketAdd(ticket_list):
    # This list will store the user info into ticket format where it will be appeded into the bigger lst
    ticket_info = []
    # This contains the questions the user will be asked
    user_questions = ["""What ticket would the customer like?
  Tickets include: 1-day, 3-day, and VIP,
    --->  """, 
    "What is the customers name?  --->  ", 
    "How old is the customer?  --->  "]

    # This loops through each question, gets user input, and changes it accordingly for each question. Ensures user info is correct format
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
            
            print('\033cError That was not a valid option, please try again!') # If none of the questions could run, the user tpyed in something invalid

        ticket_info.append(info) # Once the question is asked the user info is stored inside of a list
    dict_info = {'Type':ticket_info[0],'Name':ticket_info[1],'Age':ticket_info[2]}
    ticket_list.append(dict_info) # Which is appended to ticket info to shortly be returned
    return ticket_list


# This function actually changes the ticket data.
def TicketChange(ticket_list, searched_item):

    ticket_location = ticket_list.index(searched_item)
    print('''What would you like to change?:
  Type
  Name
  Age''')
    
    # Asks user what they would like to change on the ticket (name, age, and ticket type).
    while True:
        changeType = input('  --->  ')
        if changeType.lower() in ['type','name','age']:
            break
        print('\nThat was not a valid option. (Options: type, name, age)')

    # Allows user to actually change the ticket
    while True:
        info = input(f'What would you like to change the {changeType} to?  --->  ')

        # If the user wants to change ticket type
        if changeType == 'type':
            if info.lower() in ['1-day','1day','1 day','3-day','3day','3 day','vip']:
                if not info == 'vip':
                    info = f'{info[0]}-day'
                    break
        
        # if the user want to change their name
        elif changeType == 'name':
            info = info.title()
            break

        # if the user wants to change their age
        elif changeType == 'age':
            if info.isdigit():
                break

        print('Error That was not a valid option, please try again!')
    ticket_list[ticket_location][changeType.title()] = info # Returns the changed and error handled ticket list
    return ticket_list


# Part of ticket function, Searches for an existing ticket in the ticket list
def TicketSearch(ticket_list, action):
    while True:
        # Searches for tickets based off of age, and name
        search1 = input('\033cWhat name would you like to search for?  --->  ')
        search2 = input('What age would you like to search for?  --->  ')

        # This list will contain all of the found tickets based off of search results
        search_list = []
        for ticket in ticket_list:
            if search1.title().startswith(ticket['Name']) or ticket['Name'].startswith(search1.title()):
                if search2 == ticket['Age']:
                    search_list.append(ticket)

        # These will collect 1 ticket that can be removed or changed at the end of the function
        if len(search_list) == 1: # If only one item was found, it tells you.
            print(f"\033cA {search_list[-1]['Type']} ticket with the name: {search_list[-1]['Name']}, age: {search_list[-1]['Age']} was found. Is this the right ticket?")
            while True:
                again = input('(y/n) --->  ')
                if again.lower() in ['y','n']:
                    break
                print('\nNot a valid option.')
            if again == 'y': break

        elif len(search_list) >= 2: # If multiple items were would it prints them out and allows you to choose between them
            print(f'\033c{len(search_list)} tickets have been found.')
            for ticket in range(len(search_list)):
                print(f"  {ticket+1}. Name: {search_list[ticket]['Name']}, Age: {search_list[ticket]['Age']}, Type: {search_list[ticket]['Type']}")
            print('\nWhich ticket seemed correct to you?')
            while True:
                try:
                    correct = int(input(' (Input a number)  --->  '))
                    if correct <= len(search_list) and correct > 0:
                        search_list = [search_list[correct-1]]
                        break
                except:
                    print('\nThat was not a valid option, please try again...')
            break

        else: # If no items were found it gives the option to search for another item.
            print('\033cNothing was found. Would you like to search again?')
            while True:
                again = input('(y/n) --->  ')
                if again.lower() in ['y','n']:
                    break
                print('\033cNot a valid option.')
            if again == 'n': return ticket_list

    if action == 'change': ticket_list = TicketChange(ticket_list, search_list[0]) # if the user wants to change 
    elif action == 'remove': ticket_list.remove(search_list[0])
    return ticket_list


# This UI function is used for giving user options to add, change, remove their ticket in the ticket list. Returns a changed ticket list like this [[ticket, name, age], [ticket, name, age]] ect. (Gabe's Section)
def TicketUI(ticket_list):
    print('\033c') # clears terminal

    # While true ensures the user inputs a correct option, and runs each function which changes the ticket information
    while True:
        print('''Please select a ticket option (Choose a number 1-3):
  1. Add a Ticket
  2. Change a Ticket
  3. Remove a Ticket''')
        option = input(' --->  ')

        print('\033c')
        if option == '1':
            ticket_list = TicketAdd(ticket_list)

        elif option == '2':
            ticket_list = TicketSearch(ticket_list,'change')

        elif option == '3':
            ticket_list = TicketSearch(ticket_list,'remove')

        else:
            print('\033cThat was not a valid option please try again!\n')
            continue
        return ticket_list # returns ticket list to main function for usage later

# ------------------------------------ END OF GABES CODE ------------------------------------------

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