
def stateIncrement(v:int ,stats: int) -> int:
    return (v + 1) % stats

def clickForState(v: int, k: int, desireState: int) -> int:
    countForState = 0
    while v != desireState:
        v = stateIncrement(v, k)
        countForState += 1
    return countForState

def clickOnIndexWithState(arr: list[int], k: int, desiredState: int, index: int) -> int:
    countInside = clickForState(arr[index], k, desiredState)
    for i in range(index, len(arr)):
        for _ in range(0, countInside):
            arr[i] = stateIncrement(arr[i], k)

    return countInside

def flip(arr: list[int], desireState: int, k):
    count = 0
    for index,val in enumerate(arr):
        if val != desireState:
            clicks = clickOnIndexWithState(arr, k, desireState, index)
            count += clicks
        
    print(arr)
    return count
    

def clickBool(arr: list[bool], index: int) -> None:
    for i in range(index, len(arr)):
        arr[i] = not arr[i]
def flipBol(arr: list[bool]) -> int:
    '''
    the goal is to count the amount of clicks in order to change all light bold to on
    note that if you click on the k element then all elements from [k::] will flip there state
    '''
    currentState = arr[-1]
    index = len(arr) - 1
    count = 0
    while index != 0:
        previousIndex = index - 1
        previousState = arr[previousIndex]
        if currentState != previousState:
            clickBool(arr, index)
            count += 1
            currentState = previousState
        index = previousIndex
    if not currentState:
        clickBool(arr, index)
        count += 1


    print(arr)
    return count


def flipBoolForward(arr: list[bool]):
    '''
    the goal is to count the amount of clicks in order to change all light bold to on
    note that if you click on the k element then all elements from [k::] will flip there state
    '''
    count = 0
    for index ,val  in enumerate(arr):
        if val:
            continue
        clickBool(arr, index)
        count += 1
    print(arr)
    return count

'''a = [0,1,0,1,0,1,0,1, 0 , 1, 0 , 1, 0 ,1]
b = [0,1,0,1,0,1,0,1, 0 , 1, 0 , 1, 0 ,1]
bool_arr_a: list[bool] = [bool(x) for x in a]
bool_arr_b: list[bool] = [bool(x) for x in b]

c_1 = flipBoolForward(bool_arr_a)
c_2 = flipBol(bool_arr_b)

count_flip = flip([0,1,3,2,1,0,2,3,1], 1, 4)

print(count_flip)
'''

v = c_2 = flipBol([False, True, False])