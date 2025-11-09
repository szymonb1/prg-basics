amount = int(input("Podaj ile zl: "))
amount5pln = 0
amount2pln = 0
amount1pln = 0

amount5pln = amount//5
amount = amount%5
amount2pln = amount//2
amount = amount%2
amount1pln = amount

print(f"5 PLN coins: {amount5pln}")
print(f"2 PLN coins: {amount2pln}")
print(f"1 PLN coins: {amount1pln}")