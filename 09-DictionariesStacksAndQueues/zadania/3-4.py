import queue

remainders = queue.LifoQueue()

def to_bin(n):
    while n != 0:
        remainder = round(n%2)
        remainders.put(remainder)
        n //= 2


to_bin(18)
while not remainders.empty():
    print(remainders.get(), end="")
