
import random
random.seed(10) 
def BubleSort(arr):
    comprehensionCounter = 0
    for looperIndex, _ in enumerate(arr):
        wasSwapped = False
        for index, item in enumerate(arr[looperIndex:-1]):
            nextItem = arr[index+1]
            comprehensionCounter += 1
            if (nextItem < item):
                # swap them
                arr[index+1] = item
                arr[index] = nextItem
                wasSwapped = True

        comprehensionCounter += 1
        if not wasSwapped:
            break
    return arr, comprehensionCounter
    
data = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = BubleSort(data)
print(sorted_arr, 'worst case')
data = [-9, -2, 0, 11, 45]
print(BubleSort(data), 'best case')
anotherExample = [random.randint(-1000, 1000) for _ in range(30)]
anotherExample2 = [random.randint(-100, 100) for _ in range(30)]
print('BubleSort(anotherExample)', '*' * 100)
print(BubleSort(anotherExample))
print('BubleSort(anotherExample2)', '*' * 100)
print(BubleSort(anotherExample2))