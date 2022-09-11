from cmath import inf


heap: list[int] = [200, 180, 100, 90 , 80, 99, 81 , 36, 24] 


def getIndexParent(index) -> int:
    nIndex = index / 2
    if isinstance(nIndex, int):
        return nIndex - 1
    return int(nIndex - 0.5)

def swap(heap: list[int], firstIndex: int, secondIndex: int) -> None:
    temp = heap[firstIndex]
    heap[firstIndex] = heap[secondIndex]
    heap[secondIndex] = temp

def getIndexLeftChild(index) -> int:
    return index * 2 + 1

def getIndexRightChild(index) -> int:
    return index * 2 + 2


def getLeftChildIndexSafe(heap: list[int], index: int) -> int:
    if getIndexLeftChild(index) >= len(heap):
        return -1
    return getIndexLeftChild(index)


def getRightChildIndexSafe(heap: list[int], index: int) -> int:
    if getIndexRightChild(index) >= len(heap):
        return -1
    return getIndexRightChild(index)


def maxHeap(heap: list[int]) -> None:
    parentIndex = len(heap) - 1

    while True:
        childIndex = parentIndex
        child = heap[childIndex]
        parentIndex = getIndexParent(parentIndex)
        parent = heap[parentIndex]
        if (child > parent and childIndex != 0):
            swap(heap, childIndex , parentIndex)
        else:
            break


def minHeap(heap: list[int]) -> None:
    parentIndex = len(heap) - 1
    while True:
        childIndex = parentIndex
        child = heap[childIndex]
        parentIndex = getIndexParent(parentIndex)
        parent = heap[parentIndex]
        if (child < parent and childIndex != 0):
            swap(heap, childIndex, parentIndex)
        else:
            break

def minHeapDown(heap: list[int], index: int):
    '''
    heap the list of int of your heap
    index: the index of the element to start from
    '''
    while True:
        parentIndex: int = index 
        parent: int = heap[parentIndex]
        leftChildIndex: int = getLeftChildIndexSafe(heap,parentIndex)
        leftChild: int = heap[leftChildIndex]
        if leftChildIndex == -1:
            leftChild = inf
        
        rightChildIndex: int = getRightChildIndexSafe(heap, parentIndex)
        rightChild: int = heap[rightChildIndex]
        if rightChildIndex == -1:
            rightChild = inf

        if rightChild == inf and leftChild == inf:
            break
        if rightChild > leftChild and leftChild < parent:
            index: int = getIndexLeftChild(index)
        elif rightChild < leftChild and rightChild < parent:
            index: int = getIndexRightChild(index)  
        else: 
            break
        swap(heap, index, parentIndex)

def maxHeapDown(heap: list[int], index: int):
    '''
    heap the list of int of your heap
    index: the index of the element to start from
    '''
    while True:
        parentIndex = index 
        parent = heap[parentIndex]
        leftChildIndex: int = getLeftChildIndexSafe(heap,parentIndex)
        leftChild: int = heap[leftChildIndex]
        if leftChildIndex == -1:
            leftChild = inf
        
        rightChildIndex: int = getRightChildIndexSafe(heap, parentIndex)
        rightChild: int = heap[rightChildIndex]
        if rightChildIndex == -1:
            rightChild = inf

        if rightChild == inf and leftChild == inf:
            break
        if rightChild > leftChild and leftChild < parent:
            index: int = getIndexLeftChild(index)
        if rightChild > leftChild and rightChild > parent:
            index = getIndexRightChild(index)
        elif rightChild < leftChild and leftChild > parent:
            index = getIndexLeftChild(index)  
        else: 
            break
        swap(heap, index, parentIndex)






def minHeapDel(heap: list[int], index: int): 
    last_el = heap[len(heap) - 1]
    swap(heap, last_el, index)
    heap.pop()
    minHeapDown(heap, index)

def maxHeapDel(heap: list[int], index: int): 
    last_el = heap[len(heap) - 1]
    print(last_el)
    swap(heap, len(heap) - 1, index)
    heap.pop()
    parent = heap[getIndexParent(index)]
    if parent > heap[index]:
        maxHeapDown(heap, index)
    else:
        maxHeap(heap, index)

def addMaxHeap(heap: list[int], el: int):
    heap.append(el)
    maxHeap(heap)
    return heap

def addMinHeap(heap: list[int], el: int):
    heap.append(el)
    maxHeap(heap)
    print(heap)
    return heap






# maxHeapDel(heap, 2)
minHeap = [0, 1, 2 , 3, 4 , 5 , 6 , 7 , 8 , 9, 10 , 11 , 12 , 13]
minHeapDel(minHeap, 2)
print(minHeap)
