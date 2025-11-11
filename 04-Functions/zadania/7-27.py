def f(product_code):
    if sum(int(x) for x in product_code[:-1])%7 == int(product_code[3]):
        return True
    else:
        return False
print(f("2035"))