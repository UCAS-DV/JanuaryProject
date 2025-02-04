#This is he actual program, use this one
#use sets
#TIP!!!!!
#If you right-click the Pseudocode file > Open to the side, it will show both this and the Pseudocode file at the same time!

#Variable for repeats
rept = 1


import random
#Schedule variables
tmes = ("09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00")
ven1 = ("09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00")
ven2 = ("09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00")
ven3 = ("09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00")
ven4 = ("09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00")
artist_list=["None-None-None"]
attendees = ["None-None"]
venus={"None-None"}
price_one = 100
price_three = 250
price_vip = 450


def venu(amount, venus, rept): #amount is how many venu slots you want
    #{venue,venue2}
    try:
        choice=input(f"""Press the number of the option you want
        1. Add new venus (Note: there can only be {amount} total venus)
        2. Remove venue
        3. View venu list 
        4. Exit
""")
        if choice=="1": #add new venu
            if len(venus)>=amount:
                print("All venu slots are full")
                rept = 1
                return amount, venus, rept
            else:
                name=input("What is the venu name?\n    ")
                location=input("Where is the location?\n    ")
                venus.append({name,location})
                rept = 1
                return amount, venus, rept

        elif choice=="2": #remove venu
            name=input("What is the venu name?\n    ")
            gone=True
            for x in venus:
                if name in venus[x]:
                    venus.remove(x)
                    gone=False
                    rept = 1
                    return amount, venus, rept
                else:
                    rept = 1
                    return amount, venus, rept
            if gone==True:
                print("Item not in venu list")
                rept = 1
                return amount, venus, rept

        elif choice=="3":
            for x in venus:
                print(x)
                return amount, venus, rept

        else: #exit
            rept = 1
            return amount, venus, rept
    except:
        print("Invalid option")
        rept = 1
        return amount, venus, rept

#Schedule variables

def ticket_attendee_guest(attendees, rept, price_one, price_vip, price_three):
    while True:
        choice = input("""What would you like to do?
        1. See ticket prices
        2. Buy ticket
""")
        if choice == "1":
            print("The price for a 1-day pass is $", price_one, ", the price for a 3-day pass is $", price_three, ", the price for a VIP pass is $", price_vip)
            return attendees, rept, price_one, price_vip, price_three
        elif choice == "2":
            ans = input("What is your name?\n    ")
            ask = input("What pass do you want? One, Three, or VIP?\n    ")
            if ask == "One":
                ask = "One-day-pass"
                pass
            elif ask == "Three":
                ask = "Three-day-pass"
                pass
            elif ask == "VIP":
                ask = "VIP-pass"
            attendees.append(f"{ans}, {ask}")
            return attendees, rept, price_one, price_vip, price_three


def ticket_attendee(attendees, rept, price_one, price_vip, price_three):
    while True:
        choice = input("""What would you like to do?
        1. See ticket prices
        2. Adjust ticket prices
        3. Add attendee information
        4. Attendee information list
        5. End
""")
        if choice == "1":
            print("The price for a 1-day pass is $", price_one, ", the price for a 3-day pass is $", price_three, ", the price for a VIP pass is $", price_vip)
            return attendees, rept, price_one, price_vip, price_three
        elif choice == "2":
            choice = input("""What would you like to change?
        1. Change the 1-day pass price
        2. Change the 3-day pass price
        3. Change the VIP pass price
        4. Exit
""")
            if choice == "1":
                choice = float(input("What would you like to change the price to?\n    "))
                price_one = choice
                return attendees, rept, price_one, price_vip, price_three
            elif choice == "2":
                choice = float(input("What would you like to change the price to?\n    "))
                price_three = choice
                return attendees, rept, price_one, price_vip, price_three
            elif choice == "3":
                choice = float(input("What would you like to change the price to?\n    "))
                price_vip = choice
                return attendees, rept, price_one, price_vip, price_three
            else:
                return attendees, rept, price_one, price_vip, price_three
        elif choice == "3":
            nme = input("Attendee name?\n    ")
            typ = input("What type of pass?\n    ")
            schedule = schedule.append([nme, typ])
            return attendees, rept, price_one, price_vip, price_three
        elif choice == "4":
            print(attendees)
            return attendees, rept, price_one, price_vip, price_three
        else:
            return attendees, rept, price_one, price_vip, price_three


