import json

# Read the contents of the json file
with open(r"09-DictionariesStacksAndQueues\zadania\voting.json", "r") as f:
    content = json.load(f)

# Vote for a person
person_name = input('Name of the person you are voting for (jakub/szymek): ')
content[person_name] += 1

with open(r"09-DictionariesStacksAndQueues\zadania\voting.json", "w") as f:
    json.dump(content, f)

