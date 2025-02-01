
#Music Festival Management System

# ------------------------------------ START OF GABES CODE ------------------------------------------

attendee_list = []
# Displays tickets in a list with each ticket numbered
def ticket_display(ticket_list):
    print('\033cDisplaying tickets:')

    for i in range(len(ticket_list)):
        # Prints the name, the age, and then the ticket type
        print(f"{i+1}. Name: {ticket_list[i]['Name']}, Age: {ticket_list[i]['Age']}, Ticket Type: {ticket_list[i]['Type']}")


# Part of ticket function, Adds a new ticket to the ticket list
def ticket_add(ticket_list):
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
    attendee_list.append(dict_info)
    return ticket_list


# This function actually changes the ticket data.
def ticket_change(ticket_list, searched_item):

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
def ticket_search(ticket_list, action):
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

    if action == 'change': ticket_list = ticket_change(ticket_list, search_list[0]) # if the user wants to change 
    elif action == 'remove': 
        ticket_list.remove(search_list[0])
        attendee_list.remove(search_list[0])
    return ticket_list


# This UI function is used for giving user options to add, change, remove their ticket in the ticket list. Returns a changed ticket list like this [[ticket, name, age], [ticket, name, age]] ect. (Gabe's Section)
def ticket_UI(ticket_list):
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
            ticket_list = ticket_search(ticket_list)

        elif option == '2':
            ticket_list = ticket_search(ticket_list,'change')

        elif option == '3':
            ticket_list = ticket_search(ticket_list,'remove')

        else:
            print('\033cThat was not a valid option please try again!\n')
            continue
        return ticket_list # returns ticket list to main function for usage later

# ------------------------------------ END OF GABES CODE ------------------------------------------

# Jonas Fairchild, Venue Management

import os
venues = []

def venue_modify(): #Handles all modification for all venues.
    choice = input("Do you want to add or remove a venue?: ").lower()

    if choice == "remove": #Handles venue removal
        if venues: #Checks if the list is not empty
            print("Which venue do you want to remove?")
            for i, venue in enumerate(venues, start = 1): #Displays each venue with a number
                print(f"{i}. {venue['name']}")
            removal = input().lower()
            for venue in venues:
                if venue["name"].lower() == removal:
                    venues.remove(venue) #Removes the venue from the list
                    print("Successfully removed venue.")
                    return venues 
            print("That venue isn't on the list.")
        else:
            print("There are no venues to remove.")

    elif choice == "add": #Handles venue adding
        venue_name = input("What is the name of your venue?: ")
        if not any(v["name"].lower() == venue_name.lower() for v in venues): #Avoids duplicates
            venues.append({"name": venue_name, "stage": []}) #Adds the venue to the list
            print(f"Venue successfully added.")
        else:
            print("That venue already exists.")

    else: #Handles nonsense makers :)
        print("Invalid input. Try again.")
        return venue_modify()

    return venues

def stage_modify(): #Handles the modification for the stages within each venue.
    if venues:
        while True:
            print("Which venue's stages do you want to modify?")
            for i, venue in enumerate(venues, start = 1):
                print(f"{i}. {venue['name']}")
            venue_choice = input().lower()
            if any(v["name"].lower() == venue_choice for v in venues):
                break
            print("That venue isn't on the list. Try again.")
        venue = next((v for v in venues if v['name'].lower() == venue_choice.lower()), []) #Specifies the venue that the name references
        choice = input("Do you want to add or remove a stage?: ").lower()
        
        if choice == "remove": #Handles the removal of stages
            if venue['stage']: #Checks if the list is not empty
                print("Which stage do you want to remove?")
                for i, stage in enumerate(venue['stage'], start = 1): #Displays each venue with a number
                    print(f"{i}. {stage['name']}")
                removal = input().lower()
                for stage in venue['stage']:
                    if stage["name"].lower() == removal:
                        venue['stage'].remove(stage) #Removes the stage from the list
                        print("Successfully removed stage.")
                        return venues 
                print("That stage isn't on the list.")
            else:
                print("There are no stages to remove.")

        elif choice == "add": #Handles the adding of stages
            stage_name = input("What is the name of your stage?: ")
            if not any(s["name"].lower() == stage_name.lower() for s in venue['stage']): #Avoids duplicates
                venue['stage'].append({"name": stage_name, "equipment": []}) #Adds the stage to the list
                print(f"Stage successfully added.")
            else:
                print("That stage already exists.")
        
        else:
            print("Invalid input. Try again.")
            return stage_modify()
    else:
        print("There are no venues to put stages at.")

    return venues

