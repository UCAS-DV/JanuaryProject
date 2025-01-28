# Music Festival Management System

# Tuple of times of in standard notation
currentTimes = ()
currentTimeframes = []

schedule = ()

artist_list = [{'name': 'Eminem', 'genre': 'Rap', 'start': schedule[9], 'end': 11.30}]

days = int(input("How many days are you going to have the festival be?:"))

def ListArtists():
    for artist in artist_list:
        print(f'Name: {artist['name']}')
        print(f'Genre: {artist['genre']}')

ListArtists()