def artists(rept, artist_list): #lists
    #list format: name,genre
    choice=input("""Press the number of what you want:
        1. Add an artist
        2. Remove an artist
        3. Edit artists
        4. See artists
        5. Exit
""")
    if choice=="1":#add
        artist=input("Artist Name?\n    ")
        genre=input("Genre of the artist?\n    ")
        ven=input("Venu performing at?\n    ")
        artist_list.append(f"{artist}-{genre}-{ven}")
        rept = 1
        return rept, artist_list
        
    elif choice=="2": #remove
        print(artist_list)
        ans = input("What position in the list is it?\n    ")
        cnt = 0
        for x in enumerate(artist_list):
            cnt += 1
            if "cnt" == ans:
                artist_list.remove(x)
                print(artist_list)
        return rept, artist_list

    elif choice=="3": #Edit Artists
        print(artist_list)
        ans = input("What position in the list is it?\n    ")
        cnt = 0
        for x in enumerate(artist_list):
            cnt += 1
            if "cnt" == ans:
                artist_list.remove(x)
                print(artist_list)
                pass
        artist=input("Artist Name?\n    ")
        genre=input("Genre of the artist?\n    ")
        ven=input("Venu performing at?\n    ")
        artist_list.append(f"{artist}-{genre}-{ven}")
        rept = 1
        return rept, artist_list
        
    elif choice=="4": #See artists
        print(artist_list)
        return rept, artist_list
    
    else: #Exit
        rept = 1
        return rept, artist_list



#The randomised still broken
def schedule(tmes, ven1, ven2, ven3, ven4, rept, artist_list):
    ans = input('''What would you like to do?
        1 Remove artist from schedule
        2 Add artist to empty slot
        3 See schedules
        4 Menu
''')
    '''
    if ans == 1:
        #This will add times and sechdule timing to a venu slot
        lst = []
        lst1 = []
        ans = input("What venu would you like to make the schedule for?\n   ")
        count = 0
        countlst = len(tmes)
        for x in artist_list:
            if ans in x:
                lst.append(x)
                count += 1
            else:
                pass
        if count > countlst:
            return tmes, ven1, ven2, ven3, ven4, rept, artist_list, ("The amount of artists is too much for the amount of time slots")
        else:
            lst3 = lst[:]
            random.shuffle(lst3)
            lst = lst3
            for x in lst:
                for i in tmes:
                    lst1 = lst1.append(i + x)
            print(f"Venu #1:\n{ven1}\nVenu #2:\n{ven2}\nVenu #3:\n{ven3}\nVenu #4:\n{ven4}\n")
            ans = int(input("Which venu SLOT do you want to save this schedule to? (5 for none)\n    "))
            if ans == 1:
                ven1 = tuple(lst1)
            elif ans == 2:
                ven2 = tuple(lst1)
            elif ans == 3:
                ven3 = tuple(lst1)
            elif ans == 4:
                ven4 = tuple(lst1)
            else:
                print("Not saved to a slot")
            return tmes, ven1, ven2, ven3, ven4, rept, artist_list
    '''
    if ans == "1":
        #This is to delete a time slot, need to work on making the times back into the list
        #Fix is the list that will be saved to the venu
        ask = input("What venu slot would you like to access? (1-4)\n    ")
        if ask == "1":
            fix = list(ven1)
            print(fix)
            ans = input("What item would you like to remove? (Don't do times, only the artist)\n    ")
            for i, x in enumerate(fix):
                if ans in x:
                    fix[i] = x.replace(f", {ans}", "")
                    print(fix)
                    pass
            ven1 = tuple(fix)
            pass
        elif ask == "2":
            fix = list(ven2)
            print(fix)
            ans = input("What item would you like to remove? (Don't do times, only the artist)\n    ")
            for i, x in enumerate(fix):
                if ans in x:
                    fix[i] = x.replace(f", {ans}", "")
                    print(fix)
                    pass
            ven2 = tuple(fix)
            pass
        elif ask == "3":
            fix = list(ven3)
            print(fix)
            ans = input("What item would you like to remove? (Don't do times, only the artist)\n    ")
            for i, x in enumerate(fix):
                if ans in x:
                    fix[i] = x.replace(f", {ans}", "")
                    print(fix)
                    pass
            ven3 = tuple(fix)
            pass
        elif ask == "4":
            fix = list(ven4)
            print(fix)
            ans = input("What item would you like to remove? (Don't do times, only the artist)\n    ")
            for i, x in enumerate(fix):
                if ans in x:
                    fix[i] = x.replace(f", {ans}", "")
                    print(fix)
                    pass
            ven4 = tuple(fix)
            pass
        else:
            print("Not an available slot")
        return tmes, ven1, ven2, ven3, ven4, rept, artist_list
    #This is the adding function, need to fix the slot they need to add to
    elif ans == "2":
        ask = input("What venu slot would you like to access? (1-4)\n   ")
        if ask == "1":
            fix = list(ven1)
            print(fix)
            ask = input("What time would you like to add this to?\n    ")
            ans = input("What would you like to add?\n    ")
            for i, x in enumerate(fix):
                if ask in x:
                    fix[i] += f", {ans}"
                    print(fix)
                    pass
            ven1 = tuple(fix)
            return tmes, ven1, ven2, ven3, ven4, rept, artist_list
        elif ask == "2":
            fix = list(ven2)
            print(fix)
            ask = input("What time would you like to add this to?\n    ")
            ans = input("What would you like to add?\n    ")
            for i, x in enumerate(fix):
                if ask in x:
                    fix[i] += f", {ans}"
                    print(fix)
                    pass
            ven2 = tuple(fix)
            return tmes, ven1, ven2, ven3, ven4, rept, artist_list
        elif ask == "3":
            fix = list(ven3)
            print(fix)
            ask = input("What time would you like to add this to?\n    ")
            ans = input("What would you like to add?\n    ")
            for i, x in enumerate(fix):
                if ask in x:
                    fix[i] += f", {ans}"
                    print(fix)
                    pass
            ven3 = tuple(fix)
            return tmes, ven1, ven2, ven3, ven4, rept, artist_list
        elif ask == "4":
            fix = list(ven4)
            print(fix)
            ask = input("What time would you like to add this to?\n    ")
            ans = input("What would you like to add?\n    ")
            for i, x in enumerate(fix):
                if ask in x:
                    fix[i] += f", {ans}"
                    print(fix)
                    pass
            ven4 = tuple(fix)
            return tmes, ven1, ven2, ven3, ven4, rept, artist_list
        else:
            return tmes, ven1, ven2, ven3, ven4, rept, artist_list, ("Invalid input!")
    elif ans == "3":
        ask = input("What venu slot would you like to access? (1-4)\n    ")
        if ask == "1":
            print(ven1)
            pass
        elif ask == "2":
            print(ven2)
            pass
        elif ask == "3":
            print(ven3)
            pass
        elif ask == "4":
            print(ven4)
            pass
        else:
            pass
        return tmes, ven1, ven2, ven3, ven4, rept, artist_list
    else:
        return tmes, ven1, ven2, ven3, ven4, rept, artist_list


