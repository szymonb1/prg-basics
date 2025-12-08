import csv
data_list = []
filename = r"08-FileHandling\clothing.csv"
with open(filename, 'r') as f:
    fread = csv.DictReader(f)
    for row in fread:
        data_list.append(row)


for data in data_list:
    if float(data["Price"]) < 60 and float(data["Stock_Quantity"]) < 40:
        for x in data.values():
            print(x, end=" ")
        print()