from turtle import right


arr =  [4,8,2,3,6,5,1,7]

def quickSort(arr: list[int]):
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return [arr[1], arr[0]]
        return arr
    if len(arr) == 0 or len(arr) == 1:
        return arr
    index: int = int(len(arr) / 2)
    pivot: int = arr[index]
    i: int = 0
    j: int = 0
    while j < len(arr):
        val = arr[i]
        if val <= pivot and i > index: # right side of the pivot
            del arr[i]
            arr.insert(index, val)
            index += 1

        elif val > pivot and index > i: # left side of the pivot
            del arr[i]
            arr.append(val)
            index -= 1
            i -= 1
        i += 1
        j += 1  

    left: list[int] = arr[: index]
    right: list[int] = arr[index :]
    lSide = quickSort(left)
    rSide = quickSort(right)
    return lSide + rSide

print(quickSort(arr))