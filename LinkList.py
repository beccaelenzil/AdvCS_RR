
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
        self.head.setNext(self.head)
        self.head.setData(item)

    def size(self):
        ref = self.head
        count = 0
        while ref.next.data != None:
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

l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
print l.size()