#Music Festival Management System

# Darius Vaiaoga, Artist Management

artist_list = [{'name': 'Eminem', 'genre': 'Rap'}]

heheheha = []

def print_artist(dictionary):
    for property in dictionary:
        print(f'{property.capitalize()}: {dictionary[property]}')


def add_artist(dictionary, prompts):
    i = 0
    for property in dictionary:
        try:
            dictionary[property] = input(prompts[i])
            i += 1
        except:
            print('Invalid Input')
            return None
        
    artist_list.append(dictionary)

def get_artist():
    artist_names = []

    for artist in artist_list:
        artist_names.append[artist['name'].lower()]
        print_artist(artist)

    selected_artist = input('Which artist do you select?').lower()

    # If there is an artist of the name the user inputted, go through every artist again to find that artist, then return that artist.
    if selected_artist in artist_names:

        for artist in artist_list:

            if artist['name'] == selected_artist:
                return artist

# Prompts the user to modify a artist by providing them with what they can modify, then modifies that property by how they request
def modify_artist(artist):
    properties = []

    print_artist(artist)
    for property in artist:
        properties.append(property)

    prop_to_mod = input("What property do you want to modify? ").lower()

    if prop_to_mod in properties:
        try:
            artist[prop_to_mod] = input(f'What do you want to change "{prop_to_mod.capitalize()}" to? ')
        except:
            print('Invalid Input')
            return None
    
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
        print("That's not a valid input. Try again.")
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
            print("Invalid input. Try again.")
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
            print("Invalid input. Try again.")
        venue = next((v for v in venues if v['name'].lower() == venue_choice.lower()), []) #Specifies the venue that the name references
        
        while True:
            print("Which stage has equipment lists you want to modify?")
            for i, stage in enumerate(venue["stage"], start = 1):
                print(f"{i}. {stage['name']}")
            stage_choice = input().lower()
            if any(s["name"].lower() == stage_choice for s in venue["stage"]):
                break
            print("Invalid input. Try again.")
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
                    print("Invalid input. Try again.")

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

def display_venues(): #Shows all venues in an organized manner.
    for venue in venues:
        print(f"{venue['name']}:")
        for stage in venue['stage']:
            print(f"\t{stage['name']}:")
            for equipment in stage['equipment']:
                print(f"\t\t{equipment['count']} {equipment['name']}s")

def venue_management(): #A sort of sub-main function that contains a user interface for this smaller part of the program.
    while True:
        try:
            os.system("cls")
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
                return venues
            else:
                print("Invalid input. Try again.")
        except:
            print("Invalid input. Try again.")

# Matthew McKinley, Time Management
currentTimes = ()
currentTimeframes = []
schedule = []

days = int(input("How many days are you going to have the festival be? :"))
dayCount = 0

def updateCurrentTimes(timeframes, startTime, endTime):
    timeframeCount = timeframes
    timeNow = startTime
    timeNowHour = startTime

    currentTimes = currentTimes + timeNow
    currentTimes = currentTimes + timeNowHour


    while timeNow <= endTime:
        remainder = timeframeCount % 2
        if remainder == 1:
            timeNowHour = timeNowHour + 1
        elif remainder == 0:
            timeNow = timeNow + .30

if days >= dayCount:
    start = float(input("What time does the performance start? (Minutes are after a decimal point, ex. 10.30)"))
    end = float(input("What time does the performance end? (Minutes are after a decimal point, ex 12.30)"))
    timeframes = end - start
    timeframes = timeframes / 2
    currentTimeframes = currentTimeframes + timeframes
    updateCurrentTimes()
