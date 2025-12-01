arr = [1,2,3,4,5,6,7,8,9]
subset_arr = [5,3,1,8]

if all(subset_arr[n] in arr for n in range(len(subset_arr))):
    print("yes yes")
else:
    print("no no no")