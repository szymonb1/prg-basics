def f(number):
    number = str(number)
    sum = 0
    for n in number:
        list_of_numbers = [x for x in number]
        list_of_numbers.remove(n)
        sum += int(n) if any(x == n for x in list_of_numbers) else 0
    print(sum)
f(513553007)