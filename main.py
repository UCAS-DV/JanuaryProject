# Music Festival Management System

artist_list = [{'name': 'Eminem', 'genre': 'Rap'}]

def print_dict(dictionary):
    for property in dictionary:
        print(f'{property.capitalize()}: {dictionary[property]}')

def add_dict(dictionary, target_list, prompts):
    i = 0
    for property in dictionary:
        try:
            dictionary[property] = input(prompts[i])
            i += 1
        except:
            print('Invalid Input')
            return None
        
    target_list.append(dictionary)

# Prompts the user to modify a dictionary by providing them with what they can modify, then
def modify_dict(dictionary):
    properties = []

    print_dict(dictionary)
    for property in dictionary:
        properties.append(property)

    prop_to_mod = input("What property do you want to modify? ").lower()

    if prop_to_mod in properties:
        try:
            dictionary[prop_to_mod] = input(f'What do you want to change "{prop_to_mod.capitalize()}" to? ')
        except:
            print('Invalid Input')
            return None
        
add_dict({'name': '', 'genre': 'rap'}, artist_list, ['Who is the artist? ', "What genre is the artist's performance? "])
add_dict({'name': '', 'genre': 'rap'}, artist_list, ['Who is the artist? ', "What genre is the artist's performance? "])

for artist in artist_list:
    print_dict(artist)

modify_dict(artist_list[1])

for artist in artist_list:
    print_dict(artist)