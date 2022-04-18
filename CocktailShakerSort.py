import random
random.seed(10) 
def CocktailShakerSort(arr):
    comprehensionCounter = 0
    for _ in range(len(arr)):
        isSwaped = False
        for fowardIndex in range(len(arr) - 1):
            currentItem = arr[fowardIndex]
            nextItem = arr[fowardIndex + 1]
            comprehensionCounter += 1
            if (nextItem < currentItem):
                # swap between them
                arr[fowardIndex + 1] = currentItem
                arr[fowardIndex] = nextItem
                isSwaped = True

        comprehensionCounter += 1
        if not isSwaped:
            break

        for backIndex in range(len(arr) - 1, 0, -1):
            nextItem = arr[backIndex - 1]
            currentItem = arr[backIndex]
            comprehensionCounter += 1
            if (nextItem > currentItem):
                # swap between them
                arr[backIndex] = nextItem
                arr[backIndex - 1] = currentItem
                isSwaped = True

        comprehensionCounter += 1
        if not isSwaped:
            break
        continue

        
        
        
            
    return arr, comprehensionCounter

data = [105, 110, 100, 80, 85]
print(CocktailShakerSort(data), 'worst case')

data = [-9, -2, 0, 11, 45]
print(CocktailShakerSort(data), 'best case')
anotherExample = [random.randint(-1000, 1000) for _ in range(30)]
anotherExample2 = [random.randint(-100, 100) for _ in range(30)]
print('CocktailShakerSort(anotherExample)', '*' * 100)
print(CocktailShakerSort(anotherExample))
print('CocktailShakerSort(anotherExample2)', '*' * 100)
print(CocktailShakerSort(anotherExample2))
