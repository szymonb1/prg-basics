arr = [x for x in range(20)]

chosen_number = int(input("Podaj numerek: "))

for n in range(chosen_number+1, len(arr)+1):
    print(n, end=" ")