import queue

n = 0
stack = queue.LifoQueue()

def dodaj(nr):
    global n
    stack.put(nr)
    n+=1
    return f"dodano do kolejnki {nr}"
def usun():
    global n
    n-=1
    return f"nr {stack.get()} do okienka"



print(dodaj(n))
print(dodaj(n))
print(usun())
print(dodaj(n))