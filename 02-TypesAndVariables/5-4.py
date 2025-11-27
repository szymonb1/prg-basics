amount = float(input("podaj ilość: "))
vat = 0.23

vatamount = round(amount * vat, 2)
amount_after_tax = round(amount + amount * vat, 2)

print(f'Amount: {amount}\nVAT 23%: {vatamount} ')