def search(rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus):
    ans = input('''What would you like to do?
        1 for attendees
        2 for venu
        3 for artists
        4 for schedule
        5 for end
''')
    #Searches for attendee by name
    if ans == "1":
        atnd = input("What is the attendee name?\n    ")
        if atnd in attendees:
            print(f"{atnd} is in the list!")
            rept = 1
            return rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus
        else:
            print(f"{atnd} not in the list!")
            rept = 1
            return rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus
    #Searches for venu by name of venu
    elif ans == "2":
        ven = input("What is the name of the venu?\n    ")
        if ven in venus:
            print(f"{ven} in the list!")
            rept = 1
            return rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus
        else:
            print(f"{ven} not in the list!")
            rept = 1
            return rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus
    #Searches for artist by name
    elif ans == "3":
        art = input("What is the artist's name?\n    ")
        if art in artist_list:
            print(f"{art} in the list!")
            rept = 1
            return rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus
        else:
            print(f"{art} not in list!")
            rept = 1
            return rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus
    #Prints the schedule
    elif ans == "4":
        ans = input("What slot of venu schedule would you like to access? (1-4)\n    ")
        if ans == "1":
            print(ven1)
            pass
        elif ans == "2":
            print(ven2)
            pass
        elif ans == "3":
            print(ven3)
            pass
        elif ans == "4":
            print(ven4)
            pass
        else:
            print("Invalid input!")
            pass
        rept = 1
        return rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus
    #Ends the function and returns to menu
    else:
        rept = 1
        return rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus



def main(rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus, price_one, price_three, price_vip, tmes):
    while rept > 0:
        ans = input("\n\nWhat is the password for admin? (ADMIN is default)\n    ")
        if ans == "ADMIN":
            choice = input("""        1. Artist Management
        2. Schedule Management
        3. Venue Management
        4. Ticket Sales and Attendee Management
        5. Search
        6. End
Enter the number of the thing you would like to do:
""")
            if choice == "1":
                rept, artist_list = artists(rept, artist_list)
            elif choice == "2":
                tmes, ven1, ven2, ven3, ven4, rept, artist_list = schedule(tmes, ven1, ven2, ven3, ven4, rept, artist_list)
            elif choice == "3":
                rept, venus = venu((int(input("How many venus would you like to make?\n    "))), venus, rept)
            elif choice == "4":
                attendees, rept, price_one, price_vip, price_three = ticket_attendee(attendees, rept, price_one, price_vip, price_three)
            elif choice == "5":
                rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus = search(rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus)
            else:
                rept = 0
        else:
            choice = input("""        1. Search
        2. Ticket sales
Enter the number of the thing you would like to do:
""")
            if choice == "1":
                rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus = search(rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus)
            elif choice == "2":
                attendees, rept, price_one, price_vip, price_three = ticket_attendee_guest(attendees, rept, price_one, price_vip, price_three)
    return rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus, price_one, price_three, price_vip

# loop that makes sure the program continues until the user is done
while rept > 0:
    print("Music Festival Manager")
    rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus, price_one, price_three, price_vip = main(rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus, price_one, price_three, price_vip, tmes)
print("Thank you for using this program.")