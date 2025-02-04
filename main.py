

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


currentTimes = ()
currentTimeframes = []
schedule = []

clearTimeframes = []

days = 0
dayCount = 0

# Prints out filled time frames with the performances happening then 
def print_timetable():
    for timeFrame in unclearTimeframes:
        performance = performances[unclearTimeframes.index(timeFrame)]

        print(f"{timeFrame} - {performance['Artist']['name']}'s {performance['Artist']['genre']} performance")

def update_current_times(timeframes, startTime, endTime):
    timeframeCount = timeframes
    timeNow = startTime
    timeNowHour = round(startTime)

    currentTimes = currentTimes + timeNow
    currentTimes = currentTimes + timeNowHour

    while timeNow <= endTime:
        remainder = timeframeCount % 2
        if remainder == 1:
            timeNowHour = timeNowHour + 1
        elif remainder == 0:
            timeNow = timeNow + .30
    
    schedule = schedule + timeNow
    schedule = schedule + timeNowHour
    schedule = sorted(schedule)
    clearTimeframes = schedule
    return clearTimeframes, schedule

def modify_festival_length():
    if days >= dayCount:
        dayStart = int(input("What time does the day start? (Make it an hour, no minutes)"))
        dayEnd = float(input("What time does the day end? (Minutes are after a decimal point, ex 12.30)"))
        timeframes = dayEnd - dayStart
        timeframes = timeframes / 2
        currentTimeframes = currentTimeframes.append(timeframes)
        update_current_times(timeframes, dayStart, dayEnd)

def performancesInDay(startTime, endTime):
    performInDay = int(input("How many performances are in this day?"))

    sample_performance = {'Artist': {}, 'Start Time': 1.30, 'End Time': 2.30}

    while performInDay >= 1:
        
        try:
            sample_performance['Artist'] = artist_list[get_artist()]
        except:
            input("Couldn't find artist")
            break

        startTime = float(input("What time do you want the performance to start? (military time with minutes after a decimal, Ex. 16.30 is 4:30 PM)"))
        endTime = float(input("What time do you want the performance to end? (military time with minutes after a decimal, Ex. 16.30 is 4:30 PM)"))
        nowTime = startTime

        sample_performance['Start Time'] = startTime
        sample_performance['End Time'] = endTime

        if nowTime in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]:
            clearTimeframes.remove(nowTime)
            unclearTimeframes.append(nowTime)
            nowTime = nowTime + .30
            if nowTime == endTime:
                continue
        elif nowTime in [1.30, 2.30, 3.30, 4.30, 5.30, 6.30, 7.30, 8.30, 9.30, 10.30, 11.30, 12.30, 13.30, 14.30, 15.30, 16.30, 17.30, 18.30, 19.30, 20.30, 21.30, 22.30, 23.30]:
            clearTimeframes.remove(nowTime)
            unclearTimeframes.append(nowTime)
            nowTime = round(nowTime)
            nowTime = nowTime + 1
        performInDay -= 1

#Jonas Fairchild, Master display and Main function

def display_all(): #Uses a combination of display functions from every part of the code to display everything imaginable.
    print("---------- Artists ----------\n")
    print_artists()
    print("\n---------- Schedule ----------\n")
    print("\n---------- Venues ----------\n")
    display_venues()
    print("\n---------- Tickets/attendees ----------\n")

def time_menu():
    while True:
        os.system('cls')
        print('"---------- Time ----------')
        match input('What do you want to do with time? \nSee Time Table \n2. Modify Festival Hours \n3. Set Performances \n6.'):
            case '1':
                print_timetable()
            case '2':
                modify_festival_length()
            case '3':
                performancesInDay()
            case '6':
                main()
                break
            case _:
                input('Invalid Input')

def artist_menu():
    while True:
        os.system('cls')
        print('"---------- Artists ----------')
        match input('What do you want to do with the artists? \n1. See Artists \n2. Add Artist \n3. Remove Artist \n4. Modify Artist \n6. Go Back \n'):
            case '1':
                print_artists()
            case '2':
                add_artist()
            case '3':
                remove_artist()
            case '4':
                modify_artist()
            case '6':
                main()
                break
            case _:
                input('Invalid Input')
                

def main(): #Provides a UI that branches to every part of the program, allowing modification of everything.
    while True:
        os.system("cls")
        choice = input("What do you want to do?\n1. Manage artists\n2. Manage schedule\n3. Manage venues\n4. Manage ticket sales/attendees\n5. Display everything\n6. Exit program\n")
        if choice == '1':
            artist_menu()
        elif choice == '2':
            time_menu()
        elif choice == '3':
            venues = venue_management()
        elif choice == '4':
            pass
        elif choice == '5':
            display_all()
        elif choice == '6':
            break
        else:
            print("That isn't on the list of options. Try again.")
