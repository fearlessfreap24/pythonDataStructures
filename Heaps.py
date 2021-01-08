import math

# child = 2 x parent + 1, 2 x parent + 2
# parent = floor(child - 1 / 2)
class Heaps:

    class MaxHeap:

        def __init__(self):
            self.dataArr = []
            self.lastPos = len(self.dataArr)

        
        def add(self, data):
            self.dataArr.append(data)
            self.trickleUp(len(self.dataArr) - 1)
            self.lastPos += 1


        def remove(self):
            data = self.dataArr[0]
            self.dataArr[0] = self.dataArr[-1]
            self.dataArr.pop()
            self.lastPos = len(self.dataArr) - 1
            self.trickleDown(0)
            return data


        def swap(self, fromLocation, toLocation):
            temp = self.dataArr[fromLocation]
            self.dataArr[fromLocation] = self.dataArr[toLocation]
            self.dataArr[toLocation] = temp


        def trickleUp(self, position):
            if position == 0:
                return
            else:
                parent = int(math.floor((position - 1)/2))
                if self.dataArr[parent] < self.dataArr[position]:
                    self.swap(position, parent)
                    self.trickleUp(parent)


        def trickleDown(self, parent):
            left = 2*parent+1
            right = 2*parent+2
            
            if left > self.lastPos - 1 and right > self.lastPos -1:
                return

            if left == (self.lastPos - 1):
                if self.dataArr[parent] < self.dataArr[left]:
                    self.swap(parent, left)
                return
            if right == (self.lastPos - 1):
                if self.dataArr[parent] < self.dataArr[right]:
                    self.swap(parent, right)
                return
            if self.dataArr[left] > self.dataArr[right] and self.dataArr[parent] < self.dataArr[left]:
                self.swap(parent, left)
                self.trickleDown(left)
            elif self.dataArr[parent] < self.dataArr[right]:
                self.swap(parent, right)
                self.trickleDown(right)


    class MinHeap:

        def __init__(self):
            self.dataArr = []
            self.lastPos = len(self.dataArr)

        
        def add(self, data):
            self.dataArr.append(data)
            self.trickleUp(len(self.dataArr) - 1)
            self.lastPos = len(self.dataArr)


        def remove(self):
            data = self.dataArr[0]
            self.dataArr[0] = self.dataArr[-1]
            self.dataArr.pop()
            self.lastPos = len(self.dataArr) - 1
            self.trickleDown(0)
            return data


        def swap(self, fromLocation, toLocation):
            temp = self.dataArr[fromLocation]
            self.dataArr[fromLocation] = self.dataArr[toLocation]
            self.dataArr[toLocation] = temp


        def trickleUp(self, position):
            if position == 0:
                return
            else:
                parent = int(math.floor((position - 1)/2))
                if self.dataArr[parent] > self.dataArr[position]:
                    self.swap(position, parent)
                    self.trickleUp(parent)


        def trickleDown(self, parent):
            left = 2*parent+1
            right = 2*parent+2
            
            if left > self.lastPos - 1 and right > self.lastPos -1:
                return

            if left == (self.lastPos - 1):
                if self.dataArr[parent] > self.dataArr[left]:
                    self.swap(parent, left)
                return
            if right == (self.lastPos - 1):
                if self.dataArr[parent] > self.dataArr[right]:
                    self.swap(parent, right)
                return
            if self.dataArr[left] < self.dataArr[right]:
                if self.dataArr[parent] > self.dataArr[left]:
                    self.swap(parent, left)
                    self.trickleDown(left)
            else:
                if self.dataArr[parent] > self.dataArr[right]:
                    self.swap(parent, right)
                    self.trickleDown(right)


if __name__ == "__main__":
    
    import random
    testrange = 100
    # heap = Heaps.MinHeap()
    heap = Heaps.MaxHeap()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(testrange):
        heap.add(alphabet[random.randrange(26)])

    print(heap.dataArr)

    
    for i in range(testrange):
        print(heap.remove())
    print(heap.dataArr)
    
    