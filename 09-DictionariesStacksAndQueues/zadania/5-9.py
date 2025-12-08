import csv
file_path = r"09-DictionariesStacksAndQueues\vehicle.txt"
file_path2 = r"09-DictionariesStacksAndQueues\province.csv"
ilosc = {

}


with open(file_path2, "r", encoding="utf-8") as f:
    for row in csv.reader(f):
        ilosc[row[0]] = 0
    del ilosc["Letter"]

with open(file_path, 'r') as f:
    for plate in f:
        ilosc[plate[0]] += 1

print(ilosc)