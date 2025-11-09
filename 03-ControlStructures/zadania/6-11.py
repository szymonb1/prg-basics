current_price = float(input("current price: "))
before_discount_price = float(input("before discount: "))
price_reduced_in_percentage = (before_discount_price - current_price)/before_discount_price
percentage = "{:.2%}".format(price_reduced_in_percentage)
print(percentage)