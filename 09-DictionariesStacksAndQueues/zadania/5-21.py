import json
favourite_book = {
    'author': 'Albert Camus',
    'genre': 'Philosophical novel',
    'release year': 1942,
    'original language': 'French',
    'number of words': 42000
}

with open(r'09-DictionariesStacksAndQueues\zadania\favourite.json', 'w') as f:
    json.dump(favourite_book, f)
