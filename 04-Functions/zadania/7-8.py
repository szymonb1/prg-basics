def f(number, even):
    number = str(number)
    sum = 0
    if even:
        for n in number:
            sum +=int(n) if int(n)%2 == 0 else 0
    elif not even:
        for n in number:
            sum +=int(n) if int(n)%2 != 0 else 0
    else: return sum
    return sum




def main():
    print(f(4789, False))

if __name__ == "__main__":
    main()