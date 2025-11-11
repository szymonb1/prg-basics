
def check_if_binary(number):
    print("liczba jest binarna" if all(n in "01" for n in number) else "liczba nie jest binarna")
def main():
    check_if_binary("10101010100")
if __name__ == "__main__":
    main()