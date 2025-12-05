import queue
stack = queue.LifoQueue()


stack.put(2)
stack.put(3)
stack.put(7)
stack.put(4)
stack.put(1)
stack.put(9)
stack.put(8)

sum = stack.get() + stack.get()

print(sum)