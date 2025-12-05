hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

def hotel_list(hotels):
    name_list = []
    for hotel in hotels:
        name_list.append(hotel["name"])
    return name_list

def avg_price(hotels):
    price_sum = 0
    for hotel in hotels:
        price_sum += hotel["price"]
    avg_price= price_sum / len(hotels)
    return avg_price

print("hotels in krakow: ", hotel_list(hotels_in_Krakow))
print("hotels in krakow: ", hotel_list(hotels_in_Sopot))
