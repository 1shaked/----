from cmath import inf


heap: list[int] = [200, 180, 100, 90 , 80, 99, 81 , 36, 24] 


def getIndexParent(index: int) -> int:
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


def maxHeap(heap: list[int], index: int ) -> None:
    '''
    This function assuming that the heap is valid as max heap and only the element is the index is out of range
    then it will fix the array as heap by float up the value up.
    so one of the requirements is that you assuming that the value at the index is greater the both parents
    '''
    parentIndex = index

    while True:
        childIndex = parentIndex
        child = heap[childIndex]
        parentIndex = getIndexParent(parentIndex)
        parent = heap[parentIndex]
        if (child > parent and childIndex != 0):
            swap(heap, childIndex , parentIndex)
        else:
            break

def maxHeapifyRec(heap: list[int], index: int) -> list[int]:
    '''
    This function will build the max heapify assuming only the element at the index is smaller then one or both of the children
    '''
    leftChildIndex = getLeftChildIndexSafe(heap, index)
    rightChildIndex = getRightChildIndexSafe(heap, index)
    if leftChildIndex == rightChildIndex and leftChildIndex == -1:
        return heap
    if leftChildIndex == -1:
        leftChildIndex = index
    elif rightChildIndex == -1:
        rightChildIndex = index
    
    leftValue = heap[leftChildIndex]
    rightValue = heap[rightChildIndex]

    largestIndex = index
    if leftValue > heap[largestIndex]:
        largestIndex = leftChildIndex
    if rightValue > heap[largestIndex]:
        largestIndex = rightChildIndex
    
    if largestIndex != index:
        swap(heap, index, largestIndex)
        maxHeapifyRec(heap, largestIndex)
    return heap

def maxHeapDown(heap: list[int], index: int) -> list[int]:
    '''
    heap the list of int of your heap
    index: the index of the element to start from
    '''
    while True:
        parentIndex = index 
        leftChildIndex: int = getLeftChildIndexSafe(heap,parentIndex)
        rightChildIndex: int = getRightChildIndexSafe(heap, parentIndex)

        if leftChildIndex == rightChildIndex and rightChildIndex == -1:
            break
        elif rightChildIndex == -1:
            rightChildIndex = index
        elif leftChildIndex == -1:
            leftChildIndex = index

        leftChild: int = heap[leftChildIndex]
        rightChild: int = heap[rightChildIndex]
        largestIndex = index
        if leftChild > heap[largestIndex]:
            largestIndex = leftChildIndex
        if rightChild > heap[largestIndex]:
            largestIndex = rightChildIndex
        if largestIndex != index:
            swap(heap, index, largestIndex)
            index = largestIndex
        else: 
            break
    return heap
        

def minHeap(heap: list[int], index) -> None:
    '''
    This function will assume that there is only one element in the heap that is not is the correct position
    and will assume that it is greater and needed to be float down
    '''
    parentIndex = index
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
    This function will float the element down in min heap
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



def maxHeapRec(heap: list[int], index: int)-> dict[str, list[int]]:
    leftNodeIndex: int  = getLeftChildIndexSafe(heap, index)
    rightNodeIndex: int = getRightChildIndexSafe(heap, index)
    if  rightNodeIndex == leftNodeIndex:
        return heap
    if rightNodeIndex == -1:
        rightNodeIndex = index
    elif leftNodeIndex == -1:
        leftNodeIndex = index
    
    maxHeapRec(heap , leftNodeIndex)
    maxHeapRec(heap , rightNodeIndex)

    leftNodeValue: int = heap[leftNodeIndex]
    rightNodeValue: int = heap[rightNodeIndex]
    largest: int = index
    if heap[largest] < leftNodeValue:
        largest = leftNodeIndex
    if heap[largest] < rightNodeValue:
        largest = rightNodeIndex
    if  index != largest:
        swap(heap, largest, index)
    return heap




def maxHeapDel(heap: list[int], index: int): 
    '''
    this function assuming that you have element with the value you want to delete and you choose the index 
    and the function will delete the element from the heap 
    and will maintain the max heap property, but remember the actual structure of the heap tree will probably be changed
    '''
    swap(heap, len(heap) - 1, index)
    heap.pop()
    parent = heap[getIndexParent(index)]
    if parent > heap[index]:
        maxHeapDown(heap, index)
    else:
        maxHeap(heap, index)





def buildMaxHeap(heap: list[int]) -> list[int]:
    '''
    This function will build the max heap in O(2n) ~ O(n)
    '''
    middle: int = int((len(heap) +1) / 2)
    # for index in range(0, middle):
    for index in range(middle, -1, -1):
        heap = maxHeapDown(heap, index)
        
        # arr.append(heap[0])
        # heap = heap[1::]

    return heap 

def heapSort(heap: list[int]) -> list[int]:
    '''
    This function will sort the list in a descending order in O(log(n) * n)
    '''
    heap:list[int] = buildMaxHeap(heap)
    arr: list[int] = []
    for _ in range(len(heap)):
        heap = maxHeapDown(heap, 0)
        arr.append(heap[0])
        heap = heap[1::]
    return arr
# maxHeapDel(heap, 2)
# minHeap = [0, 1, 2 , 3, 4 , 5 , 6 , 7 , 8 , 9, 10 , 11 , 12 , 13]
# print(minHeap)
def heapUpdateKey(heap: list[int], index: int, value: int) -> list[int]:
    if heap[index] > value:
        heap[index] = value
        heap = maxHeapDown(heap, index)
        return heap
    elif heap[index] == value:
        return heap
    
    heap[index] = value
    while heap[getIndexParent(index)] < heap[index]:
        swap(heap, getIndexParent(index), index)
        index = getIndexParent(index)

    return heap
    
def heapInsertKey(heap: list[int], value: int):
    heap.append(value)
    heap = heapUpdateKey(heap, len(heap) - 1, value)
    return heap

def extractMaxHeap(heap: list[int]) -> list[int]:
    '''
    This function will remove the biggest element from the heap and return the new heap in O(log(n))
    '''
    swap(heap , 0, len(heap) - 1)
    heap.pop()
    heap = maxHeapDown(heap, 0)
    return heap

'''
# build max heap by heap sort 
heap = [5,4,8, 5,19, 20, 17]
res = buildMaxHeap(heap)
print(res)
'''
# heap = [0, 100 , 200 , 50, 25, 70 , 80, 10 , 20 ,15, 12]
# res = heapSort(heap)
# print(res)
# res = maxHeapifyRec(heap, 0)
# print(res)
# maxHeapDown(heap, 0)
# print(heap)
'''
heap = [0 , 1 , 2, 3 , 4, 5, 6]
# res = buildMaxHeap(heap)
res = heapSort(heap)
print(res)
'''


'''
heap = [15, 13, 9, 5,12, 8, 7, 4, 0, 6, 2, 1]
res= extractMaxHeap(heap)
print(res)
'''
'''
heap = [15, 13, 9, 5,12, 8, 7, 4, 0, 6, 2, 1]
res = heapUpdateKey(heap, 5, 20)
print(res)
'''

'''
# showing how to create a heap from a list of elements
arr = []
heap = [15, 13, 9, 5,12, 8, 7, 4, 0, 6, 2, 1]
for i in heap:
    arr = heapInsertKey(arr, i)
print(arr)
'''
