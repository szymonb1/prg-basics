file_path=r"C:\Users\turni\Desktop\programowanie\prg-basics\prg-basics\08-FileHandling\Zadania\liczby.txt"
def oblicz(x):
    list = [str(pow(x,n)) for n in range(1,4)]
    return list


try:
    with open(file_path, 'a') as f:
        for n in range(1, 101):
            text = ",".join(oblicz(n))
            f.write(text)
            f.write("\n")
except FileNotFoundError:
    print("nie ma takiego pliku")


