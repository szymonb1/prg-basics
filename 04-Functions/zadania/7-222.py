def f(name):
    acronym = name[0]
    for n in range(len(name)):
        if name[n-1] == " ":
            acronym += name[n]
        else:
            pass
    print(acronym)

f("Internet of Things")
