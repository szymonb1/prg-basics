import csv
filename = r"08-FileHandling\it_company.csv"
rows = []
with open(filename, 'r') as f:
    fread = csv.DictReader(f)
    for row in fread:
        rows.append(row)
print("GRAPIC DESIGNERS")
print("="*10)
for row in rows:
    
    print(row["First Name"], row["Last Name"]+","+row["Email"])
for x in rows[0].keys():
    print(x, end=" ")