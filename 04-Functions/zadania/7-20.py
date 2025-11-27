def f(n):
    number = n
    if number != 0 and number != 1:
        return "" if any(number%x==0 for x in range(2, n)) else number
def main():
    for x in range(20):
        if f(x) != None:
            print(x, end=" ")

if __name__ == "__main__":
    main()