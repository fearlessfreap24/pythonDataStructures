# from LinkedList import LinkedList
from DoublyLinkedList import LinkedList
import time
import random

def testAddFirstRemLast(n):
    ll = LinkedList()

    startLoad = time.time()
    for i in range(n):
        ll.add(i)
    print(f"addFirst {n} items: Load time = {time.time() - startLoad}")
    if ll.size != n:
        return False

    startRemove = time.time()
    for i in range(n):
        x = ll.removeLast()
        if x != i:
            return False
    print(f"removeLast {n} items: Remove time = {time.time() - startRemove}")

    if ll.size != 0:
        return False

    return True

def testAddLastRemFirst(n):
    ll = LinkedList()
    
    startLoad = time.time()
    for i in range(n):
        ll.addRear(i)
    print(f"addLast {n} items: Load time = {time.time() - startLoad}")

    if ll.size != n:
        return False

    startRemove = time.time()
    for i in range(n):
        x = ll.removeFirst()
        if x != i:
            return False
    print(f"removeFirst {n} items: Remove time = {time.time() - startRemove}")

    if ll.size != 0:
        return False
    
    return True


def testRemove(n):
    ll = LinkedList()
    for i in range(n):
        ll.add(i)

    listN = [i for i in range(n)]
    while len(listN) != 0:
        randNum = random.choice(listN)
        x = ll.remove(randNum)
        if x != randNum:
            return False
        listN.remove(randNum)
    
    return True

def testContains(n):
    ll = LinkedList()

    for i in range(n):
        ll.add(i)

    randNum = random.randrange(n)
    startContains = time.time()
    hasRandNum = ll.contains(randNum)
    endContains = time.time()
    print(f"contains \"{randNum}\" out {n} items: {endContains - startContains}")
    return hasRandNum


def testContinuity(n):
    
    ll = LinkedList()
    
    for i in range(n):
        ll.add(i)
    
    return {'head': ll.continuityCheck(n), 'tail': ll.continuityCheck(n, end='tail')}
    


def main():
    testSize = 10000
    addFirstRemLast = testAddFirstRemLast(testSize)
    print(f"Testing addFirst removeLast - {addFirstRemLast}")
    addLastRemFirst = testAddLastRemFirst(testSize)
    print(f"Testing addLast removeFirst - {addLastRemFirst}")
    remove = testRemove(testSize)
    print(f"Testing Remove - {remove}")
    contains = testContains(testSize)
    print(f"Testing contains - {contains}")
    continuityCheck = testContinuity(testSize)
    print(f"Testing Continuity - from head: {continuityCheck['head']}, from tail: {continuityCheck['tail']}")


if __name__ == "__main__":
    
    main()