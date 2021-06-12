array = [3,5,6,1,2,4]
print(max(array))

def find_max_num(array):
  max = array[0]
  for i in array:
    if max < i:
      max = i
  return max
  
print(find_max_num(array))