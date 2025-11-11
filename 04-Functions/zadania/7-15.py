def f(detector):
    number_of_people = sum(n == "+" for n in detector)
    return True if number_of_people >=3 else False
print(f("--+--------------+"))