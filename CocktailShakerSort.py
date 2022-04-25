import random
from turtle import backward
random.seed(10) 
def CocktailShakerSort(arr):
    comprehensionCounter = 0
    for looperIndex, _ in enumerate(arr):
        backwardItems = -1 * (looperIndex + 1)
        isSwapped = False
        for forwardIndex, currentItem in enumerate(arr[looperIndex:backwardItems]):
            nextItem = arr[forwardIndex + 1]
            comprehensionCounter += 1
            if (nextItem < currentItem):
                # swap between them
                arr[forwardIndex + 1] = currentItem
                arr[forwardIndex] = nextItem
                isSwapped = True

        comprehensionCounter += 1
        if not isSwapped:
            break

        for backIndex in range(len(arr) + backwardItems, looperIndex, -1): #enumerate(arr[looperIndex:backwardItems]): #range(len(arr) - 1, 0, -1):
            nextItem = arr[backIndex - 1]
            currentItem = arr[backIndex]
            comprehensionCounter += 1
            if (nextItem > currentItem):
                # swap between them
                arr[backIndex] = nextItem
                arr[backIndex - 1] = currentItem
                isSwapped = True

        comprehensionCounter += 1
        if not isSwapped:
            break
        continue

        
        
        
            
    return arr, comprehensionCounter

data = [0, 100, 200, 50, -1]
print(CocktailShakerSort(data), 'worst case')

data = [-9, -2, 0, 11, 45]
print(CocktailShakerSort(data), 'best case')
anotherExample = [random.randint(-1000, 1000) for _ in range(30)]
anotherExample2 = [random.randint(-100, 100) for _ in range(30)]
print('CocktailShakerSort(anotherExample)', '*' * 100)
print(CocktailShakerSort(anotherExample))
print('CocktailShakerSort(anotherExample2)', '*' * 100)
print(CocktailShakerSort(anotherExample2))
