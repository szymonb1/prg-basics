price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
sum = 0
for product, price in price_list.items():
    discount_price = round(price*0.9,2)
    print(f"{product}, {price}, {discount_price}")
    sum += discount_price
print("suma", round(sum, 2))