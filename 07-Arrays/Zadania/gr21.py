def f(id):
    id = str(id)
    if len(id) != 16:
        return "erorr"
    return id[::2]


print(f(1234567896234567))