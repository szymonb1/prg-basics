import queue
def f(rpn):
    stack = queue.LifoQueue()
    for char in rpn:
        if not char in "+-*/=":
            stack.put(char)
        elif char in "+-*/":
            a, b = stack.get(), stack.get()
            temp_exp = f"{b}{char}{a}"
            stack.put(str(eval(temp_exp)))
        elif char == "=":
            return stack.get()

print(f("831+/32-4+*="))