ean_number = str(input("Podaj nr ean: "))
if ean_number[0:3] == "590" and len(ean_number) == 13:
    print("z polski prawid")
elif len(ean_number) == 13:
    print("prawidłowo")
else:
    print("zle")
print(ean_number[0:3])