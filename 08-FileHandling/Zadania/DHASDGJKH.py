import random
ListaMiesiecy = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj',
'czerwiec', 'lipiec', 'sierpień', 'wrzesień', 'październik',
'listopad', 'grudzień']
ListaPlac = [random.randint(1,10000) for x in range(12)]

slownik = {}

x = dict(zip(ListaMiesiecy, ListaPlac))
print(x)

srednia = sum(ListaPlac) / len(ListaPlac)

for key, value in x.items():
    if value > srednia:
        print(key)




