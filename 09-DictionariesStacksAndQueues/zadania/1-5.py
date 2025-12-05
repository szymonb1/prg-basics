countries = [
{"name":"Poland", "population":38000000},
{"name":"Poland2", "population":5000000},
{"name":"Poland3", "population":78000000},
{"name":"Poland4", "population":18000000},
{"name":"Poland5", "population":98000000},
]

print("COUNTRY POPULATION")
for dict1 in countries:
    name = dict1["name"]
    pop = dict1["population"]
    print(name, pop)