def equipment_modify(): #Handles the modification for the equipment lists for each stage.
    if venues:
        while True:
            print("On which venue are the stages whose equipment lists you want to modify?")
            for i, venue in enumerate(venues, start = 1):
                print(f"{i}. {venue['name']}")
            venue_choice = input().lower()
            if any(v["name"].lower() == venue_choice for v in venues):
                break
            print("That venue isn't on the list. Try again.")
        venue = next((v for v in venues if v['name'].lower() == venue_choice.lower()), []) #Specifies the venue that the name references
        
        while True:
            print("Which stage has equipment lists you want to modify?")
            for i, stage in enumerate(venue["stage"], start = 1):
                print(f"{i}. {stage['name']}")
            stage_choice = input().lower()
            if any(s["name"].lower() == stage_choice for s in venue["stage"]):
                break
            print("That stage isn't on the list. Try again.")
        stage = next((s for s in venue["stage"] if s['name'].lower() == stage_choice.lower()), []) #Specifies the stage that the name references
        choice = input("Do you want to add or remove equipment?: ").lower()
        
        if choice == "remove": #Handles the removal of equipment
            if stage['equipment']: #Checks if the list is not empty
                print("Which equipment do you want to remove?")
                for i, equipment in enumerate(stage['equipment'], start = 1): #Displays each venue with a number
                    print(f"{i}. {equipment['name']}")
                removal = input().lower()
                for equipment in stage['equipment']:
                    if equipment["name"].lower() == removal:
                        stage['equipment'].remove(equipment) #Removes the equipment from the list
                        print("Successfully removed equipment.")
                        return venues 
                print("That stage isn't on the list.")
            else:
                print("There is no equipment to remove.")
  
        elif choice == "add": #Handles the adding of equipment
            equipment_name = input("What is the name of your equipment?: ")
            while True:
                try:
                    equipment_count = int(input("How much of this equipment is needed?: "))
                    break
                except:
                    print("That's not an integer. Try again.")

            if not any(e["name"].lower() == equipment_name.lower() for e in stage['equipment']): #Avoids duplicates
                stage['equipment'].append({"name": equipment_name, "count": equipment_count}) #Adds the equipment to the list
                print(f"Equipment successfully added.")
            else:
                print("That equipment already exists.")
        
        else:
            print("Invalid input. Try again.")
            return equipment_modify()
    else:
        print("There are no venues to put stages' equipment lists at.")

    return venues

def display_venues(venues_for_display): #Shows all venues in an organized manner.
    if venues_for_display:
        for venue in venues_for_display:
            print(f"{venue['name']}.")
            for stage in venue['stage']:
                print(f"\t{stage['name']}.")
                for equipment in stage['equipment']:
                    print(f"\t\t{equipment['count']} {equipment['name']}s")
    else:
        print("There's nothing to display.")

def venue_management(): #A sort of sub-main function that contains a user interface for this smaller part of the program.
    while True:
        try:
            choice = int(input("What do you want to do?\n1. Add/Remove a venue\n2. Add/Remove a stage\n3. Add/Remove equipment\n4. Display all venues/stages/equipment\n5. Exit venue management\n"))
            if choice == 1:
                venues = venue_modify()
            elif choice == 2:
                venues = stage_modify()
            elif choice == 3:
                venues = equipment_modify()
            elif choice == 4:
                display_venues()
            elif choice == 5:
                try:
                    return venues
                except:
                    venues = []
                    return venues
            else:
                print("That isn't on the list of options. Try again.")
            input("Done reading?: ")
        except:
            print("That's not an integer. Try again.")
            input("Done reading?: ")


# Matthew McKinley, Time Management

currentTimes = ()
currentTimeframes = []
schedule = []

clearTimeframes = []

performances = []
unclearTimeframes = []

days = 0
dayCount = 0

# Prints out filled time frames with the performances happening then 
def print_timetable():
    for timeFrame in unclearTimeframes:
        performance = performances[unclearTimeframes.index(timeFrame)]

        print(f"{timeFrame} - {performance['Artist']['name']}'s {performance['Artist']['genre']} performance")

def update_current_times(timeframes, startTime, endTime):
    # timeframes is half hour segments
    # timeframeCount is a countable version of timeframes

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

# Darius Vaiaoga, Artist Management 

artist_list = []

def print_artists():
    if artist_list != []:
        for artist in artist_list:
            for property in artist:
                print(f'{property.capitalize()}: {artist[property]}')
    else:
        input('Sorry, there seems to be no artists!')
    

def add_artist():

    prompts = ['Who is the artist? ', 'What genre is the performance? ', 'How long will the performance go (in 30 minute blocks)? ']
    sample_artist = {'name': '', 'genre': ''}

    i = 0

    # Get property value from user per property
    for property in sample_artist:
        sample_artist[property] = input(prompts[i])
        i += 1
            
    artist_list.append(sample_artist)

