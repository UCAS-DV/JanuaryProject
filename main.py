# Music Festival Management System

# Tuple of times of in standard notation
currentTimes = ()
currentTimeframes = []

schedule = ()

artist_list = [{'name': 'Eminem', 'genre': 'Rap', 'start': 10.30, 'end': 11.30}]

days = int(input("How many days are you going to have the festival be?:"))

def PrintDict(dictionary):
    for item in dictionary:
        print(f'{item.capitalize()}: {dictionary[item]}')

PrintDict(artist_list[0])