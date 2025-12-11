import json

with open(r"09-DictionariesStacksAndQueues\reservations.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    data = data['reservations']



sum_of_paid= 0
sum_of_unpaid = 0
count_paid = 0
for dic in data:
    if dic['paid'] == True:
        count_paid += 1
        sum_of_paid += dic['nights'] * dic['price_per_night']
    elif dic['paid'] == False:
        sum_of_unpaid += dic['nights'] * dic['price_per_night']
    

unpaid_amount = len(data) - count_paid



print(len(data))
print(count_paid)
print(unpaid_amount)
print(sum_of_paid)
print(sum_of_unpaid)
