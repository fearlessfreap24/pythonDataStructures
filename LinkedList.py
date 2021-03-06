class LinkedList(): 
    
    class Node():
        
        def __init__(self, data):
            self.data = data
            self.next = None


    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.index = 0
    

    def add(self, data):
        newNode = self.Node(data)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
        if self.tail == None:
            self.tail = newNode


    def addRear(self, data):
        newNode = self.Node(data)
        if self.tail != None:
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
            current = self.head
            while current != self.tail:
                previous = current
                current = current.next
            previous.next = None
            self.tail = previous
            self.size -= 1
            return current.data


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


    def __iter__(self):
        return self


    def __next__(self):
        if self.index >= self.size:
            self.index = 0
            raise StopIteration
        node = self.head
        for i in range(self.index):
            node = node.next 
        self.index += 1
        return node.data



# boundary conditions
# 1. empty list
# 2. single element
# 3. working at beginning
# 4. working a the and
# 5. working in the middle


if __name__ == "__main__":
    ll = LinkedList()
    
    for i in range(10):
        ll.add({f'user': f'user{i}', 'password': f'password{i}'})

    for num in ll:
        print(num)
        
    for num in ll:
        print(num)

    