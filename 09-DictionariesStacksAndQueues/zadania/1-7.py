products = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}
sum = 0
for name, quantity in products.items():
    print(name, quantity)
    sum += quantity
print(f"suma to: {sum}")