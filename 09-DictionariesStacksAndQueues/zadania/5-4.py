paragraph = "cat dog mouse cat rat cat mouse"
paragraph = paragraph.split()
quantity = {

}

for word in paragraph:
    if not word in quantity.keys():
        quantity[word] = 1
    else:
        quantity[word] += 1

print(quantity)