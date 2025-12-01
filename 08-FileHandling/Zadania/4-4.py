x=5

try:    
    with open(r"prg-basics\08-FileHandling\it_company.csv", 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("nie istnieje")
content = content.splitlines()


def czytaj(x):
    for num in range(x-4,x+1):
        print(content[num])
while True:
    if x == 5:
        czytaj(x)
        x += 5
    cont = str(input("Kontynuować? (enter/nie)"))
    if cont == "":
        czytaj(x)
        x += 5
    else:
        break



