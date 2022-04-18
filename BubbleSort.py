
import random
random.seed(10) 
def BubleSort(arr):
    comprehensionCounter = 0
    for _ in arr:
        wasSwaped = False
        for index, item in enumerate(arr[:-1]):
            nextItem = arr[index+1]
            comprehensionCounter += 1
            if (nextItem < item):
                # swap them
                arr[index+1] = item
                arr[index] = nextItem
                wasSwaped = True

        comprehensionCounter += 1
        if not wasSwaped:
            break
    return arr, comprehensionCounter
    
data = [-2, 45, 0, 11, -9]
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