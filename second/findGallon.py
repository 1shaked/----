import math
def FindDp(n1: int, n2: int, s1: int, s2: int, m: int) -> int:
    if m == 0:
        return 1

    options: dict[int, int] = {n1: 2, n2: 2, s1: 1, s2: 1, abs(n1 - n2): 3}
    if n1 == s1 or n1 == s2:
        options[n1] = 1
    
    if n2 == s1 or n2 == s2:
        options[n2] = 1

    s1Plus2 = s1+s2
    if s1Plus2 > n1:
        key = s1Plus2 - n1
        if key in options:
            options[key] = min(options[key], 2)
        else:
            options[key] = 2
    if s1Plus2 > n2:
        key = s1Plus2 - n2
        if key in options:
            options[key] = min(options[key], 2)
        else:
            options[key] = 2
    

    for i in range(1, m+1):
        currentBest: int = math.inf
        if i in options:
            continue
        for k in options:
            prev = i - k
            if prev not in options:
                continue
            if prev < 0:
                continue
            currentBest = min(currentBest , options[prev] + options[k])
        
        if currentBest != math.inf:
            options[i] = currentBest
    
    return options[m]


print(FindDp(11, 7,2, 6 , 7))