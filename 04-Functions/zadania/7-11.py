def f(*args):
    
    list = (args)
    return True if any(n<0 for n in list) else False

def main():
    print(f(0,9,0))
if __name__ == "__main__":
    main()