import queue
def reverser(sztring):
    stack = queue.LifoQueue()
    text = ""
    for char in sztring:
        stack.put(char)
    while not stack.empty():
        text += stack.get()
    return text

print(reverser("Maciek"))
x = "Maciek"
print(x[::-1])


