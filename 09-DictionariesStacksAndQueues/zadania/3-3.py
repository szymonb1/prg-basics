import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct


slownik = {
   ")": "(",
   "}": "{",
   "]": "["
}

def brackets_ok(expression):
   brackets = queue.LifoQueue()
   for char in expression:
      if char in slownik.values():
         brackets.put(char)
      if char in slownik.keys():
         if slownik[char] == brackets.get():
            pass
         else:
            return False 
   return True if brackets.empty() else False

print(brackets_ok(expression1))
print(brackets_ok(expression2))
print(brackets_ok(expression3))