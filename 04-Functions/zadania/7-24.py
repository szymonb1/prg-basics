import operator
import re
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,

}

def f(expression):
    """operation_result = 0
    for x in range(0, len(expression), 2):
        try: 
            operand = expression[x+1]
        except:
            break
        if x>0:
            com1 = operation_result
        else:
            com1 = int(expression[x])
        com2 = int(expression[x+2])
        operation_result = ops[operand](com1, com2)
    print(operation_result)
            
    """
    print(eval(expression))


def main():
    f("3+8-1+2+6/5")


if __name__ == "__main__":
    main()