def get_artist():

    # Get all lowercase artist names
    artist_names = []
    for artist in artist_list:
        artist_names.append(artist['name'].lower())

    print_artists()

    selected_artist = input('Which artist do you select? ').lower()

    if selected_artist in artist_names:
        for artist in artist_list:  
            if artist['name'].lower() == selected_artist:
                return artist_list.index(artist)
    
def remove_artist():
    artist_list.remove(artist_list[get_artist()])

# Prompts the user to modify a artist by providing them with what they can modify, then modifies that property by how they request
def modify_artist():
    
    # Get the artist to modify
    try:
        artist = artist_list[get_artist()]
    except:
        input("Couldn't find artist")
        return None
    properties = []

    # Get all properties of artists
    for property in artist:
        properties.append(property)

    prop_to_mod = input("What property do you want to modify? ").lower()

    if prop_to_mod != 'name' or 'genre':
        input("That property doesn't exist")
        return None

    # Ask user what they want to change the property to. If the property is the performance duration, convert answer to integer
    try:
        if prop_to_mod != "performance_duration":
            artist[prop_to_mod] = input(f'What do you want to change "{prop_to_mod.capitalize()}" to? ')
        else:
            artist[prop_to_mod] = int(input(f'What do you want to change "{prop_to_mod.capitalize()}" to? '))
    except:
        input('Invalid Input')
        return None

# Darius Vaiaoga, Search Functions

search_list = []

# Combines artist list, venue list, and ticket lists by seperating each entry in each list by type
def create_search_list():
    search_list.clear()

    for artist in artist_list:
        search_list.append({'Type': 'Artist', 'info': artist})

    # Seperates Venues, from stages, from equipment, in search list
    for venue in venues:
        search_list.append({'Type': 'Venue', 'info': venue})
        for stage in venue['stage']:
            search_list.append({'Type': 'Stage', 'info': stage})
            for equipment in stage['equipment']:
                search_list.append({'Type': 'Equipment', 'info': equipment})

    
            
def print_result(result):
    for property in result:
        print(f'{property.capitalize()}: {result[property]}')

def search():
    query = input('What do you want to search for? ').lower()
    create_search_list()

    for item in search_list:
        match item['Type']:
            case 'Artist':

                # Checks if first two letters of artist name is the same as the first two letters of the query
                if [item['info']['name'][0].lower(), item['info']['name'][1].lower()] == [query[0], query[1]]:
                    print('Artist:')
                    print_result(item['info'])
            case 'Venue':

                # Checks if first two letters of venue name is the same as the first two letters of the query
                if [item['info']['name'][0].lower(), item['info']['name'][1].lower()] == [query[0], query[1]]:

                    print('Venue:')
                    display_venues([item['info']])

            case 'Stage':
                
                if [item['info']['name'][0].lower(), item['info']['name'][1].lower()] == [query[0], query[1]]:

                    # Print Stage's name and equipment
                    print('Stage:')
                    print(f'Stage Name: {item['info']['name']}')
                    for equipment in item['info']['equipment']:
                        print(f"\t{equipment['count']} {equipment['name']}s")

            case 'Equipment':

                if [item['info']['name'][0].lower(), item['info']['name'][1].lower()] == [query[0], query[1]]:

                    # Print equipment's name and
                    print('Equipment:')
                    print(f"\t{item['info']['count']} {item['info']['name']}s")            

# Jonas Fairchild, Master display and Main function

def display_all(): #Uses a combination of display functions from every part of the code to display everything imaginable.
    print("---------- Artists ----------\n")
    print_artists()
    print("\n---------- Schedule ----------\n")
    print("\n---------- Venues ----------\n")
    display_venues(venues)
    print("\n---------- Tickets/attendees ----------\n")

    input('Done Reading? ')

def time_menu():
    while True:
        print('"---------- Time ----------')
        match input('What do you want to do with time? \n1. See Time Table \n2. Modify Festival Hours \n3. Set Performances \n6. Go Back'):
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
        print('---------- Artists ----------')
        match input('What do you want to do with the artists? \n1. See Artists \n2. Add Artist \n3. Remove Artist \n4. Modify Artist \n5. Go Back \n'):
            case '1':
                print_artists()
            case '2':
                add_artist()
            case '3':
                remove_artist()
            case '4':
                modify_artist()
            case '5':
                main()
                break
            case _:
                input('Invalid Input')
                

def main(): #Provides a UI that branches to every part of the program, allowing modification of everything.
    while True:
        choice = input("What do you want to do?\n1. Manage artists\n2. Manage schedule\n3. Manage venues\n4. Manage ticket sales/attendees\n5. Display everything\n6. Search\n7. Exit program\n")
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
            search()
        elif choice == '7':
            break
        else:
            print("That isn't on the list of options. Try again.")

main()