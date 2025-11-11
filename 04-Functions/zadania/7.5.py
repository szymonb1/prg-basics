


def check_if_in_range(n, x, y):
    if n in range(x, y):
        return True
    else:
        return False
def main():
    if check_if_in_range(16, 2, 16):
        print("true")
    else:
        print("nope")


if __name__ == "__main__":
    main()
