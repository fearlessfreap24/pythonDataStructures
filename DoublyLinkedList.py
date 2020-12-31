class LinkedList(): 
    
    class Node():
        
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None


    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    

    def add(self, data):
        newNode = self.Node(data)
        newNode.next = self.head
        if self.head != None:
            self.head.prev = newNode
        self.head = newNode
        self.size += 1
        if self.tail == None:
            self.tail = newNode


    def addRear(self, data):
        newNode = self.Node(data)
        if self.tail != None:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode
        self.size += 1


    def removeFirst(self):
        if self.head == None and self.tail == None:
            return None
        
        temp = self.head.data
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        self.size -= 1
        return temp
        
    
    def removeLast(self):
        if self.head == None and self.tail == None:
            return None

        if self.head == self.tail:
            return self.removeFirst()
        else:
            previous = None
            temp = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return temp


    def remove(self, data):
        previous = None
        current = self.head

        while current != None:
            if current.data == data:
                # 2, 3
                if current == self.head:
                    return self.removeFirst()
                # 4
                if current == self.tail:
                    return self.removeLast()
                # 5
                self.size -= 1
                current.next.prev = previous
                previous.next = current.next
                return current.data
            previous = current
            current = current.next
        # 1, not found
        return None

        
    def contains(self, data):
        current = self.head

        while current != None:
            if current.data == data:
                return True
            current = current.next

        return False

    
    def peekHead(self):
        if self.head == None:
            return None
        else:
            return self.head.data


    def peekTail(self):
        if self.tail == None:
            return None
        else:
            return self.tail.data


# boundary conditions
# 1. empty list
# 2. single element
# 3. working at beginning
# 4. working a the and
# 5. working in the middle


if __name__ == "__main__":
    ll = LinkedList()
    print(f"peekHead = {ll.peekHead()}, peekTail = {ll.peekTail()}")
    print(f"adding one {ll.add('one')}")
    print(f"peekHead = {ll.peekHead()}, peekTail = {ll.peekTail()}")
    print(f"adding two {ll.add('two')}")
    print(f"peekHead = {ll.peekHead()}, peekTail = {ll.peekTail()}")
    print(f"adding three {ll.add('three')}")
    print(f"peekHead = {ll.peekHead()}, peekTail = {ll.peekTail()}")
    print(f"adding four {ll.add('four')}")
    print(f"peekHead = {ll.peekHead()}, peekTail = {ll.peekTail()}")
    print(f"adding five to the rear {ll.addRear('five')}")
    print(f"peekHead = {ll.peekHead()}, peekTail = {ll.peekTail()}")
    print(f"current size - {getattr(ll,'size')}")
    print(f"remove three - {ll.remove('three')}")
    print(f"current size - {getattr(ll,'size')}")
    print(f"peekHead = {ll.peekHead()}, peekTail = {ll.peekTail()}")
    print(f"remove one - {ll.remove('one')}")
    print(f"current size - {getattr(ll,'size')}")
    print(f"peekHead = {ll.peekHead()}, peekTail = {ll.peekTail()}")
    print(f"remove six - {ll.remove('six')}")
    print(f"current size - {getattr(ll,'size')}")
    print(f"peekHead = {ll.peekHead()}, peekTail = {ll.peekTail()}")
    print(f"Is one in the list? {ll.contains('one')}")
    print(f"Is two in the list? {ll.contains('two')}")
    print(f"Is three in the list? {ll.contains('three')}")
    print(f"Is four in the list? {ll.contains('four')}")
    print(f"Is five in the list? {ll.contains('five')}")
    print(f"Is six in the list? {ll.contains('six')}")

    