def input_string(message):
    x = input(message)
    return x

def input_integer(message):
    x = int(input(message))
    return x

def input_real(message):
    x = float(input(message))
    return x

def input_boolean(message):
    if message == "y":
        x = True
    elif message == "n":
        x= False
    else:
        print("nieprawidlowy")
    return x