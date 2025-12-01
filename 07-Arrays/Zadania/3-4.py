arr = [-15,8,-31,47,-2,19]
max = arr[0]
min = arr[0]
i = 0
for n in arr:
    if n > max:
        max = arr[i]
    if n < min:
        min = arr[i]
    i += 1

print(max)
print(min)



