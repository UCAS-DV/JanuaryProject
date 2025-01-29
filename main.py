#Music Festival Management System

#Venue Management (Jonas Fairchild)
import os
venues = {}

def venue_modify(): #Handles the modification for all venues.
    venues = list(venues)
    choice = input("Do you want to add or remove a venue?: ").lower()
    if choice == "remove":
        if venues != []:
            print("Which venue do you want to remove?")
            count = 1
            for venue in venues:
                print(f"{count}. {venue[0]}", end = "\n")
            removal = input().lower()
            for venue in venues:
                if venue[0].lower() == removal:
                    return set(venues.remove(venue))
            else:
                print("That isn't on the list of venues.")
                return set(venues)
        else:
            print("There are no venues to remove.")
            return set(venues)
    elif choice == "add":
        venue_name = input("What is the name of your new venue?: ")
        return set(venues.add([[venue_name, []]]))
    else:
        print("That's not a valid input. Try again.")
        venue_modify()



currentTimes = ()
currentTimeframes = []

days = int(input("How many days are you going to have the festival be? :"))

def updateCurrentTimes():
    pass
