dec_num = int(input("Podaj liczbe w dec: "))
remainder = []
while dec_num !=0:
    remainder.append(int(dec_num%2))
    print(remainder)
    dec_num = int(dec_num/2)
for x in range(len(remainder), 0, -1):
    print(remainder[x-1], end = '')


