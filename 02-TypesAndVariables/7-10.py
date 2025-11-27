import random
computer_throw = random.randint(1, 6)
user_guess = int(input("Podaj numer: "))
if user_guess == computer_throw:
    print(f'Zgadłeś! Liczbą rzuconą przez komputer jest {computer_throw}')
else:
    print(f'Nie zgadłeś! Liczbą rzuconą przez komputer jest {computer_throw}')
