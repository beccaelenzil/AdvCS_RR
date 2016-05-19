import copy

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class LinkedList:
    def __init__(self):
        self.head = Node(None)

    def __repr__(self):
        stg = ""
        ref = self.head
        for i in range(self.size()):
            stg += str(ref.data) + ","
            ref = ref.next
        return stg

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        self.head.next = copy.copy(self.head)
        self.head.data = item

    def size(self):
        ref = self.head
        count = 0
        while ref.data != None:
            count += 1
            ref = ref.getNext()
        return count

    def search(self, item):
        ref = self.head
        while ref.next.data != None and ref.getData() != item:
            ref = ref.getNext()
        return True if ref.getData() == item else False

    def remove(self, item):
        if self.head.data == item:
            self.head = self.head.next
            return True
        if not self.search(item):
            return False
        ref = self.head
        while ref.getData() != item:
            ref = ref.next
        ref.next = ref.next.next
        return True

    def append(self,item):
        ref = self.head
        while ref.data != None:
            ref = ref.next
        ref.data = item
        ref.next = Node(None)

    def insert(self,item,index):
        ref = self.head
        for i in range(index):
            ref = ref.next
        ref.next = copy.copy(ref)
        ref.data = item

    def pop(self):
        item = self.head.data
        self.head = copy.copy(self.head.next)
        return item

    def getAtIndex(self,index):
        ref = self.head
        for i in range(index):
            ref = ref.next
        return ref.data

    def removeFront(self):
        self.head = copy.copy(self.head.next)

    def removeAtIndex(self,index):
        temp = LinkedList()
        ref = self.head
        for i in range(index):
            temp.add(ref.data)
            ref = ref.next
        ref = ref.next
        for i in range(self.size()-index-1):
            temp.add(ref.data)
            ref = ref.next
        self.head = temp.head



l = LinkedList()
l.add("hi")
l.add(5)
l.append("fu")
l.insert("bar",2)
l.removeAtIndex(2)
print l