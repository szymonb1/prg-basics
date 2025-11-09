hours_amount = int(input("Podaj liczbe godzin: "))
if hours_amount >= 1 and hours_amount <= 2:
    print("Cena 5pln")
elif hours_amount >= 3 and hours_amount <= 6:
    print("Cena 15pln")
elif hours_amount > 6:
    print("Cena 20pln")
else:
    print("błąd")