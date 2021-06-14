array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]

def merge(array1, array2):
  array_c = []
  index1 = 0
  index2 = 0
  while index1 < len(array1) and index2 < len(array2):
    if array1[index1] < array2[index2]:
      array_c.append(array1[index1])
      index1 += 1
    else:
      array_c.append(array2[index2])
      index2 += 1
  if index1 == len(array1):
    while index2 < len(array2):
      array_c.append(array2[index2])
      index2 += 1
  if index2 == len(array2):
    while index1 < len(array1):
      array_c.append(array1[index1])
      index1 += 1
      
  return array_c
  
print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!