def combineTwoArray(arr1, arr2):
  first_count = 0
  second_count = 0
  totalArray = []
  while first_count < len(arr1) and second_count < len(arr2):
     first_el = arr1[first_count]
     second_el = arr2[second_count]
     if (first_el < second_el):
       totalArray.append(first_el)
       first_count += 1
       continue
     totalArray.append(second_el)
     second_count += 1
  if (first_count == len(arr1) and second_count < len(arr2)):
    totalArray = totalArray + arr2[second_count:]
  elif (first_count < len(arr1) and second_count == len(arr2)):
    totalArray = totalArray + arr2[second_count::]
  return totalArray

def combineArrays(arrays):
  if (len(arrays) == 2):
    return combineTwoArray(arrays[0], arrays[1])
  else:
    half_size = int(len(arrays) / 2)
    print(half_size)
    f = combineArrays(arrays[0: half_size])
    s = combineArrays(arrays[half_size::])
    return combineTwoArray(f, s)

arrays = [
          [0 ,1 , 2 , 3 , 4, 6],
          [-6 ,-1 , 1 , 2 , 4, 6],
          [-8 ,1 , 5 , 30 , 40, 60],
          [0 ,2 , 4 , 6 , 8, 600],
]
print(combineArrays(arrays))