import re

def f(name):
    letters = re.findall(r"\b[A-Za-z]",name)
    print(letters)
    acronym = ""
    for letter in letters:
        acronym += letter
    return acronym


if __name__ == "__main__":
    print(f("For Your Information"))