import re
def f(name):
    first_letters = re.findall("\s([a-zA-Z])", name)
    first_letters.insert(0, name[0])
    for x in first_letters:
        print(x, end='')
f("Internet of Things")

