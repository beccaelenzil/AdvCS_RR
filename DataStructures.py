class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def stacklessparChecker(str):
    a = 0
    for i in range(len(str)):
        a += 1 if str[i] == '(' else -1
        if a < 0:
            return False
    return False if a > 0 else True

def parChecker(str):
    s = Stack()
    for i in range(len(str)):
        if str[i] == '(':
            s.push("(")
        else:
            if s.isEmpty():
                return False
            else:
                s.pop()
    return True if s.isEmpty() else False

def balSymChecker(str):
    s = Stack()
    for i in range(len(str)):
        if str[i] == '(' or str[i] == "{" or str[i] == "[":
            s.push(str[i])
        else:
            if s.isEmpty():
                return False
            else:
                var = s.pop()
                if not((var == "(" and str[i] == ")") or (var == "{" and str[i] == "}") or (var == "[" and str[i] == "]")):
                    return False
    return True if s.isEmpty() else False

def divideByTwo(int):
    s = Stack()
    while int != 0:
        s.push(str(int%2))
        int = int//2
    return "".join([s.pop() for i in range(s.size())])
def divideByN(int,n):
    s = Stack()
    while int != 0:
        s.push(str(int%n))
        int = int//n
    return "".join([s.pop() for i in range(s.size())])

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def hotPotato(nameList, num):
    q = Queue()
    for name in nameList:
        q.enqueue(name)
    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()

print "The winner is Susan == ", hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7)