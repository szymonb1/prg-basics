import random
arr = [random.randint(0, 10) for x in range(10)]
print(arr)
arr_even = []
arr_odd = []
for n in arr:
    if n%2 == 0:
        arr_even.append(n)
    else:
        arr_odd.append(n)
arr_even.extend(arr_odd)
print(arr_even)